#!/usr/bin/env python3

import os
import glob
import jinja2

import codecs
import markdown
from markdown_jinja import MarkdownJinja
from frontend.digital_land_frontend.filters import get_jinja_template_raw

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
                "examples": jinja2.FileSystemLoader(searchpath="./src"),
            }
        ),
    ]
)
env = jinja2.Environment(loader=multi_loader)
# register jinja filters
env.filters["raw_jinja"] = get_jinja_template_raw

# set variables to make available to all templates
env.globals["static_path"] = "http://digital-land.github.io"

# get page template
index_template = env.get_template("index.html")
get_started_template = env.get_template("getting-started.html")
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


component_dir = "src/digital-land/components"
dist_component_dir = "components"


def get_components(components_dir):
    components = []
    component_dirs = [d[0] for d in os.walk(components_dir)]
    for c in component_dirs:
        components.append(c.split("/")[-1])

    # don't need to include component dir
    if "components" in components:
        components.remove("components")
    return components


def render_example_pages(components, dir_, dest, jinja_path):
    for c in components:
        for file in glob.glob(f"{dir_}/{c}/*.html"):
            # don't want to render pages for the macro files
            if not "macro.html" in file:
                n = os.path.basename(file)
                render(
                    f"{dest}/{c}/{n}",
                    example_template,
                    partial_name=f"{jinja_path}/{c}/{n}",
                )


def read_markdown_file(p):
    _content = codecs.open(
        p,
        mode="r",
    )
    return _content.read()


def render_markdown_file(file_, dest_file, template, **kwargs):
    markdown_content = read_markdown_file(file_)
    render(
        dest_file,
        template,
        rendered_markdown=markdown_compile(markdown_content),
        **kwargs,
    )


def render_component_doc_pages(components, dir_, dest, **kwargs):
    for c in components:
        documentation_path = f"{dir_}/{c}/README.md"
        if os.path.isfile(documentation_path):
            markdown_content = read_markdown_file(documentation_path)
            render(
                f"{dest}/{c}/index.html",
                component_template,
                rendered_markdown=markdown_compile(markdown_content),
                **kwargs,
            )
        else:
            print(f"No documentation for {c}")


components = get_components(component_dir)
render_example_pages(
    components,
    "src/digital-land/components",
    "components",
    "examples/digital-land/components",
)
render_component_doc_pages(
    components,
    "src/digital-land/components",
    "components",
    section="components",
)

govuk_components = get_components("src/govuk/components")
render_example_pages(
    govuk_components,
    "src/govuk/components",
    "govuk-components",
    "examples/govuk/components",
)
render_component_doc_pages(
    govuk_components,
    "src/govuk/components",
    "govuk-components",
    section="govuk-components",
)

# generate the pages
render("index.html", index_template)
render("get-started/index.html", get_started_template)
render_markdown_file(
    "src/govuk/components/README.md",
    "govuk-components/index.html",
    component_template,
    section="govuk-components",
)
render_markdown_file(
    "src/digital-land/components/README.md",
    "components/index.html",
    component_template,
    section="components",
)
