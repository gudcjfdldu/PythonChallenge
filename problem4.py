#!/usr/bin/python
import urllib2
import re
p = re.compile('[0-9]+')
normal_pattern = re.compile('and the next nothing is [0-9]+')
full_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
flag = 1
full_url_index = re.search(p, full_url).start()

def get_parameter(full_url):
    response = urllib2.urlopen(full_url)
    the_page = response.read()
    parameter = ''.join(p.findall(the_page))
    return (parameter, the_page)



def repeat_request(full_url, flag):
    while flag:
        new_parameter, the_page = get_parameter(full_url)
        if ''.join(normal_pattern.findall(the_page)) == '':
            print the_page
        full_url = full_url[:full_url_index] + new_parameter

repeat_request(full_url, flag) 

