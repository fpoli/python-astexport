# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


from setuptools import setup


version = "0.1.0"

description = "Python command line application to export Python AST as Json."

with open("Readme.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "astexport",
    version = version,
    description = description,
    author = "Federico Poli",
    author_email = "federpoli@gmail.com",
    url = "https://github.com/fpoli/python-astexport",
    license = "GPLv3",
    packages = ["astexport"],
    entry_points = {
        "console_scripts": ["astexport = astexport.cli:main"]
    },
    long_description = long_descr,
    install_requires = [
        "meta",
    ]
)
