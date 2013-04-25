#!/usr/bin/env python
# encoding: utf-8

from AbstractScraper import RecipeScraper


class FoodNetwork(RecipeScraper):

    def title(self):
        title = self.find("meta", {"property": "og:title"})
        return title["content"].encode("ascii", 'ignore').strip()

    def url(self):
        title = self.find("meta", {"property": "og:url"})
        return title["content"].encode("ascii", 'ignore').strip()

    def num_servings(self):
        return self.find("span", {"itemprop": "recipeYield"}).string.encode("ascii", 'ignore')

    def prep_time(self):
        duration = self.find("meta", {"itemprop": "prepTime"})["content"].encode("ascii", 'ignore')
        return self.parse_duration(duration)

    def cook_time(self):
        duration = self.find("meta", {"itemprop": "cookTime"})["content"].encode("ascii", 'ignore')
        return self.parse_duration(duration)

    def total_time(self):
        duration = self.find("meta", {"itemprop": "totalTime"})["content"].encode("ascii", 'ignore')
        return self.parse_duration(duration)

    def ingredients(self):
        #<li itemprop="ingredients">
        ings = self.findAll("li", {"itemprop": 'ingredients'})
        for ing in ings:
            yield ing.string.encode("ascii", "ignore").strip()

    def directions(self):
        #<div class="fn_instructions" itemprop="recipeInstructions">

        for s in self.find("div", {"class": "fn_instructions"}).findAll("p"):
            if s.string.strip() == "":
                continue
            yield s.string

    def note(self):
        return ""
