#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from collections import namedtuple

TestIO = namedtuple("Test", "input output")


def generateTests(cls):
    build_test = getattr(cls, "build_test")
    for i, data in enumerate(cls.tests):
        def test(self):
            build_test(self, data)
        test.__name__ = "test_{0}".format(i)
        setattr(cls, test.__name__, test)
    delattr(cls, "build_test")
    delattr(cls, "tests")
    return cls
