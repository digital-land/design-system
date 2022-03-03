#!/usr/bin/env python3
import os
import jinja2
from bin.filters import is_current_page

from digital_land_frontend.filters import is_list_filter
from digital_land_frontend.globals import random_int


def get_jinja_template_raw(template_file_path):
    if template_file_path:
        if os.path.exists(template_file_path):
            file = open(template_file_path, "r")
            return file.read()
    return None


def setup_jinja():
    # register templates
    multi_loader = jinja2.ChoiceLoader(
        [
            jinja2.FileSystemLoader(searchpath="./templates"),
            jinja2.PrefixLoader(
                {
                    "govuk_frontend_jinja": jinja2.PackageLoader(
                        "govuk_frontend_jinja"
                    ),
                    "digital-land-frontend": jinja2.PackageLoader(
                        "digital_land_frontend"
                    ),
                    "examples": jinja2.FileSystemLoader(searchpath="./documentation"),
                }
            ),
        ]
    )
    env = jinja2.Environment(loader=multi_loader)

    # specific to design system
    env.filters["is_list"] = is_list_filter
    env.filters["raw_jinja"] = get_jinja_template_raw
    env.filters["is_current_page"] = is_current_page

    # set variables to make available to all templates
    env.globals["staticPath"] = "/static"
    env.globals["assetPath"] = "/static"  # used by digital-land-frontend
    env.globals["urlPath"] = "/design-system"
    env.globals["includesMap"] = False
    env.globals["random_int"] = random_int

    return env
