#!/usr/bin/env python
# encoding: utf-8
"""
AllRecipesComScraper.py

Created by Timothy Hopper on 2013-03-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from Scraper import RecipeScraper

class AllRecipesCom(RecipeScraper):
    
    def title(self):
        return self.soup.title.string.encode("ascii",'ignore').strip().split(" - ")[0]
    
    def url(self):
        return self.url

    def numServings(self):
        return self.soup.find("div", {"class": "servings"}).find("span", {"id":"lblYield"}).string.split(" ")[0]
    
    def prepTime(self):
        return self.getTime("prepHoursSpan") + self.getTime("prepMinsSpan")
        
    def cookTime(self):
        return self.getTime("cookHoursSpan") + self.getTime("cookMinsSpan")
        
    def totalTime(self):
        return self.getTime("totalHoursSpan") + self.getTime("totalMinsSpan")
        
    def ingredients(self):
        for s in self.soup.findAll("p", {"itemprop":"ingredients"}):
            yield s.get_text().encode("ascii").strip().replace("\n", " ")
        
    def directions(self):
        for s in self.soup.findAll("span", {"class":"plaincharacterwrap"}):
            yield s.get_text().encode("ascii").strip().replace("\n", " ")
        
    def note(self):
        return ""
    
    def getTime(self, spanName):
        find = self.soup.find("div",{"id":"divRecipeTimesContainer"}).find("span", {"id": spanName})
        if find.__class__.__name__ != "NoneType":
          return " " + find.get_text().encode("ascii")
        return ""