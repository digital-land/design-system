#!/usr/bin/env python3

import jinja2

from digital_land_frontend.filters import (
    get_jinja_template_raw,
    organisation_id_to_name_filter,
    is_list,
)


def setup_jinja():
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
                    "examples": jinja2.FileSystemLoader(searchpath="./documentation"),
                }
            ),
        ]
    )
    env = jinja2.Environment(loader=multi_loader)

    # register jinja filters
    env.filters["raw_jinja"] = get_jinja_template_raw
    env.filters["organisation_id_to_name"] = organisation_id_to_name_filter
    env.filters["is_list"] = is_list

    # set variables to make available to all templates
    env.globals["staticPath"] = "https://digital-land.github.io"
    env.globals["urlPath"] = "/design-system"
    env.globals["includesMap"] = False

    return env
