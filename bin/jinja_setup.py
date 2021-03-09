#!/usr/bin/env python3

import jinja2

from digital_land_frontend.filters import (
    group_id_to_name_filter,
    get_jinja_template_raw,
    organisation_id_to_name_filter,
    is_list,
    strip_slug,
    is_historical,
    contains_historical,
)

from bin.filters import is_current_page


def setup_jinja():
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
    env.filters["raw_jinja"] = get_jinja_template_raw
    env.filters["organisation_id_to_name"] = organisation_id_to_name_filter
    env.filters["is_list"] = is_list
    env.filters["group_id_to_name"] = group_id_to_name_filter
    env.filters["clean_slug"] = strip_slug
    env.filters["is_historical"] = is_historical
    env.filters["contains_historical"] = contains_historical
    env.filters["is_current_page"] = is_current_page

    # set variables to make available to all templates
    env.globals["staticPath"] = "https://digital-land.github.io"
    env.globals["urlPath"] = "/design-system"
    env.globals["includesMap"] = False

    return env
