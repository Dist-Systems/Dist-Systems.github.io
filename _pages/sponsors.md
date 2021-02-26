---
title: Sponsors
layout: splash
header: 
    image: https://picsum.photos/id/1040/1280/200
permalink: /sponsors/
entries_layout: grid
classes: wide
author_profile: false

---
<div id="main" role="main">
<div class="grid__wrapper">
{% for sponsor in site.data.sponsors %}
<div class="grid__item">
  <a href="{{ sponsor.url }}">
  <img class="sponsor_img" src="/assets/images/logos/{{ sponsor.logo }}" alt="{{ sponsor.name }}" title="{{ sponsor.name }}"></a>
  </div>
{% endfor %}
</div>
</div>

      
