# -*- coding: UTF-8 -*-

import unittest
import ast
import json
from astexport.export import export_json
from test import TestIO


class TestExportJson(unittest.TestCase):
    maxDiff = None

    def test_export_json(self):
        for i, test in enumerate(self.tests):
            with self.subTest(test=i):
                result = json.loads(export_json(test.input))
                expected = test.output
                self.assertEqual(result, expected)

    tests = [
        TestIO(
            input = ast.Module(
                body = [
                    ast.Assign(
                        targets = [
                            ast.Name(
                                ctx = ast.Store(),
                                id = "x"
                            )
                        ],
                        value = ast.Num(n = 5)
                    )
                ]
            ),
            output = {
                "ast_type": "Module",
                "body": [
                    {
                        "ast_type": "Assign",
                        "col_offset": None,
                        "lineno": None,
                        "targets": [
                            {
                                "ast_type": "Name",
                                "col_offset": None,
                                "ctx": {
                                    "ast_type": "Store"
                                },
                                "id": "x",
                                "lineno": None
                            }
                        ],
                        "value": {
                            "ast_type": "Num",
                            "col_offset": None,
                            "lineno": None,
                            "n": {
                                "ast_type": "int",
                                "n": 5,
                                "n_str": "5"
                            }
                        }
                    }
                ]
            }
        ),
        TestIO(
            input = ast.Module(
                body = [
                    ast.Expr(
                        col_offset = 0,
                        lineno = 1,
                        value = ast.Call(
                            col_offset = 0,
                            lineno = 1,
                            func = ast.Name(
                                col_offset = 0,
                                lineno = 1,
                                id = "foobar",
                                ctx = ast.Load()
                            ),
                            args = [],
                            keywords = [],
                            starargs = None,
                            kwargs = None
                        )
                    )
                ]
            ),
            output = {
                "ast_type": "Module",
                "body": [
                    {
                        "ast_type": "Expr",
                        "col_offset": 0,
                        "lineno": 1,
                        "value": {
                            "args": [],
                            "ast_type": "Call",
                            "col_offset": 0,
                            "func": {
                                "ast_type": "Name",
                                "col_offset": 0,
                                "ctx": {
                                    "ast_type": "Load"
                                },
                                "id": "foobar",
                                "lineno": 1
                            },
                            "keywords": [],
                            "lineno": 1
                        }
                    }
                ]
            }
        ),
        TestIO(
            input = ast.NameConstant(None),
            output = {
                "ast_type": "NameConstant",
                "col_offset": None,
                "lineno": None,
                "value": "None"
            }
        ),
        TestIO(
            input = ast.NameConstant(True),
            output = {
                "ast_type": "NameConstant",
                "col_offset": None,
                "lineno": None,
                "value": "True"
            }
        ),
        TestIO(
            input = ast.NameConstant(False),
            output = {
                "ast_type": "NameConstant",
                "col_offset": None,
                "lineno": None,
                "value": "False"
            }
        ),
        TestIO(
            input = ast.Module(
                body = [
                    ast.Global(
                        names = ["x"],
                        lineno = 1,
                        col_offset = 0
                    )
                ]
            ),
            output = {
                "body": [
                    {
                        "lineno": 1,
                        "col_offset": 0,
                        "ast_type": "Global",
                        "names": ["x"]
                    }
                ],
                "ast_type": "Module"
            }
        ),
        TestIO(
            input = ast.FunctionDef(
                name = "function",
                args = ast.arguments(
                    args = [],
                    vararg = None,
                    kwonlyargs = [
                        ast.arg(
                            arg = "x",
                            annotation = None,
                            lineno = 1,
                            col_offset = 16
                        )
                    ],
                    kw_defaults = [None],
                    kwarg = None,
                    defaults = []
                ),
                body = [
                    ast.Pass(lineno = 1, col_offset = 20)
                ],
                decorator_list = [],
                returns = None,
                lineno = 1,
                col_offset = 0
            ),
            output = {
                "args": {
                    "args": [],
                    "ast_type": "arguments",
                    "defaults": [],
                    "kw_defaults": [None],
                    "kwarg": None,
                    "kwonlyargs": [
                        {
                            "annotation": None,
                            "arg": "x",
                            "ast_type": "arg",
                            "col_offset": 16,
                            "lineno": 1
                        }
                    ],
                    "vararg": None
                },
                "ast_type": "FunctionDef",
                "body": [
                    {
                        "ast_type": "Pass",
                        "col_offset": 20,
                        "lineno": 1
                    }
                ],
                "col_offset": 0,
                "decorator_list": [],
                "lineno": 1,
                "name": "function",
                "returns": None
            }
        ),
    ]
