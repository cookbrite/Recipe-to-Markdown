#!/usr/bin/env python
# encoding: utf-8
"""
ScrapeRecipe.py

Created by Timothy Hopper on 2013-03-16.
"""

import sys
import getopt
import httplib
import urlparse
from site import *


def get_server_status_code(url):
    """
    Download just the header of a URL and
    return the server's status code.
    http://pythonadventures.wordpress.com/2010/10/17/check-if-url-exists/
    """
    # http://stackoverflow.com/questions/1140661
    host, path = urlparse.urlparse(url)[1:3]    # elems [1] and [2]
    try:
        conn = httplib.HTTPConnection(host)
        conn.request('HEAD', path)
        return conn.getresponse().status
    except StandardError:
        return None


def check_url(url):
    """
    Check if a URL exists without downloading the whole file.
    We only check the URL header.
    http://pythonadventures.wordpress.com/2010/10/17/check-if-url-exists/
    """
    # see also http://stackoverflow.com/questions/2924422
    good_codes = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
    return get_server_status_code(url) in good_codes


class Usage(Exception):

    def __init__(self, msg):
        self.msg = msg


def cmd_line_main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
        except getopt.error, msg:
            raise Usage(msg)

        # option processing
# for option, value in opts:
           #       if option == "-v":
           #           verbose = True
           #       if option in ("-h", "--help"):
           #           raise Usage(help_message)
           #       if option in ("-o", "--output"):
           #           output = value

    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2

    url = argv[1]
    save_recipe(url)


def save_recipe(url):

    if check_url(url) == False:
        print >> sys.stderr, "URL", url, "does not exist"
        return 2

    if "allrecipes.com" in url:
        scraper = AllRecipesCom(url)
        scraper.write(to_file=True)
    elif "thepioneerwoman.com" in url:
        scraper = PioneerWoman(url)
        scraper.write(to_file=True)
    if "food.com" in url:
        scraper = FoodCom(url)
        scraper.write(to_file=True)


if __name__ == "__main__":
    sys.exit(cmd_line_main())
