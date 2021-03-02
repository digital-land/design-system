---
contains_map: False
---
# Data record

The data record component is used to show a single record of data. Including all the attributes the make up the record and the resouce it was collected from.

{{ designSystemExample({
"iframe": {
    "title": "An example of a data record panel",
    "url": "example.html",
    "size": "l"
},
"example": {
    "path": "digital-land/components/data-record"
}
}) }}

## Reference cells

Use the `dlDataReferenceCell` macro to change an identifier value to a link through to the related data record. The original identifier is still shown in brackets.

The example below shows how the identifier `local-authority-eng:HAG` is displayed as a link to Harrogate Borough Council along with the identifier.

{{ designSystemExample({
"iframe": {
    "title": "An example of a data record panel with a reference cell",
    "url": "example-reference.html",
    "size": "s"
},
"example": {
    "path": "digital-land/components/data-record"
}
}) }}
