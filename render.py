#!/usr/bin/env python3

import os
import sys
import glob
import jinja2

import codecs
import markdown

from bin.jinja_setup import setup_jinja
from bin.markdown_jinja import MarkdownJinja

from frontmatter import Frontmatter

docs = "docs/"


def render(path, template, **kwargs):
    path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w") as f:
        f.write(template.render(**kwargs))


env = setup_jinja()

# get page templates
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
        ),
        "fenced_code",
    ]
)


def markdown_compile(s):
    html = md.convert(s)
    html = html.replace("<p>", '<p class="govuk-body">')
    html = html.replace("<h1>", '<h1 class="govuk-heading-xl">')
    html = html.replace("<h2>", '<h2 class="govuk-heading-l">')
    html = html.replace("<h3>", '<h3 class="govuk-heading-m">')
    html = html.replace("<h4>", '<h4 class="govuk-heading-s">')
    html = html.replace("<ul>", '<ul class="govuk-list govuk-list--bullet">')
    html = html.replace("<pre>", '<pre class="hljs-container">')
    return html


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


def get_components(components_dir):
    components = []
    component_dirs = [d[0] for d in os.walk(components_dir)]
    for c in component_dirs:
        components.append(c.split("/")[-1])

    # don't need to include component dir
    if "components" in components:
        components.remove("components")
    return components


def render_example_pages(name, src_dir, dest, jinja_path, **kwargs):
    for file in glob.glob(f"{src_dir}/{name}/*.html"):
        # don't want to render pages for the macro files
        if not "macro.html" in file:
            example = os.path.basename(file)
            render(
                f"{dest}/{name}/{example}",
                example_template,
                partial_name=f"{jinja_path}/{name}/{example}",
                **kwargs,
            )


def is_displaying_map(documentation):
    if documentation["attributes"] is not None:
        return documentation["attributes"].get("contains_map")
    return None


def generate_documentation_pages(component_sets):
    for cset in component_sets:
        src_dir = f"src/{cset['type']}/components"
        components = get_components(src_dir)
        for component in components:
            jinja_input_path = f"examples/{cset['type']}/components"
            documentation_path = f"{src_dir}/{component}/README.md"
            if os.path.isfile(documentation_path):
                documentation = Frontmatter.read_file(documentation_path)

                # render the documentation page for the component
                render(
                    f"{cset['dest']}/{component}/index.html",
                    component_template,
                    rendered_markdown=markdown_compile(documentation["body"]),
                    section=cset["dest"],
                )

                # render all examples for component
                render_example_pages(
                    component,
                    src_dir,
                    cset["dest"],
                    jinja_input_path,
                    display_map=is_displaying_map(documentation),
                )
            else:
                print(f"No documentation for component: {component}")


def generate_design_system():
    # generate all component docs and examples
    component_sets = [
        {"type": "digital-land", "dest": "components"},
        {"type": "govuk", "dest": "govuk-components"},
    ]

    generate_documentation_pages(component_sets)

    # generate the index pages
    render("index.html", index_template)
    render("get-started/index.html", get_started_template)

    render_markdown_file(
        "src/guides/get-started.md", "get-started/index.html", get_started_template
    )
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


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["staticPath"] = "/static"

    generate_design_system()
