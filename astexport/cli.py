# -*- coding: utf-8 -*-

import fileinput
from astexport.parse import parse
from astexport.export import export_json


def main():
    """Read source from stdin, parse and export the AST as Json"""
    source = "".join(fileinput.input())
    tree = parse(source)
    json = export_json(tree)
    print(json)
