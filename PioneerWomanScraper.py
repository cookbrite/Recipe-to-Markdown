#!/usr/bin/env python
# encoding: utf-8
"""
AllRecipesComScraper.py

Created by Timothy Hopper on 2013-03-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from Scraper import RecipeScraper


class PioneerWoman(RecipeScraper):

    def title(self):

        title = self.find("h2", {"class": "recipe-title"})
        return title.find("span").string.encode("ascii", 'ignore').strip()

    def url(self):
        return self.url

    def num_servings(self):
        y = self.find("span", {"itemprop": "yield"})
        return y.string.encode("ascii", 'ignore').strip()

    def prep_time(self):
        return self.find("time", {"itemprop": "prepTime"}).string.encode("ascii", 'ignore').strip()

    def cook_time(self):
        return self.find("time", {"itemprop": "cookTime"}).string.encode("ascii", 'ignore').strip()

    def total_time(self):
        return ""

    def ingredients(self):
        ings = self.findAll("span", {"itemprop": 'ingredient'})
        for ing in ings:
            amt = ing.find("span", {"itemprop": "amount"}).string.encode(
                "ascii", 'ignore').strip()
            if amt == "":
                yield ing.find("span", {"itemprop": "name"}).string.encode("ascii", 'ignore').strip()
            else:
                yield ing.find("span", {"itemprop": "amount"}).string.encode("ascii", 'ignore').strip() \
                    + " " + ing.find("span", {"itemprop": "name"}).string.encode(
                        "ascii", 'ignore').strip()

    def directions(self):
        for s in self.find("div", {"itemprop": "instructions"}).findAll("p"):
            yield s.string.encode("ascii", 'ignore').strip()

    def note(self):
        return ""
