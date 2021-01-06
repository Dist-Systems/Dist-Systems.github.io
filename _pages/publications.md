---
title: Publications
layout: splash
header: 
  image: https://picsum.photos/id/141/1280/100
permalink: /publications/
collection: publications
entries_layout: list
classes: wide
---
{% assign pubs = site.publications  %}
<ul>
{% for pub in pubs reversed %}
  {% capture pub_authors %}{% for author in pub.authors %}{{ author }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
   <h3>{{ pub.title }}</h3>
   <small> {{ pub_authors }}</small>
   <p> {{ pub.date | date: "%B %Y"}} </p> 
   <div style="font-size: 30%"><pre> {{ pub.bibtex }}</pre></div>
{% endfor %}

