---
contains_examples: False
---
# Index page templates

This templates is used to generate index pages for a set of data we have collected.

The template extends the [dlf-base.html](../dlf-base)

{{ designSystemExample({
"iframe": {
    "title": "An example of a secondary action button",
    "url": "example-basic.html",
    "size": "xl"
},
"example": {
    "path": "digital-land/templates/index-page"
}
}) }}

### Options

Contains all the options available to [dlf-base](../dlf-base).

The index template adds makes more options available.

| Option name  | Option type  | Description |
| ----------- | ----------- | ----------- |
| `data_type` | variable | This is the collection name and is set by the renderer. It can be overridden in the template if needed. |
| `indexTitle` | block | Part of `content` block. Contains the heading displayed on the page |
| `indexList` | block | Part of `content` block. Displays a list of records or the records grouped. |
| `initMapBlock` | block | Part of `bodyEnd` block. JS script the looks for `boundary-map` module and inits the map. |
| `initFilteringBlock` | block | Part of `bodyEnd` block. JS script that sets up any filters on the page - these can be a `FilterList` filter and a `FilterHistorical` filter. |
