#!/usr/bin/env python
# encoding: utf-8

import os, sys, urllib2
from bs4 import BeautifulSoup

class RecipeScraper():
    
    def __init__(self, url):
        self.url = url
        # print url
        # self.url = url.split("?")[0]
        self.soup = BeautifulSoup(urllib2.urlopen(url).read())
    
    def title(self):
        raise NotImplementedError( "Should have implemented this" )
    
    def url(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def num_servings(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def prep_time(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def cook_time(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def total_time(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def ingredients(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def directions(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def note(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def write_to_file(self, path = "~/Dropbox/Text Notes/"):

        path = os.path.expanduser(path)

        fileName = path + self.title() + ".txt"

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

        for i, s in enumerate(self.directions(),1):
            print str(i) + ".", s

        sys.stdout = saveout
        fsock.close()
