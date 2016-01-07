# -*- coding: UTF-8 -*-

import ast
import json


def export_json(tree, pretty_print=False):
    assert(isinstance(tree, ast.AST))
    return json.dumps(
        export_dict(tree),
        indent=4 if pretty_print else None,
        sort_keys=True,
        separators=(",", ": ") if pretty_print else (",", ":")
    )


def export_dict(tree):
    assert(isinstance(tree, ast.AST))
    class_name = tree.__class__.__name__
    args = {
        "ast_type": class_name
    }

    for name in tree.__dict__:
        # Check conflicts (we use ast_type to store class_name)
        if name == "ast_type":
            raise Exception(
                ("Unexpected attribute '{name}' in class {class_name}").format(
                    name = name,
                    class_name = class_name
                )
            )
        val = getattr(tree, name)
        if isinstance(val, ast.AST):
            args[name] = export_dict(val)
        elif val is True or val is False or val is None:
            args[name] = str(val)
        elif isinstance(val, str):
            args[name] = val
        elif isinstance(val, int) and name in ("lineno", "col_offset"):
            args[name] = val
        elif isinstance(val, int):
            args[name] = {"ast_type": "int", "n": val}
        elif isinstance(val, float):
            args[name] = {"ast_type": "float", "n": val}
        elif isinstance(val, complex):
            args[name] = {"ast_type": "complex", "n": val.real, "i": val.imag}
        elif isinstance(val, list) or isinstance(val, tuple):
            args[name] = [export_dict(x) for x in val]
        else:
            raise Exception(
                ("Attribute '{name}' of class {class_name} "
                 "not recognized, type is: {type}, value is: {value}").format(
                    name = name,
                    class_name = class_name,
                    type = type(val).__name__,
                    value = val
                )
            )

    return args
