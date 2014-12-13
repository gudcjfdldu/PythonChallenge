#!/usr/bin/python

import urllib2
import re

url_address = "http://www.pythonchallenge.com/pc/def/ocr.html"

url_ptr = urllib2.urlopen(url_address)
url_content = url_ptr.read()

url_content_index = url_content.find('%%')
string = url_content[url_content_index:]

answer = ''.join(e for e in string if e.isalnum())

print answer


