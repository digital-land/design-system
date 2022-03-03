---
requires_orgs: True
---
{{ govukTag({
  "text": "candidate"
}) }}

# Autocomplete 

An example of how to use the autocomplete module.

{{ designSystemExample({
"iframe": {
    "title": "An example autocomplete component used to list all organisations",
    "url": "example.html",
    "size": "s"
},
"example": {
    "path": "digital-land/components/autocomplete"
}
}) }}


### Include the assets

Need to include the required `js` and `css`.

Add the css to the page head. For example

    <link href="{{ staticPath|default('/static') }}/stylesheets/vendor/govuk-accessible-autocomplete.min.css" rel="stylesheet" media="all" />

Add the js to end of the `<body>`. For example

    <script src="{{ staticPath|default('/static') }}/javascripts/vendor/govuk-accessible-autocomplete.min.js"></script>
    <script>
        const $picker = document.querySelector('#organisation-search')
        accessibleAutocomplete.enhanceSelectElement({
            selectElement: $picker
        })
    </script>

