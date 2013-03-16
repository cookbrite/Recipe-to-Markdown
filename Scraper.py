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
        print "AAAA"
        raise NotImplementedError( "Should have implemented this" )
    
    def url(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def numServings(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def prepTime(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def cookTime(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def totalTime(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def ingredients(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def directions(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def note(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def writeToFile(self, path = "~/Dropbox/Text Notes/"):

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

        print "Servings: ", self.numServings()
        print 

        print "* Prep Time  :", self.prepTime()
        print "* Cook Time  :", self.cookTime()
        print "* Total Time :", self.totalTime()
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
        