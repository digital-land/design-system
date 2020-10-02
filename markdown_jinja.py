#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from jinja2 import Environment


class MarkdownJinja(Extension):
    def __init__(self, configs={}, env=None, macros={}):
        self.env = env
        self.macros = macros
        self.config = {
            "context_file": [
                "",
                "Default location of JSON file containing template context",
            ]
        }
        for key, value in configs.items():
            self.setConfig(key, value)

    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add(
            "jinja",
            JinjaPreprocessor(md, self.getConfigs(), self.env, self.macros),
            "_begin",
        )


class JinjaPreprocessor(Preprocessor):
    def __init__(self, md, config, env, macros):
        super(JinjaPreprocessor, self).__init__(md)
        self.environment = env if env is not None else Environment()
        self.context = (
            json.load(open(config["context_file"])) if config["context_file"] else {}
        )
        self.macros = macros

    def register_macros(self):
        macros = {}
        for k, v in self.macros.items():
            macros[k] = self.register_macro(v, k)
        return macros

    def register_macro(self, template_name, attribute):
        return getattr(self.environment.get_template(template_name).module, attribute)

    def run(self, lines):
        registered_macros = self.register_macros()
        text = "\n".join(lines)
        template = self.environment.from_string(text)
        new_text = template.render(**self.context, **registered_macros)
        return new_text.split("\n")


def makeExtension(*args, **kwargs):
    return MarkdownJinja(kwargs)
