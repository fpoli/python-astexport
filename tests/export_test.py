#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
import ast
import json
from astexport.export import export_json
from test import TestIO


class TestExportJson(unittest.TestCase):

    def test_export_json(self):
        for test in self.tests:
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
                u"ast_type": u"Module",
                u"body": [{
                    u"ast_type": u"Assign",
                    u"targets": [{
                        u"ast_type": u"Name",
                        u"ctx": {
                            u"ast_type": u"Store"
                        },
                        u"id": u"x"
                    }],
                    u"value": {
                        u"ast_type": u"Num",
                        u"n": {
                            u"ast_type": u"int",
                            u"n": 5
                        }
                    }
                }]
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
        )
    ]
