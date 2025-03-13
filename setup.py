#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="meems",
    version="0.0.1",
    author="Isaac Overcast",
    author_email="iao2122@columbia.edu",
    license="GPLv3",
    description="A package to simulate georeferenced plant community data where plant",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": ["simpd = meems.__main__:main"]
    },
)
