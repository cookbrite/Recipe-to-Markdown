#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import urllib2
from bs4 import BeautifulSoup
import isodate


class RecipeScraper():

    def parse_duration(self, tstring):
        tdelta = isodate.parse_duration(tstring)
        d = {}
        fmt = []
        if tdelta.days == 1:
            fmt.append("{days} day")
            d["days"] = tdelta.days
        if tdelta.days > 1:
            fmt.append("{days} days")
            d["days"] = tdelta.days

        hours, rem = divmod(tdelta.seconds, 3600)
        if hours == 1:
            fmt.append("{hours} hour")
            d["hours"] = hours
        if hours > 1:
            fmt.append("{hours} hours")
            d["hours"] = hours

        minutes, _ = divmod(rem, 60)
        if minutes == 1:
            fmt.append("{minutes} minute")
            d["minutes"] = minutes
        if minutes > 1:
            fmt.append("{minutes} minutes")
            d["minutes"] = minutes

        fmt = ', '.join(fmt)
        return fmt.format(**d)

    def find(self, name, attrs):
        return self.soup.find(name, attrs)

    def findAll(self, name, attrs):
        return self.soup.findAll(name, attrs)

    def __init__(self, url):
        self.url = url
        # print url
        # self.url = url.split("?")[0]
        self.soup = BeautifulSoup(urllib2.urlopen(url).read())

    def title(self):
        raise NotImplementedError("Should have implemented this")

    def url(self):
        raise NotImplementedError("Should have implemented this")

    def num_servings(self):
        raise NotImplementedError("Should have implemented this")

    def prep_time(self):
        raise NotImplementedError("Should have implemented this")

    def cook_time(self):
        raise NotImplementedError("Should have implemented this")

    def total_time(self):
        raise NotImplementedError("Should have implemented this")

    def amt_unit_ingredient_tuple(self):
        raise NotImplementedError("Should have implemented this")

    def ingredients(self):
        try:
            for amt, unit, ingredient in self.unit_ingredient_tuple():
                yield amt + " " + unit + " " + ingredient
        except Exception:
            raise NotImplementedError("Should have implemented this")

    def directions(self):
        raise NotImplementedError("Should have implemented this")

    def note(self):
        raise NotImplementedError("Should have implemented this")

    def write(self, to_file=False, path="~/Dropbox/Text Notes/"):
        if to_file:
            path = os.path.expanduser(path)

            fileName = os.path.join(path, self.title() + ".txt")

            saveout = sys.stdout
            fsock = open(fileName, 'w')
            sys.stdout = fsock

        # Print recipe title
        print self.title()
        print

        print self.url
        print

        print "* Servings:", self.num_servings()

        if self.prep_time() != "":
            print "* Prep Time:", self.prep_time()
        if self.cook_time() != "":
            print "* Cook Time:", self.cook_time()
        if self.total_time() != "":
            print "* Total Time:", self.total_time()
        print

        print "Ingredients:"
        print

        for s in self.ingredients():
            print "*", s
        print

        print "Directions:"
        print

        for i, s in enumerate(self.directions(), 1):
            print str(i) + ".", s

        if to_file:
            sys.stdout = saveout
            fsock.close()
