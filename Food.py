# Need to update to match structure

<!-- # -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import subprocess
import urllib2
from bs4 import BeautifulSoup
import re, string, sys, os

# <codecell>

recipeDirection = os.path.expanduser("~/Dropbox/Text Notes/")

if (len(sys.argv) <= 1):
    print "Please include address as argument."
    exit()

# <codecell>

recipeUrl = sys.argv[1]
recipeUrl = recipeUrl.split("?")[0]
soup = BeautifulSoup(urllib2.urlopen(recipeUrl).read())
title = soup.title.string.encode("ascii",'ignore').strip().split(" - ")[-3]
fileName = recipeDirection + title + ".txt"

# <codecell>

saveout = sys.stdout
fsock = open(fileName, 'w')
sys.stdout = fsock

# <codecell>

# Print recipe title
print title
print 

# <codecell>

print recipeUrl
print 

# <codecell>

print soup.find("div", {"class": "rz-ss-e serviceSize"}).find("input", {"id":"original_value"})["value"] + " servings"
print 

# <codecell>

print "* Prep Time  : " + soup.find("div", {"class" : "ct-e"}).find("p", {"class":"preptime"}).find("meta")["content"][2:].replace("H", " hours ").replace("M", " minutes")
print "* Cook Time  : " + soup.find("div", {"class" : "ct-e"}).find("p", {"class":"cooktime"}).find("meta")["content"][2:].replace("H", " hours ").replace("M", " minutes")
print "* Total Time : " + soup.find("div", {"class" : "ct-e"}).find("h3", {"class":"duration"}).find("meta")["content"][2:].replace("H", " hours ").replace("M", " minutes")
print

# <codecell>

def getName(sp):
    if x.find("span",{"class":"name"}).find("a") != None:
        return x.find("span",{"class":"name"}).find("a").string.strip()
    else: 
        return x.find("span",{"class":"name"}).string.strip()
def getAmt(sp):
    if x.find("span",{"class":"amount"}).find("span", {"class":"value"}).string != None:
        return x.find("span",{"class":"amount"}).find("span", {"class":"value"}).string.strip()
    else: 
        return ''
def getUnit(sp):
    if x.find("span",{"class":"amount"}).find("span", {"class":"type"}).string != None:
        return x.find("span",{"class":"amount"}).find("span", {"class":"type"}).string.strip()
    else: 
        return ''

print "Ingredients:"
print

    
ingredients = [' '.join(
    [getAmt(x), 
    getUnit(x), 
    getName(x)]) for x in soup.findAll("li",{"class":"ingredient"})]
for s in ingredients:
    print "*", s
print

print "Directions:"
print

for x in soup.find("div", {"class" : "pod directions"}).findAll("div",{"class":"txt"}):
    print "* " + x.string -->