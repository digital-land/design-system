---
contains_map: False
---
# Hero

This component is a blue hero panel. It should be used to introduce a new site, service or significant section.

{{ designSystemExample({
"iframe": {
    "title": "An example of the hero component",
    "url": "example.html",
    "size": "m"
},
"example": {
    "path": "digital-land/components/hero"
}
}) }}

### Hero with button

If you need more control over the elements in the hero component you can you the `call` method.

This allows you to use additional jinja components within the `hero`. For example you might want to include a start button to prompt the user to start a journey of your service.

{{ designSystemExample({
"iframe": {
    "title": "An example of the hero component with a button",
    "url": "example-button.html",
    "size": "m"
},
"example": {
    "path": "digital-land/components/hero"
}
}) }}
