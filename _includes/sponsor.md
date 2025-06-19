{% if include.type == "platinum" %}
{% assign width = "600px" %}
{% assign min_width = "400px" %}
{% assign max_height = "350px" %}
{% elsif include.type == "gold" %}
{% assign width = "350px" %}
{% assign min_width = "350px" %}
{% assign max_height = "200px" %}
{% elsif include.type == "silver" %}
{% assign width = "300px" %}
{% assign min_width = "250px" %}
{% assign max_height = "150px" %}
{% else %}
{% assign width = "200px" %}
{% assign min_width = "200px" %}
{% assign max_height = "100px" %}
{% endif%}


<div style="flex:1;flex-shrink:0;min-width:{{ min_width }};max-width:{{ width }};margin:auto;padding:20px;min-height:{{max_height}};line-height:{{max_height}};vertical-align: middle;text-align:center;">
  <a href="{{ include.url }}" style="margin:auto"><img src="{{ include.file_path }}" style="width:auto;margin:auto;display:inline-block;max-height: {{max_height}};max-width:{{width}};"/></a>
</div>
