---
title: "Fechas"
bg: logo_yellow
color: logo_purple2
style: center
fa-icon: calendar
published: true
---

# ROSCon {{site.roscon_event}} {{site.roscon_year}}
# Fechas importantes


<br>

{% if site.proposals_talks_deadline %}
### Plazo para propuestas de charlas
{{ site.proposals_talks_deadline }}

<br>

{% if site.proposals_workshops_deadline %}
### Plazo para propuestas de workshops / tutorials
{{ site.proposals_workshops_deadline }}
{% endif %}

<br>

{% endif %}
{% if site.early_registration_start %}
### Apertura registro previo
{{ site.early_registration_start }}
{% endif %}

<br>

{% if site.statement_acceptance_talks %}
### Comunicación de aceptación de las charlas
{{ site.statement_acceptance_talks }}
{% endif %}

<br>

{% if site.statement_acceptance_workshops %}
### Comunicación de aceptación de las workshops/tutoriales
{{ site.statement_acceptance_workshops }}
{% endif %}

<br>

{% if site.early_registration_deadline %}
### Fin del registro previo
{{ site.early_registration_deadline }}
{% endif %}

<br>

{% if site.late_registration %}
### Inicio del registro general
{{ site.late_registration }}
{% endif %}

<br>

{% if site.event_date %}
### Día del evento
{{ site.event_date }}
{% endif %}

<br>
