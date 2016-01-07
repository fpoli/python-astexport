import fileinput
import argparse
from astexport import __version__, __prog_name__
from astexport.parse import parse
from astexport.export import export_json


def create_parser():
    parser = argparse.ArgumentParser(
        prog=__prog_name__,
        description="Python source code in, JSON AST out. (v{})".format(
            __version__
        )
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
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="print version and exit"
    )
    return parser


def main():
    """Read source from stdin, parse and export the AST as JSON"""
    parser = create_parser()
    args = parser.parse_args()
    if args.version:
        print("{} version {}".format(__prog_name__, __version__))
        return
    source = "".join(fileinput.input(args.input))
    tree = parse(source)
    json = export_json(tree, args.pretty)
    print(json)
