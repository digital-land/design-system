---
contains_map: True
---
# Map component

Use this component when seeing something on a map would be useful for a user.

These examples show how to use `DLMaps.Map()` to create simple maps displaying area boundaries.

## Show a local authority boundary

We regularly need to show the extent of an area or areas. The most common is the local authority boundary.

This example shows the boundaries for [Harrogate borough council](https://digital-land.github.io/organisation/local-authority-eng/HAG/) and [City of York Council](https://digital-land.github.io/organisation/local-authority-eng/YOR/).

{{ designSystemExample({
"iframe": {
    "title": "An example of the map component with 2 local authority boundaries plotted.",
    "url": "example.html",
    "size": "m"
},
"component": {
    "name": "map"
}
}) }}

## Show multiple shapes

There are a number of ways to pass ursl to geojson files to the map component.

All urls must point to `.geojson` files.

### HTML attribute

You can pass a list of urls, separate by `;`, to the `data-geojson-urls` attribute of the map element.

    <div class="dl-map" id="aMap" 
        data-module="boundary-map"
        data-geojson-urls="/conservation-area/c52ff772-db94-4a8a-acdf-be3a1ac79d25/boundary.geojson;/local-authority-district/E06000001/geometry.geojson"
    >

{{ designSystemExample({
"iframe": {
    "title": "Example - pass urls as HTML attributes",
    "url": "example-html.html",
    "size": "l"
},
"component": {
    "name": "map"
}
}) }}

### Jinja macro option

Use the `data-geojson-urls` option when calling the jinja macro. It accepts a string with urls separated by `;` or it accepts an array urls.

{{ designSystemExample({
"iframe": {
    "title": "An example showing list of paths passed to the map component",
    "url": "example-multiple.html",
    "size": "l"
},
"component": {
    "name": "map"
}
}) }}

### JS init option

An alternative approach is to provide the url(s) to the `geojsonUrls` option which initalising the module.

{{ designSystemExample({
"iframe": {
    "title": "An example of the map component with multiple geometries passed to JS",
    "url": "example.html",
    "size": "m"
},
"component": {
    "name": "map"
}
}) }}


## Options

### Aria Labelledby

You can added a `aria-labelledby` attribute by adding text to the optional ` arialabelledby` option when using the component.

{{ designSystemExample({
"iframe": {
    "title": "A map showing a single conservation area",
    "url": "example-labelledby.html",
    "size": "m"
},
"component": {
    "name": "map"
}
}) }}

--------------

### Key

This is an experimental component.

An example of the key we use on the Brownfield land maps. Currently testing 2 options.

{{ designSystemExample({
"iframe": {
    "title": "A key used on the brownfield land maps",
    "url": "example-key.html",
    "size": "s"
},
"component": {
    "name": "map"
}
}) }}