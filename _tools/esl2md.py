"""Archive the Encrypted Systems Lab blog as markdown."""
import os
import re
import ssl
import sys
import urllib.request
from html.parser import HTMLParser

FEED = "https://esl.cs.brown.edu/blog/index.xml"
BASE = "https://esl.cs.brown.edu"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
VOID = {"br", "img", "hr", "meta", "link", "input", "source", "col"}
MONTHS = dict(Jan=1, Feb=2, Mar=3, Apr=4, May=5, Jun=6,
              Jul=7, Aug=8, Sep=9, Oct=10, Nov=11, Dec=12)


class Node:
    def __init__(self, tag=None, attrs=None):
        self.tag, self.attrs, self.kids, self.text = tag, dict(attrs or {}), [], None


class DOM(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs)
        self.stack[-1].kids.append(n)
        if tag not in VOID:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].kids.append(Node(tag, attrs))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        n = Node()
        n.text = data
        self.stack[-1].kids.append(n)


def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=90, context=CTX).read()
    return data if binary else data.decode("utf-8", "ignore")


def find(node, cls=None, tag=None):
    out = []

    def walk(n):
        if n.tag and (tag is None or n.tag == tag):
            if cls is None or cls in n.attrs.get("class", "").split():
                out.append(n)
        for k in n.kids:
            walk(k)

    walk(node)
    return out


def text_of(node):
    parts = []

    def walk(n):
        if n.text:
            parts.append(n.text)
        for k in n.kids:
            walk(k)

    walk(node)
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def absolute(url):
    """Resolve the blog's relative links against the live site."""
    if not url or url.startswith(("http://", "https://", "mailto:", "#")):
        return url
    url = re.sub(r"^(\.\./)+", "/", url)
    if not url.startswith("/"):
        url = "/" + url
    return BASE + re.sub(r"//+", "/", url)


def esc(s):
    # Deliberately does not escape \ or _. Several posts write LaTeX straight
    # into the prose (\emph{...}, \dots) and dollar-delimited math ($F_K(w_i)$)
    # that Hugo passed through as plain text. Escaping those turns \emph into
    # \\emph and w_i into w\_i, which corrupts the author's original source.
    # Republishing will need a decision on math delimiters either way.
    return re.sub(r"([`*\[\]])", r"\\\1", s)


IMAGES = {}


def render(n, images_dir=None):
    if n.text is not None:
        t = n.text
        if not t.strip():
            return " " if t else ""
        return esc(re.sub(r"\s+", " ", t))

    tag, a = n.tag, n.attrs
    cls = a.get("class", "").split()
    inner = lambda: "".join(render(k, images_dir) for k in n.kids)

    if tag in ("script", "style", "svg", "nav", "form", "button"):
        return ""
    # Math is emitted raw. The blog wraps LaTeX in <span class="math"> using
    # \(..\) and \[..\] delimiters; escaping it would turn \sf into \\sf and
    # _w into \_w. Those delimiters are MathJax defaults and kramdown leaves
    # them alone, so they survive republication as they are.
    if "math" in cls:
        return " " + text_of(n) + " "
    # Structural chrome that is not body content.
    if "post-title" in cls or "post-subtitle" in cls or "post-date" in cls:
        return ""
    if "post-categories" in cls or "paging" in cls or "footnotes" in cls:
        return ""

    # Footnote reference in the body -> [^n]
    if tag == "sup" and a.get("id", "").startswith("fnref:"):
        return "[^%s]" % a["id"].split(":", 1)[1]
    if tag == "a" and a.get("href", "").startswith("#fn:"):
        return "[^%s]" % a["href"].split(":", 1)[1]

    if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        return "\n\n" + "#" * int(tag[1]) + " " + inner().strip() + "\n\n"
    if tag == "p":
        return "\n\n" + inner().strip() + "\n\n"
    if tag in ("em", "i"):
        s = inner().strip()
        return "*%s*" % s if s else ""
    if tag in ("strong", "b"):
        s = inner().strip()
        return "**%s**" % s if s else ""
    if tag == "code":
        return "`%s`" % text_of(n)
    if tag == "pre":
        return "\n\n```\n" + text_of(n) + "\n```\n\n"
    if tag == "a":
        label = inner().strip()
        href = absolute(a.get("href", ""))
        if not label:
            return ""
        return "[%s](%s)" % (label, href) if href else label
    if tag == "img":
        src = absolute(a.get("src", ""))
        name = os.path.basename(src.split("?")[0])
        if images_dir and src.startswith("http") and name:
            IMAGES[src] = name
            src = "img/" + name
        return "\n\n![%s](%s)\n\n" % (a.get("alt", "").strip(), src)
    if tag == "br":
        return "  \n"
    if tag == "hr":
        return "\n\n---\n\n"
    if tag == "blockquote":
        body = "".join(render(k, images_dir) for k in n.kids).strip()
        return "\n\n" + "\n".join("> " + l for l in body.split("\n")) + "\n\n"
    if tag in ("ul", "ol"):
        items = [k for k in n.kids if k.tag == "li"]
        lines = []
        for i, li in enumerate(items, 1):
            marker = "* " if tag == "ul" else "%d. " % i
            body = "".join(render(k, images_dir) for k in li.kids).strip()
            body = re.sub(r"\n{2,}", "\n", body)
            first, *rest = body.split("\n")
            lines.append(marker + first)
            lines += [" " * len(marker) + r for r in rest]
        return "\n\n" + "\n".join(lines) + "\n\n"
    if tag == "table":
        return "\n\n" + text_of(n) + "\n\n"
    return inner()


