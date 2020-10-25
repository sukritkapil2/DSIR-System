#!usr/bin/python3

# Importing required modules
import json
import os

# Initialization
authors_list = []
categories_list = []
docFiles = [f for f in os.listdir('./jsonnn') if f.endswith('.json')]

'''
Function for creating authors_list and categories_list and then storing in json file for further usage
'''
def create_author_category():
	for file in docFiles:
		with open(f'./jsonnn/{file}', encoding='utf8') as json_data:
			document = json.load(json_data)

		for word in document['authors']:
			authors_list.append(word)

		for ct in document['categories']:
			categories_list.append(ct)

	# Listing unique authors and categories
	a = list(set(authors_list))
	a.sort()
	# print('\n'.join(a))

	b = list(set(categories_list))
	b.sort()
	# print('\n'.join(b))

	# Creating folder if not exists
	if not os.path.exists('savers'):
		os.mkdir('savers')

	# Creating json
	with open('savers/authors_list.json', 'w', encoding='utf8') as fp:
		json.dump(a, fp, ensure_ascii=False)

	with open('savers/category.json', 'w', encoding='utf8') as fp:
		json.dump(b, fp, ensure_ascii=False)

# Calling the function
if __name__ == '__main__':
	create_author_category()