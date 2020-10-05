#!/usr/bin/env python3

import os
import glob
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


component_dir = "frontend/digital_land_frontend/templates/components"
dist_component_dir = "components"


def get_components():
    components = []
    component_dirs = [d[0] for d in os.walk(component_dir)]
    for c in component_dirs:
        components.append(c.split("/")[-1])

    # don't need to include component dir
    if "components" in components:
        components.remove("components")
    return components


def render_example_pages(components):
    for c in components:
        for file in glob.glob(f"{component_dir}/{c}/*.html"):
            # don't want to render pages for the macro files
            if not "macro.html" in file:
                n = os.path.basename(file)
                render(
                    f"{dist_component_dir}/{c}/{n}",
                    example_template,
                    partial_name=f"digital-land-frontend/components/{c}/{n}",
                )


def read_markdown_file(p):
    _content = codecs.open(
        p,
        mode="r",
    )
    return _content.read()


def render_component_doc_pages(components):
    for c in components:
        documentation_path = f"{component_dir}/{c}/README.md"
        if os.path.isfile(documentation_path):
            markdown_content = read_markdown_file(documentation_path)
            render(
                f"components/{c}/index.html",
                component_template,
                rendered_markdown=markdown_compile(markdown_content),
            )
        else:
            print(f"No documentation for {c}")


components = get_components()
render_example_pages(components)
render_component_doc_pages(components)

# get an example markdown file to render as a component page
_content = codecs.open(
    "frontend/digital_land_frontend/templates/components/page-feedback/README.md",
    mode="r",
)
_content_raw = _content.read()

# generate the pages
render("index.html", index_template)
