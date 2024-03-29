#!/usr/bin/env python3

import codecs
import glob
import os
import sys
import json

import markdown
from frontmatter import Frontmatter

from bin.jinja_setup import setup_jinja
from bin.markdown_jinja import MarkdownJinja

docs = "docs/"


def path_to_url(p):
    if p.startswith("docs"):
        p = p[4:]
    if p.endswith("/index.html"):
        p = p[:-11]
    return p


def render(path, template, **kwargs):
    path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w") as f:
        f.write(template.render(path=path_to_url(path), **kwargs))


env = setup_jinja()

# get page templates
index_template = env.get_template("index.html")
get_started_template = env.get_template("getting-started.html")
example_template = env.get_template("iframe-base.html")
component_template = env.get_template("component-page.html")


# data for organisation autocomplete
def get_organisations():
    with open("templates/data/organisation.json") as json_file:
        data = json.load(json_file)
        return data["organisation"]


organisations = get_organisations()

# init markdown
# give it access to the configured jinja.environment
# and any macros that might be used in the markdown files
md = markdown.Markdown(
    extensions=[
        MarkdownJinja(
            env=env,
            macros={
                "designSystemExample": "design-system/components/example/macro.html",
                "govukTag": "govuk_frontend_jinja/components/tag/macro.html",
            },
        ),
        "fenced_code",
        "tables",
    ]
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
        rendered_markdown=md.convert(markdown_content),
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
        if "macro.html" not in file:
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


def reqs_org_data(documentation):
    if documentation["attributes"] is not None:
        return documentation["attributes"].get("requires_orgs")
    return None


def generate_component_documentation_pages(component_sets):
    for cset in component_sets:
        src_dir = f"documentation/{cset['type']}/components"
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
                    rendered_markdown=md.convert(documentation["body"]),
                    section=cset["dest"],
                )

                extras = {
                    "display_map": is_displaying_map(documentation),
                }
                if reqs_org_data is not None:
                    extras["organisation_data"] = organisations

                # render all examples for component
                render_example_pages(
                    component, src_dir, cset["dest"], jinja_input_path, **extras
                )
            else:
                print(f"No documentation for component: {component}")


def generate_template_documentation_pages(directory):

    for p in os.listdir(directory):
        output_root = directory.replace(
            "documentation/digital-land/templates", "template"
        )
        if os.path.isdir(os.path.join(directory, p)):
            generate_template_documentation_pages(os.path.join(directory, p))
        elif p.endswith(".md"):
            documentation = Frontmatter.read_file(f"{directory}/{p}")

            dest = (
                os.path.join(output_root, "index.html")
                if p == "index.md"
                else os.path.join(output_root, p.replace(".md", ""), "index.html")
            )

            # render the documentation page for the template
            render(
                dest,
                component_template,
                rendered_markdown=md.convert(documentation["body"]),
                section="template",
            )
        else:
            include_path = os.path.join(directory, p).replace(
                "documentation", "examples"
            )
            render(
                os.path.join(output_root, p),
                example_template,
                partial_name=include_path,
            )


def generate_design_system():
    # generate all component docs and examples
    component_sets = [
        {"type": "digital-land", "dest": "components"},
        {"type": "govuk", "dest": "govuk-components"},
    ]

    generate_component_documentation_pages(component_sets)
    generate_template_documentation_pages("documentation/digital-land/templates")

    # generate the index pages
    render("index.html", index_template)
    render("get-started/index.html", get_started_template)

    render_markdown_file(
        "documentation/guides/get-started.md",
        "get-started/index.html",
        get_started_template,
    )
    render_markdown_file(
        "documentation/govuk/components/README.md",
        "govuk-components/index.html",
        component_template,
        section="govuk-components",
    )
    render_markdown_file(
        "documentation/digital-land/components/README.md",
        "components/index.html",
        component_template,
        section="components",
    )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["assetPath"] = "/static"
        env.globals["staticPath"] = "/static"
        env.globals["urlPath"] = ""

    generate_design_system()
