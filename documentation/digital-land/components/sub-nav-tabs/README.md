---
contains_map: False
---
# Sub nav tabs

Use this component when you have a wide table users will need to scroll horizontally.

{{ designSystemExample({
"iframe": {
    "title": "An example showing a wide table wrapped in widetable component",
    "url": "example.html",
    "size": "s"
},
"example": {
    "path": "digital-land/components/data-table"
}
}) }}


### Initialise JS module

The `subNavTabs` component is a progressive enhancement. You will need to initialise the JS module for it to work.

```
<script>
    const $subNavTabs = document.querySelector('[data-module="dlf-subnav"]')
    const subNavTabsComponent = new DLFrontend.SubNavTabs($subNavTabs).init({})
</script>
```
