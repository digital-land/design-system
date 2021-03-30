---
contains_map: False
---
# Data table

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

The `dlDataTableWrapper` component is a progressive enhancement. You will need to initialise the JS module for it to work.

```
<script>
    var $data_tables = document.querySelectorAll('[data-module*="data-table"]')
    $data_tables.forEach(data_table => {
        new window.DLFrontend.ScrollableTables(data_table).init()
    })
</script>
```
