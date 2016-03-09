# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

description = "Python command line application to export Python AST as Json."

main_ns = {}
with open("astexport/version.py") as ver_file:
    exec(ver_file.read(), main_ns)

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_descr = f.read()

setup(
    name = "astexport",
    version = main_ns['__version__'],

    description = description,
    long_description = long_descr,
    license = "MIT",
    url = "https://github.com/fpoli/python-astexport",

    author = "Federico Poli",
    author_email = "federpoli@gmail.com",

    packages = find_packages(exclude=["tests"]),

    entry_points = {
        "console_scripts": [
            "astexport = astexport.cli:main"
        ]
    },

    install_requires = [
    ],
    extras_require = {
        "dev": [
            "twine",
            "nose == 1.3.3",
            "pep8 == 1.4.6"
        ]
    },

    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Disassemblers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5"
    ]
)
