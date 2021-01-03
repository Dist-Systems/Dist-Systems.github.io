---
title: Members
layout: collection
permalink: /members/
entries_layout: grid
classes: wide

member_categories:
    - Faculty
    - PhD Students
    - Post-doctoral Researchers
    - Software Engineer
---

{% for category in page.member_categories %}

<div>
<div class="grid__item"><h2 class="page__title">{{ category }}</h2></div>
</div>

<div class="grid__wrapper">
    {% for person in site.members %}
        {% if person.portfolio-item-tag contains "current member" %}
            {% if person.portfolio-item-tag contains category %}
                {% include member-box.html type="grid" %}
            {% endif %}
        {% endif %}
    {% endfor %}
</div>

{% endfor %}
