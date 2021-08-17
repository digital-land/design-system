#!/usr/bin/env python3

import jinja2
from digital_land_frontend.filters import (
    get_jinja_template_raw,
    register_basic_filters,
    register_mapper_filters,
)

from bin.filters import is_current_page


def setup_jinja(specification):
    # register templates
    multi_loader = jinja2.ChoiceLoader(
        [
            jinja2.FileSystemLoader(searchpath="./templates"),
            jinja2.PrefixLoader(
                {
                    "digital-land-frontend": jinja2.PackageLoader(
                        "digital_land_frontend"
                    ),
                    "govuk-jinja-components": jinja2.PackageLoader(
                        "govuk_jinja_components"
                    ),
                    "examples": jinja2.FileSystemLoader(searchpath="./documentation"),
                }
            ),
        ]
    )
    env = jinja2.Environment(loader=multi_loader)

    # register jinja filters
    register_basic_filters(env, specification)
    register_mapper_filters(env, None, specification)

    # specific to design system
    env.filters["raw_jinja"] = get_jinja_template_raw
    env.filters["is_current_page"] = is_current_page

    # set variables to make available to all templates
    env.globals["staticPath"] = "https://digital-land.github.io"
    env.globals["urlPath"] = "/design-system"
    env.globals["includesMap"] = False

    return env
