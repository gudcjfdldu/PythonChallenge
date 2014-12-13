#!/usr/bin/python
import os
import zipfile
import re

filename_list = []
file_content_list = []
def get_filename_list(filename_list, file_content_list):
    for root, dirs, files in os.walk('/home/cada/channel'):
        for f in files:
            filename_list.append(f)
            file_open = open(f, 'r')
            file_content = file_open.read()
            file_content_list.append(file_content)
            
    for x, y in zip(filename_list, file_content_list):
        print x, y


total_list = []
filename_list = []
comment_list = []
file_name_list = []
start_file_name = '90052.txt'
p = re.compile('[0-9]+')

def print_info(comment_list, filename_list, total_list, file_name_list):
    zf = zipfile.ZipFile('channel.zip')
    
    for info in zf.infolist():
        filename_list.append(info.filename)
        comment_list.append(info.comment)
        
        
    for filename, comment in zip(filename_list, comment_list):
        
        f = open('/home/cada/channel/' + filename)
        content = f.read()
        new_string = p.findall(content)
        new_string = ''.join(new_string)
        new_string = new_string + '.txt' 
        total_list.append((filename, comment, new_string))



print_info(comment_list, filename_list, total_list, file_name_list)



object_file_name = '90052.txt'

def find_answer(object_file_name):
    while True:
        for token in total_list:
            if token[0] == object_file_name:
                print token[1],
                object_file_name = token[2]
                break


find_answer(object_file_name)



    



