#!/usr/bin/env python
# encoding: utf-8

from AbstractScraper import RecipeScraper


class SimpleRecipes(RecipeScraper):

    def title(self):
        # meta property="og:title
        title = self.find("meta", {"property": "og:title"})
        return title.string.encode("ascii", 'ignore').strip()

    def url(self):
        url = self.find("meta", {"property": "og:url"})
        return url.string.encode("ascii", 'ignore').strip()

    def num_servings(self):
        return self.find("input", {"id": "original_value"})["value"].encode("ascii", 'ignore')

    def prep_time(self):
        # span class="preptime" itemprop="prepTime"
        duration = self.find("span", {"itemprop": "prepTime"})["content"].encode("ascii", 'ignore')
        return self.parse_duration(duration)

    def cook_time(self):
        duration = self.find("span", {"itemprop": "cookTime"})["content"].encode("ascii", 'ignore')
        return self.parse_duration(duration)

    def total_time(self):
        return ""

    def ingredients(self):
        # div id="recipe-ingredients
        ings = self.find("div", {"id": 'recipe-ingredients'}).findAll("li", {"class": "ingredient"})
        for ing in ings:
            yield int.string.encode("ascii", "ignore").strip()

    def directions(self):
        ings = self.find("div", {"id": 'recipe-method'}).findAll("p")
        for ing in ings:
            yield ing

    def note(self):
        return ""
