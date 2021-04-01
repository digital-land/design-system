---
contains_map: False
---
# Filter group

Use this component when you have a wide table users will need to scroll horizontally.

{{ designSystemExample({
"iframe": {
    "title": "An example showing the filter group component in action",
    "url": "example.html",
    "size": "s"
},
"example": {
    "path": "digital-land/components/filter-group"
}
}) }}

### Initialise JS module

The `dlFilterGroup` component can be progressively enhanced.

When progressively enhanced it will show (and update) a count of the number of items selected in the group.

```
<script>
    var $filters = document.querySelectorAll('[data-module="selected-counter"]')
    $filters.forEach(filter => {
        new window.DLFrontend.SelectedCounter(filter).init()
    })

    var $filterCheckboxes = document.querySelectorAll('[data-module="filter-checkboxes"]')
    $filterCheckboxes.forEach(el => {
        new window.DLFrontend.FilterCheckboxes(el).init()
    })
</script>
```
