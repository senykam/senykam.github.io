---
layout: page
permalink: /power/
title: power
description: A formal theory of power, developed in the open.
nav: false
---

Power is the central concept of a lot of fields and has no formal definition in
any of them. Political science argues about it, law reasons around it and
cryptography keeps running into it without naming it. This project is an attempt
to give it one: a formal account of what it means for an agent to hold power, how
institutions compose out of smaller pieces, and what that composition implies for
privacy, surveillance, fairness and institutional design.

I am writing it as a sequence of notes rather than as a finished book, and
publishing them as they are written. The notes are the public form of a monograph
in progress. They build on each other and are meant to be read in order, and new
ones are announced in the [feed]({{ '/feed.xml' | relative_url }}).

#### The Notes

{% assign notes = site.posts | where_exp: "post", "post.hidden != true" | where: "kind", "note" | sort: "series_order" %}
{% if notes.size > 0 %}
{% include writing_list.liquid items=notes ordered=true descriptions=true %}
{% else %}
<p class="post-meta">The first notes are on their way.</p>
{% endif %}

{% assign power_essays = site.posts | where_exp: "post", "post.hidden != true" | where: "project", "power" | where: "kind", "essay" %}
{% if power_essays.size > 0 %}

#### Related Essays

{% include writing_list.liquid items=power_essays %}
{% endif %}

