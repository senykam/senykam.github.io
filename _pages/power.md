---
layout: page
permalink: /power/
title: Notes on Power
description:
og_image: /assets/img/headers/power-notes-slate.png
nav: false
---

#### Overview

{% assign notes = site.posts | where_exp: "post", "post.hidden != true" | where: "kind", "note" | sort: "series_order" %}
{% if notes.size > 0 %}
{% include writing_list.liquid items=notes ordered=true %}
{% else %}
<p class="post-meta">The first notes are on their way.</p>
{% endif %}

{% assign power_essays = site.posts | where_exp: "post", "post.hidden != true" | where: "project", "power" | where: "kind", "essay" %}
{% if power_essays.size > 0 %}

#### Related Essays

{% include writing_list.liquid items=power_essays %}
{% endif %}

