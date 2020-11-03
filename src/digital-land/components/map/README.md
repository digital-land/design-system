# Map component

Use this component when seeing something on a map would be useful for a user.

### Show a local authority boundary

We regularly need to show the extent of an area. The most common is the local authority boundary. This example shows the boundary for [Harrogate borough council](https://digital-land.github.io/organisation/local-authority-eng/HAG/).

{{ designSystemExample({
"iframe": {
    "title": "An example of the map component",
    "url": "example.html",
    "size": "m"
},
"component": {
    "name": "map"
}
}) }}

### Plot a conservation area

This example shows how to use `DLMaps.Map()` to plot a single conservation area extent on a map.

You can pass an array of urls that all point to geojson files. Any geojson that is fetched will be plotted.

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
