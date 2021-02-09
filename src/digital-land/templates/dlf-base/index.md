---
contains_examples: False
---
# DLF Base

Use this template to keep your pages consistent with the rest of Digital Land.

The [dlf-base.html]() template extends the [GOV.UK template]()

The default max width is 1020px (with margins the content width is 960px). You can make it wider if needed. Using the dlf-base--full-width.html template is another option.

{{ designSystemExample({
"iframe": {
    "title": "An example of a secondary action button",
    "url": "example-basic.html",
    "size": "xl"
},
"example": {
    "path": "digital-land/templates/dlf-base"
}
}) }}

### Options

| Option name  | Option type  | Description |
| ----------- | ----------- | ----------- |
| pageTitle  | block      | Add a title for the page. Will be added to the `<meta>` tag in the head |
| head   | block       | Use this to override the assets digital land loads in the head. |
| dlHead | block | Use this instead of the `head` block to add to the things digital land loads in the head |
| dlMetaTemplate | block | Use this block to add a `<meta name="dl-template" content="TEMPLATE">`, replace TEMPLATE with template name |
| dlCss | block | Use to override the stylesheets digital land loads as default |
| includeAutocomplete | variable | If true the assets needed for the autocomplete component will be loaded |
| includesMap | variable | If true the assets needed for dl maps will be loaded |
| header | block | Inherited from GOV.UK base |
