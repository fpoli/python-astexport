#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
import ast
from astexport.parse import parse
from test import TestIO


class TestParse(unittest.TestCase):

    def test_parse(self):
        for i, test in enumerate(self.tests):
            result = parse(test.input)
            expected = ast.fix_missing_locations(test.output)
            self.assertEqual(
                ast.dump(result, include_attributes=True),
                ast.dump(expected, include_attributes=True),
                "Test case {}".format(i)
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
                        value = ast.Num(
                            n = 5,
                            col_offset=4
                        )
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
