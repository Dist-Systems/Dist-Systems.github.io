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
  {% capture pub_authors %}{% for author in pub.authors %}{{ author }}{% unless forloop.last %}, {% endunless %}{% endfor %}{% endcapture %}
   <h3>{{ pub.title }}</h3>
   <small> {{ pub_authors }}</small>
   <p> {{ pub.date | date: "%B %Y"}} </p> 
   
   {% if pub.paper  %}<a href="/assets/pdf/{{ pub.paper }}" title="Download {{ pub.title }}">Download PDF</a>{% endif %}
   {% if pub.external_url %}<a href="{{ pub.external_url }}" target="_new" title="{{ pub.title }}"><i aria-hidden="" class="fa fa-download"></i>External Download</a>{% endif %}
   {% if pub.video_url %}<a href="{{ pub.video_url }}" target="_new" title="{{ pub.title }}"><i aria-hidden="" class="fa fa-film"></i>Video</a>{% endif %}
   {% if pub.slides %}<a href="{{ pub.slides }}" target="_new" title="{{ pub.title }}"><i aria-hidden="" class="fa fa-chevron-circle-right"></i>Slides</a>{% endif %}
   {% if pub.code %}<i class="fab fa-github-square"></i>{% endif %}
  <a title="{{ pub.title }}" data-target="#{{ pub.slug }}" data-toggle="collapse" aria-expanded="false" aria-controls="{{ pub.slug }}"><i aria-hidden="" class="fa fa-book"></i></a>
  <div class="collapse" id="{{ pub.slug }}" style="font-size: 50%">
  <pre> {{ pub.bibtex }}</pre>
  </div>
{% endfor %}
