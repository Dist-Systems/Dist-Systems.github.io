---
title: Sponsors
layout: collection
permalink: /sponsors/
header: 
    image: https://picsum.photos/id/1040/1280/200
---
<ul>
{% for sponsor in site.data.sponsors %}
  <li>
      {{ sponsor.name }}
  </li>
{% endfor %}


      