def tidy(md):
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"[ ]{2,}(?![\n])", " ", md)
    return md.strip() + "\n"


def parse_feed():
    xml = fetch(FEED)
    out = []
    for it in re.findall(r"<item>(.*?)</item>", xml, re.S):
        link = re.search(r"<link>(.*?)</link>", it)
        title = re.search(r"<title>(.*?)</title>", it)
        pub = re.search(r"<pubDate>(.*?)</pubDate>", it)
        if not link:
            continue
        iso = ""
        if pub:
            m = re.search(r"(\d{1,2}) (\w{3}) (\d{4})", pub.group(1))
            if m:
                iso = "%s-%02d-%02d" % (m.group(3), MONTHS[m.group(2)], int(m.group(1)))
        out.append((link.group(1).strip(), (title.group(1) or "").strip(), iso))
    return out


def main():
    outdir = sys.argv[1]
    os.makedirs(os.path.join(outdir, "img"), exist_ok=True)
    posts = parse_feed()
    print("%d posts in the feed\n" % len(posts))
    index = []
    for url, title, date in posts:
        slug = url.rstrip("/").rsplit("/", 1)[-1]
        try:
            html = fetch(url)
        except Exception as e:
            print("  FAILED %-58s %s" % (slug, type(e).__name__))
            continue
        d = DOM()
        d.feed(html)
        secs = find(d.root, cls="post", tag="section")
        if not secs:
            print("  NO CONTENT %s" % slug)
            continue
        sec = secs[0]

        sub = find(sec, cls="post-subtitle")
        subtitle = text_of(sub[0]) if sub else ""
        cats = [text_of(a) for a in find(sec, cls="post-category")]

        IMAGES.clear()
        body = tidy(render(sec, images_dir=True))

        # Footnotes: emit as markdown reference definitions.
        notes = []
        for fn in find(d.root, cls="footnotes"):
            for li in find(fn, tag="li"):
                num = li.attrs.get("id", "").split(":", 1)[-1]
                for ret in find(li, cls="footnote-return"):
                    ret.kids = []
                txt = tidy("".join(render(k) for k in li.kids)).strip()
                txt = re.sub(r"\s*\[return\]\s*$", "", txt)
                if num and txt:
                    notes.append("[^%s]: %s" % (num, txt.replace("\n", " ")))
        if notes:
            body = body.rstrip() + "\n\n" + "\n\n".join(notes) + "\n"

        for src, name in IMAGES.items():
            path = os.path.join(outdir, "img", name)
            if not os.path.exists(path):
                try:
                    open(path, "wb").write(fetch(src, binary=True))
                except Exception as e:
                    print("      image FAILED %s (%s)" % (name, type(e).__name__))

        fm = ["---", 'title: "%s"' % title.replace('"', "'"), "date: %s" % date]
        if subtitle:
            fm.append('subtitle: "%s"' % subtitle.replace('"', "'"))
        if cats:
            fm.append("categories: [%s]" % ", ".join(cats))
        fm += ["slug: %s" % slug, "source: %s" % url, "---", ""]

        fname = "%s-%s.md" % (date or "0000-00-00", slug)
        open(os.path.join(outdir, fname), "w").write("\n".join(fm) + body)
        index.append((date, title, fname, len(body.split()), len(notes)))
        print("  %-13s %-52s %5dw  %2dfn  %2dimg"
              % (date, slug[:52], len(body.split()), len(notes), len(IMAGES)))

    print("\n%d files, %d images" % (len(index),
          len(os.listdir(os.path.join(outdir, "img")))))
    return index


if __name__ == "__main__":
    main()
