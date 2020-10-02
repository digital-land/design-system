Jinja macro for the example component.

It uses an iframe to show the example. There is also the option to show the code needed to produce the example.

## Options

* id - (optional) an id prefix

* iframe - single object
    * url - url to the example page
    * size - (optional) size of the panel, defaults to m
    * title - title, describing what the iframe will show

* partial - list
    * type - the type of the code, usually 'html' or 'jinja'
    * name / path - refers to the partial used to produce the example. The component with display the raw text from the partial file