#!/usr/bin/env python3

import os
import jinja2

import codecs
import markdown
from markdown_jinja import MarkdownJinja

docs = "docs/"
static_path = "https://digital-land.github.io"  # use frontend assets we have published


def render(path, template, **kwargs):
    path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w") as f:
        f.write(template.render(staticPath=static_path, **kwargs))


# register templates
multi_loader = jinja2.ChoiceLoader(
    [
        jinja2.FileSystemLoader(searchpath="./templates"),
        jinja2.PrefixLoader(
            {
                "digital-land-frontend": jinja2.FileSystemLoader(
                    searchpath="./frontend/digital_land_frontend/templates"
                ),
                "govuk-jinja-components": jinja2.PackageLoader(
                    "govuk_jinja_components"
                ),
            }
        ),
    ]
)
env = jinja2.Environment(loader=multi_loader)

# get page template
index_template = env.get_template("index.html")
example_template = env.get_template("iframe-base.html")
component_template = env.get_template("component-page.html")

# init markdown
# give it access to the configured jinja.environment
# and any macros that might be used in the markdown files
md = markdown.Markdown(
    extensions=[
        MarkdownJinja(
            env=env,
            macros={
                "designSystemExample": "design-system/components/example/macro.html"
            },
        )
    ]
)


def markdown_compile(s):
    html = md.convert(s)
    html = html.replace("<p>", '<p class="govuk-body">')
    html = html.replace("<h1>", '<h1 class="govuk-heading-xl">')
    html = html.replace("<h2>", '<h2 class="govuk-heading-l">')
    html = html.replace("<h3>", '<h3 class="govuk-heading-m">')
    html = html.replace("<h4>", '<h4 class="govuk-heading-s">')
    return html


# get an example markdown file to render as a component page
_content = codecs.open(
    "frontend/digital_land_frontend/templates/components/page-feedback/README.md",
    mode="r",
)
_content_raw = _content.read()

# generate the pages
render("index.html", index_template)
render(
    "components/page-feedback/example.html",
    example_template,
    partial_name="digital-land-frontend/components/page-feedback/example.html",
)
render(
    "components/page-feedback/index.html",
    component_template,
    rendered_markdown=markdown_compile(_content_raw),
)

# generate data-item examples
_content = codecs.open(
    "frontend/digital_land_frontend/templates/components/data-item/README.md",
    mode="r",
)
_content_raw = _content.read()
render(
    "components/data-item/example.html",
    example_template,
    partial_name="digital-land-frontend/components/data-item/example.html",
)
render(
    "components/data-item/example-inline.html",
    example_template,
    partial_name="digital-land-frontend/components/data-item/example-inline.html",
)
render(
    "components/data-item/index.html",
    component_template,
    rendered_markdown=markdown_compile(_content_raw),
)
