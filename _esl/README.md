---
published: false
sitemap: false
---

# Encrypted Systems Lab blog — archive, ready to publish

A markdown copy of the ESL blog at <https://esl.cs.brown.edu/blog/>, taken while
that site was up so the content survives if access to it is lost. All 26 posts
the feed lists, May 2012 to April 2020, about 47,000 words and 21 images.

Everything is already converted and wired for publication. Nothing is live,
because the collection is commented out in `_config.yml`.

## To publish

1. In `_config.yml`, uncomment the `esl:` collection under `collections:` and
   the matching `esl` entry under `defaults:`. That is the whole switch.
2. Add a page listing the posts, the way `/how-to-search-on-encrypted-data/`
   lists its parts. Sort `site.esl` by `date` and pass it to
   `_includes/writing_list.liquid`.
3. Add a bullet on `/writing/`. It is an archive of a former publication rather
   than a series, so it belongs alongside Algorithms for the People rather than
   under Technical Series.

Posts will appear at `/encrypted-systems-lab/<slug>/`. They are a collection
rather than `_posts` deliberately, so republishing decade-old material does not
push 26 items into the feed.

## What was already done

- **Front matter.** `layout: archived-post`, plus `title`, `date`, `slug`,
  `tags`, `source`, and `categories` and `subtitle` where the post had them.
  Dates come from the blog's feed; the pages carry no machine-readable date.
- **Math promoted to `$$…$$`.** 241 dollar-delimited spans in the older posts.
  kramdown does not recognise single `$` as math and would markdown-process the
  LaTeX inside, which is what corrupted the Notes on Power posts before this was
  understood. The `\(..\)` and `\[..\]` spans were left alone, since kramdown
  passes those through and MathJax reads them by default.
- **Cross-links made site-relative.** 24 links between posts now point at
  `/encrypted-systems-lab/<slug>/` instead of the live blog. If the permalink
  changes, one search and replace fixes them. `source:` stays absolute on
  purpose, since it records where the post came from.
- **Images** moved to `assets/img/esl/` and the 27 references repointed.
- **Theme chrome removed.** The trailing `Tags//` line in 17 posts became the
  `tags` field; navigation, category chips and paging were dropped during
  conversion.
- **Footnotes** converted to markdown reference syntax, `[^N]` in the body and
  `[^N]: …` at the foot. Every reference has a matching definition.

## The one thing left, and it needs you

**There is no `author` field**, because the blog's HTML records none and the feed
carries none either. Several of these are lab work rather than solo work, so
authorship has to be filled in by hand before publishing. Doing it afterwards
means publishing colleagues' writing under no byline.

The converters live in `_tools/`: `esl2md.py` built the archive from the live
site and `esl_publish_prep.py` applied the transforms above. They sit outside
this directory because non-markdown files in a collection folder are copied
straight into the published site.

## A caution about the source

Two of the blogs linked from this site have already gone: algosforthepeople.org,
recovered from the Internet Archive, and the older blog that first carried the
*How to Search on Encrypted Data* series, whose posts survive only because they
were re-hosted on ESL. This archive exists so the same thing does not happen a
third time.
