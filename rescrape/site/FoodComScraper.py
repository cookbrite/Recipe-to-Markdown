#!/usr/bin/env python
# encoding: utf-8

from AbstractScraper import RecipeScraper


class FoodCom(RecipeScraper):

    def title(self):
        title = self.find("h1", {"itemprop": "name"})
        return title.string.encode("ascii", 'ignore').strip()

    def url(self):
        return self.url

    def num_servings(self):
        return self.find("input", {"id": "original_value"})["value"].encode("ascii", 'ignore')

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
        ings = self.findAll("span", {"class": 'ingredient'})
        for ing in ings:
            dirs = map(lambda x: x.encode("ascii", "ignore").strip(), ing.findAll(text=True))
            dirs = [d for d in dirs if d != ""]
            dirs = ' '.join(dirs).strip()
            dirs = dirs.replace(" ,", ",")
            yield ' '.join(dirs.split())

    def directions(self):
        for s in self.find("span", {"class": "instructions"}).findAll("li"):
            yield s.find("div", {"class", "txt"}).string.encode("ascii", "ignore")

    def note(self):
        return ""
