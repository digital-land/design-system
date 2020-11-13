---
contains_map: True
---
# Map component

Use this component when seeing something on a map would be useful for a user.

These examples show how to use `DLMaps.Map()` to create simple maps displaying area boundaries.

### Show a local authority boundary

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

Use the `geojsonUrls` option to plot mulitple boundaries, it accepts an array of geojson urls.

### Plot a conservation area



An alternative approach is to provide the url to the geojson in the `data-geojson-urls` attribute.

{{ designSystemExample({
"iframe": {
    "title": "An example of the map component with a single conservation area",
    "url": "example-conservation-area.html",
    "size": "m"
},
"component": {
    "name": "map"
}
}) }}

To provide mulitple separate the urls with a `;`. E.g.

    "https://digital-land.github.io/geography/boundary1.geojson;https://digital-land.github.io/geography/boundary2.geojson"

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