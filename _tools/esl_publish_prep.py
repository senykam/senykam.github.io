"""Make the ESL archive publish-ready: tags, math, links, images, layout."""
import os
import re
import shutil
import sys

SRC = "/Users/seny/src/senykam.github.io/_archive/esl"
DST = "/Users/seny/src/senykam.github.io/_esl"
IMGDST = "/Users/seny/src/senykam.github.io/assets/img/esl"
PERMALINK_BASE = "/encrypted-systems-lab"
IMG_BASE = "/assets/img/esl"

os.makedirs(DST, exist_ok=True)
os.makedirs(IMGDST, exist_ok=True)

stats = dict(tags=0, math=0, links=0, imgs=0)

for name in sorted(os.listdir(SRC)):
    if not name.endswith(".md") or name == "README.md":
        continue
    s = open(os.path.join(SRC, name)).read()
    fm, body = s.split("---", 2)[1], s.split("---", 2)[2]

    # 1. The theme's trailing "Tags// a, b, c" line is chrome. Lift the names
    #    into front matter and drop the line.
    tags = []
    def take_tags(m):
        global tags
        tags = re.findall(r"\[([^\]]+)\]\(\S*?/tags/[^)]*\)", m.group(0))
        return ""
    body, n = re.subn(r"(?m)^\s*Tags//.*(?:\n(?!\n).*)*$", take_tags, body)
    if n:
        stats["tags"] += 1

    # 2. Promote dollar-math to $$..$$ so kramdown treats it as math instead of
    #    markdown-processing the LaTeX. Existing \(..\) and \[..\] spans are
    #    protected first: one of them contains \leftarrow_{\$}, a literal dollar
    #    inside math that must not be treated as a delimiter.
    held = []
    def hold(m):
        held.append(m.group(0))
        return "\x00%d\x00" % (len(held) - 1)
    body = re.sub(r"\\\[.*?\\\]|\\\(.*?\\\)", hold, body, flags=re.S)
    body, m_n = re.subn(r"(?<!\$)\$(?!\$)((?:[^$\n]|\n(?!\n))+?)(?<!\$)\$(?!\$)",
                        r"$$\1$$", body)
    stats["math"] += m_n
    body = re.sub(r"\x00(\d+)\x00", lambda m: held[int(m.group(1))], body)

    # 3. Internal cross-links point at the live blog; make them site-relative.
    body, l_n = re.subn(r"https?://esl\.cs\.brown\.edu/+blog/([^)\s]+?)/?(?=[)\s])",
                        PERMALINK_BASE + r"/\1/", body)
    stats["links"] += l_n

    # 4. Images move under assets so they resolve from the post's permalink.
    body, i_n = re.subn(r"\]\(img/", "](" + IMG_BASE + "/", body)
    stats["imgs"] += i_n

    fm = "layout: archived-post\n" + fm.lstrip("\n")
    if tags:
        fm = fm.rstrip("\n") + "\ntags: [%s]\n" % ", ".join(tags)

    open(os.path.join(DST, name), "w").write("---\n" + fm + "---\n" + body)

for f in os.listdir(os.path.join(SRC, "img")):
    shutil.copy2(os.path.join(SRC, "img", f), os.path.join(IMGDST, f))

print("  files written      :", len([f for f in os.listdir(DST) if f.endswith('.md')]))
print("  tag lines lifted   :", stats["tags"])
print("  math spans promoted:", stats["math"])
print("  links rewritten    :", stats["links"])
print("  image refs rewritten:", stats["imgs"])
print("  images copied      :", len(os.listdir(IMGDST)))
