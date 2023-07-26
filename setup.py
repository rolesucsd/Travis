#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2023--, Travis development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Travis",
    version="0.1.0",
    author="Renee Oles",
    author_email="roles@health.ucsd.edu",
    description="A package for finding paths in a graph",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rolesucsd/travis",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 3 - Alpha"],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'travis = travis.__main__:main'
        ]
    }
)
