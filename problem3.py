#!/usr/bin/python

import re
import urllib2

p = re.compile('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}')


url_address = 'http://www.pythonchallenge.com/pc/def/equality.html'

url_ptr = urllib2.urlopen(url_address)
url_content = url_ptr.read()
check_index = url_content.find('kAewt')


check_string = url_content[check_index:]

answer = p.findall(check_string)

for token in answer:
    print token[4],

