#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
import ast
from meta.asttools import cmp_ast, str_ast
from astexport.parse import parse
from test import TestIO


class TestParse(unittest.TestCase):

    def test_parse(self):
        for test in self.tests:
            result = parse(test.input)
            expected = ast.fix_missing_locations(test.output)
            self.assertTrue(
                cmp_ast(result, expected),
                "Result:\n{}\nExpected:\n{}".format(
                    str_ast(result),
                    str_ast(expected)
                )
            )

    tests = [
        TestIO(
            input = "x = 5",
            output = ast.Module(
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
            )
        ),
        TestIO(
            input = "foobar()",
            output = ast.Module(
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
            )
        )
    ]
