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
| `pageTitle`  | block      | Add a title for the page. Will be added to the `<meta>` tag in the head |
| `staticPath` | variable | Option to set the root of the path to static assets, usually set in the renderer |
| `head`   | block       | Use this to override the assets digital land loads in the head. |
| `dlHead` | block | Use this instead of the `head` block to add to the things digital land loads in the head |
| `dlMetaTemplate` | block | Use this block to add a `<meta name="dl-template" content="TEMPLATE">`, replace TEMPLATE with template name |
| `dlMapAssets` | block | This block contains assets needed for the maps on the digital land website |
| `includesMap` | variable | If true the assets needed for dl maps will be loaded |
| `dlCss` | block | Use to override the stylesheets digital land loads as default |
| `includeAutocomplete` | variable | If true the assets needed for the autocomplete component will be loaded |
| `header` | block | Inherited from GOV.UK base. By default, includes our cookie banner and top navigation banner |
| `beforeContent` | block | Inherited from GOV.UK base. Includes prototype banner and breadcrumbs block |
| `dl_breadcrumbs` | block | Hook to insert breadcrumbs component for the page |
| `content` | block | Inherited from GOV.UK base. Where the bulk of the page content will go |
| `footer` | block | Inherited from GOV.UK base. Includes the digital land footer |
| `bodyEnd` | block | Inherited from GOV.UK base. A block to insert any scripts for the page. We have broken this down into specific block. |
| `googleAnalytics` | block | Where we include our cookie and google analytics scripts |
| `includeJQuery` | variable | If set to `true` a version of jQuery will be included on the page |
| `bodyEndScripts` | block | Where we include `dl-frontend.js` |
