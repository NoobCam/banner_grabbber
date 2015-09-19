#!/usr/bin/env python2.7

import urllib2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=file, help="Input file")
args = parser.parse_args()
try:
    with args.filename as f:
        for line in f:
            response = urllib2.urlopen(line)
            print "The URL is: ", response.geturl()
            print "This gets the code: ", response.code
            print response.info()
            print "\n"
except:
    pass