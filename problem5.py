#!/usr/bin/python
import pickle
file_name = open('banner.p', 'rb')
content = pickle.load(file_name)
charlist = []
numberlist = []
for token in content:
	print ''
	for i in range(len(token)):
		
		for string in range(token[i][1]):
			print token[i][0],
	


