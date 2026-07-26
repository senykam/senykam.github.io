---
layout: page
permalink: /writing/
title: Writing
description: 
nav: true
nav_order: 1
---

#### Technical Series

{% include writing_list.liquid items=site.data.writing.series %}

#### Essays

{% assign essays = site.posts | where_exp: "post", "post.hidden != true" | where: "kind", "essay" %}
{% include writing_list.liquid items=essays %}

#### Algorithms for the People

{% assign afp = site.algosforthepeople | sort: "date" | reverse %}
{% include writing_list.liquid items=afp %}

#### Misc

{% assign misc = site.data.writing.misc | sort: "date" | reverse %}
{% include writing_list.liquid items=misc %}

