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


def index_code_block(lines):
    if "```" in lines:
        opening_line = lines.index("```")
        closing_line = lines.index("```", opening_line + 1)
        return True, opening_line, closing_line
    return False, None, None


# extracts code blocks from lines of text
# also replaces code_blocks with a placeholder string
def extract_code_blocks(lines):
    code_blocks = []
    has_code_blocks = True
    while has_code_blocks:
        if "```" in lines:
            block, op, cl = index_code_block(lines)
            if block:
                code_blocks.append(lines[op : cl + 1])
                del lines[op + 1 : cl + 1]
                lines[op] = "{CODE BLOCK PLACEHOLDER}"
            else:
                has_code_blocks = False
        else:
            has_code_blocks = False
    return code_blocks


def insert_lines(lines, lines_to_insert, start_from):
    insert_pt = start_from
    for line in lines_to_insert:
        lines.insert(insert_pt, line)
        insert_pt = insert_pt + 1


def insert_code_blocks(lines, code_blocks, placeholder="{CODE BLOCK PLACEHOLDER}"):
    has_placeholders = True
    while has_placeholders:
        if placeholder in lines:
            idx = lines.index(placeholder)
            try:
                block = code_blocks.pop(0)
                insert_lines(lines, block, idx + 1)
                del lines[idx]
            except Exception:
                print("An exception occurred")
                lines[idx] = "{Error: Couldn't re-insert code-block}"
        else:
            has_placeholders = False
    return lines


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
        cbs = extract_code_blocks(lines)
        text = "\n".join(lines)
        template = self.environment.from_string(text)
        new_text = template.render(**self.context, **registered_macros)
        new_lines = new_text.split("\n")
        return insert_code_blocks(new_lines, cbs)


def makeExtension(*args, **kwargs):
    return MarkdownJinja(kwargs)
