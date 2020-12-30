---
title: Members
layout: collection
permalink: /members/
collection: members
entries_layout: grid
classes: wide

member_categories:
    - faculty
    - PhD graduate
    - postdoc
    - graduate student
    - research intern
    - Software Engineer
    - research staff
    - lab visitor
---

{% for category in page.member_categories %}
<div class="grid__wrapper">
<!-- <div class="grid__wrapper"> -->
    {% for person in site.members %}
        {% if person.portfolio-item-tag contains "current member" %}
            {% if person.portfolio-item-tag contains category %}
                {% include member-box.html type="grid" %}
            {% endif %}
        {% endif %}
    {% endfor %}
</div>
{% endfor %}
