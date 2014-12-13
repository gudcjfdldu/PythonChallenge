#!/usr/bin/python

from PIL import Image

im = Image.open('oxygen.png', 'r').convert('RGB')
pix = im.load()
w = im.size[0]
h = im.size[1]
RGB_result_list = []

for i in range(w):
    for j in range(h):
        if pix[i,j][0] == pix[i,j][1] and pix[i,j][1] == pix[i,j][2]:
            RGB_result_list.append(((pix[i, j])))
            

for token in RGB_result_list:
    print chr(token[0]),
            
            
                   
