import ast


def parse(source):
    if not isinstance(source, str):
        raise ValueError(
            "The argument of parse(..) must be of type string, not '{}'".format(
                type(source)
            )
        )
    tree = ast.parse(source)
    return tree
