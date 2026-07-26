---
published: false
sitemap: false
---

# Algorithms for the People — recovered archive

The blog that ran at algosforthepeople.org, recovered from the Internet Archive
after the domain was lost. The domain no longer resolves, so the Wayback capture
is the only surviving copy.

Snapshot: <https://web.archive.org/web/20200724014823/http://algosforthepeople.org/>
(24 July 2020)

## What is here

Three posts, which is the entire blog. The Wayback CDX index lists exactly three
post URLs for the site (`/posts/cointelpro/`, `/posts/moral/`, `/posts/intro/`),
so nothing is missing.

| File | Title | Date | Author |
|---|---|---|---|
| `2020-06-26-cointelpro.md` | COINTELPRO | 2020-06-26 | Seny Kamara |
| `2020-06-14-the-moral-character-of-scientific-work.md` | The Moral Character of Scientific Work | 2020-06-14 | 2950v-19 |
| `2020-06-06-intro-overview.md` | Intro & Overview | 2020-06-06 | Seny Kamara |

Cover images are in `img/`, pulled from the same snapshot.

## How it was converted

Generated from the archived HTML rather than retyped. Each post's body was
parsed into a DOM and rendered to markdown, preserving headings, emphasis,
blockquotes, lists and every link. Wayback's URL prefixes were stripped so links
point at their original targets again, and the site's own `./tags/` and
`./authors/` links were dropped in favour of front matter fields.

The result was checked against the standalone post pages in the same snapshot:
link counts match exactly (37, 16 and 1) and word counts match within the
difference introduced by the front matter.

Two things to know when reading:

- The `2950v-19` byline is group authorship for the Fall 2019 class, used
  deliberately so students were not individually identifiable.
- Literal citation brackets such as `\[Chaum81\]` are escaped so markdown does
  not read them as link syntax.

## Not published

This directory starts with an underscore, so Jekyll ignores it and none of it is
built into the site. It is here to preserve the content in version control. Wire
it up as a collection in `_config.yml` if you want it served.
