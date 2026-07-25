---
layout: page
permalink: /writing/
title: writing
description: 
nav: true
nav_order: 1
---

<!--
#### Notes on Power

{% assign notes = site.posts | where_exp: "post", "post.hidden != true" | where: "kind", "note" | sort: "series_order" %}
{% if notes.size > 0 %}
{% include writing_list.liquid items=notes ordered=true descriptions=true %}
{% else %}
<p class="post-meta">The first notes are on their way.</p>
{% endif %}
-->

#### Essays

{% assign essays = site.posts | where_exp: "post", "post.hidden != true" | where: "kind", "essay" %}
{% include writing_list.liquid items=essays %}

#### Explainers

{% assign explainers = site.posts | where_exp: "post", "post.hidden != true" | where: "kind", "explainer" %}
{% assign explainers = explainers | concat: site.data.writing.explainers %}
{% include writing_list.liquid items=explainers %}

#### Misc

{% include writing_list.liquid items=site.data.writing.misc %}

