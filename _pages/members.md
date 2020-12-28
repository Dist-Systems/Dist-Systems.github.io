---
title: Members
layout: collection
permalink: /members/
collection: members
entries_layout: grid
classes: wide
---

{% for m in site.members %}
<h4><a href="{{ m.url }}">{{ m.title }}</a></h4>
{% endfor %}