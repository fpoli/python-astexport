# -*- coding: utf-8 -*-

import fileinput
import argparse
from .parse import parse
from .export import export_json


def create_parser():
    parser = argparse.ArgumentParser(
        prog="astexport",
        description="Python source code in, JSON AST out."
    )
    parser.add_argument(
        "-i", "--input",
        default="-",
        help="file to read from or '-' to use standard input (default)"
    )
    parser.add_argument(
        "-p", "--pretty",
        action="store_true",
        help="print indented JSON"
    )
    return parser


def main():
    """Read source from stdin, parse and export the AST as JSON"""
    parser = create_parser()
    args = parser.parse_args()
    source = "".join(fileinput.input(args.input))
    tree = parse(source)
    json = export_json(tree, args.pretty)
    print(json)
