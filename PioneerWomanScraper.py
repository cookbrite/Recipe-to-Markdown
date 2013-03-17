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
        return self.soup.find("h2", {"class" : "recipe-title"}).find("span").string.encode("ascii",'ignore').strip()
    
    def url(self):
        return self.url

    def num_servings(self):
        return self.soup.find("span", {"itemprop":"yield"}).string.encode("ascii",'ignore').strip()
    
    def prep_time(self):
        return self.soup.find("time", {"itemprop":"prepTime"}).string.encode("ascii",'ignore').strip()
        
    def cook_time(self):
        return self.soup.find("time", {"itemprop":"cookTime"}).string.encode("ascii",'ignore').strip()
        
    def total_time(self):
        return ""
        
    def ingredients(self):
        ings = self.soup.findAll("span", {"itemprop":'ingredient'})
        for ing in ings:
            amt = ing.find("span", {"itemprop":"amount"}).string.encode("ascii",'ignore').strip()
            if amt == "":
                yield ing.find("span", {"itemprop":"name"}).string.encode("ascii",'ignore').strip()
            else:
                yield ing.find("span", {"itemprop":"amount"}).string.encode("ascii",'ignore').strip() \
                    + " " + ing.find("span", {"itemprop":"name"}).string.encode("ascii",'ignore').strip()
        
    def directions(self):
        for s in self.soup.find("div", {"itemprop":"instructions"}).findAll("p"):
            yield s.string.encode("ascii",'ignore').strip()
        
    def note(self):
        return ""