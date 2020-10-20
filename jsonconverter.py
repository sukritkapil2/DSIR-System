#!/usr/bin/python3

# Importing required modules
import json
import os

with open('books.json', encoding='utf8') as json_data:
	document = json.load(json_data)

'''
Function for creating json files and then storing in jsonnn folder for further usage
'''
def jsonconverter():
	for i, index in enumerate(document):
		dic = {}
		j = i + 1

		# Extracting info
		dic['desc'] = index.get('shortDescription', '')
		dic['title'] = index.get('title', '')
		dic['thumbnailUrl'] = index.get('thumbnailUrl', '')
		dic['authors'] = [a for a in index.get('authors', '') if a != '' and 'A' <= a[0] <= 'Z']
		dic['categories'] = [a.title() for a in index.get('categories', '') if a != '']

		# Creating folder if not exists
		if not os.path.exists('jsonnn'):
			os.mkdir('jsonnn')

		# Creating json
		with open(f'jsonnn/{j}.json', 'w', encoding='utf8') as fp:
			json.dump(dic, fp, ensure_ascii=False)

# Calling the function
if __name__ == '__main__':
	jsonconverter()