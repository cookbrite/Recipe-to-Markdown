# -*- coding: utf-8 -*-
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
title = soup.title.string.encode("ascii",'ignore').strip().split(" - ")[0]
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

print soup.find("div", {"class": "servings"}).find("span", {"id":"lblYield"}).string
print 

# <codecell>

def getTime(spanName):
    find = soup.find("div",{"id":"divRecipeTimesContainer"}).find("span", {"id": spanName})
    if find.__class__.__name__ != "NoneType":
      return " " + find.get_text().encode("ascii")
    return ""

print "* Prep Time  :" + getTime("prepHoursSpan") + getTime("prepMinsSpan")
print "* Cook Time  :" + getTime("cookHoursSpan") + getTime("cookMinsSpan")
print "* Total Time :" + getTime("totalHoursSpan") + getTime("totalMinsSpan")
print

# <codecell>

print "Ingredients:"
print

for s in soup.findAll("p", {"itemprop":"ingredients"}):
    print "*", s.get_text().encode("ascii").strip().replace("\n", " ")
print

# <codecell>

print "Directions:"
print

for i, s in enumerate(soup.findAll("span", {"class":"plaincharacterwrap"}),1):
    print str(i) + ".", s.get_text().encode("ascii").strip().replace("\n", " ")

