# Digital design system

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/digital-land/brownfield-land/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)

This repository builds the [design system](https://digital-land.github.io/design-system/) pages on the [digital land site](https://digital-land.github.io).

## Updating the site

We recommend working in [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) before installing the python dependencies. Then run:

    make init
    make render

This will rebuild all the pages, putting them in the `/docs` directory.

Commit changes to this directory.

## Contributing

All documentation and examples are kept in the `/src` directory.

### New examples

To add a new example, create a `.html` file in the component directory you are providing the example for. E.g. `src/digital-land/buttons/example.html`.

### Updating documentation

To update the documentation edit any of the markdown files found in `/src`. E.g. `src/digital-land/components/info-text/README.md`.

If you want to include an example add the following to your markdown:

    {{ designSystemExample({
    "iframe": {
        "title": "An example of the feedback panel component",
        "url": "example.html",
        "size": "s"
    },
    "component": {
        "name": "feedback-panel"
    }
    }) }}

Where `url` is the name of the example file, `name` is the name of the component directory and `size` is one of **xs**, **s**, **m** or **l** depending on the amount of size you want it to take up.

Remember to add the new component/documentation page to the [component menu](templates/design-system/menus/components.html).

### Documenting a new component

If a new component has been added digital land [frontend](https://digital-land.github.io/frontend/) you can add documentation for it by creating a directory for it in `src/digital-land` and then creating at least 1 example and a README.md file.

A new component should have a directory such as:

    src/digital-land/new-component
        - example.html
        - example2.html
        - README.md
