#!/usr/bin/env python3

import os
import jinja2


docs = "docs/"
static_path = "https://digital-land.github.io" # use frontend assets we have published

def render(path, template, **kwargs):
    path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w") as f:
        f.write(template.render(staticPath=static_path, **kwargs))


# register templates
multi_loader = jinja2.ChoiceLoader([
    jinja2.FileSystemLoader(searchpath="./templates"),
    jinja2.PrefixLoader({
        'digital-land-frontend': jinja2.FileSystemLoader(searchpath='./frontend/digital_land_frontend/templates'),
        'govuk-jinja-components': jinja2.PackageLoader('govuk_jinja_components')
    })
])
env = jinja2.Environment(loader=multi_loader)

# get page template
test_template = env.get_template("index.html")

# generate the pages
render("index.html", test_template)