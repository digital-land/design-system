A markdown file
    
{{ 'This is a test StRinG Lowered by a jinja macro'|lower }}
    
And a nice code block
    
```
{% from 'digital-land-frontend/components/feedback-panel/macro.html' import dlFeedbackPanel %}
{% block content %}
<!-- paste dlFeedbackPanel here -->
{% endblock %}
```

And another example

```
{% extends "digital-land-frontend/dlf-base.html" %}
```
