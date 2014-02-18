#!/usr/bin/env python
# encoding: utf-8

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Rescrape",
    version = "0.0.1",
    author = "Timothy Hopper",
    author_email = "tdhopper@gmail.com",
    description = "Scrape recipes from AllRecipes.com, etc to text/Markdown",
#   license = "BSD", # ???
    keywords = "recipe, scraper",
    url =  "https://github.com/tdhopper/Recipe-to-Markdown",
    packages=['rescrape'],
    long_description=read('README.md'),
    install_requires=[
        'beautifulsoup4',
        'isodate',
        ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
#       "License :: OSI Approved :: BSD License",
    ],
     entry_points={
         'console_scripts': [
             'rescrape = rescrape.ScrapeRecipe:cmd_line_main',
             ]
     }
)
