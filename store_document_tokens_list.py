#!usr/bin/python3

# Importing required modules
import json
import os

import nltk
from nltk.stem.snowball import SnowballStemmer

# Initialization
nltk.download('punkt')
nltk.download('stopwords')
snowball_stemmer = SnowballStemmer('english')
document_tokens_list = []

# Listing all files in jsonnn folder
docFiles = sorted([int(f.split('.')[0]) for f in os.listdir('./jsonnn') if f.endswith('.json')])

'''
Function for creating document_tokens_list and then storing in json file for further usage
'''
def create_document_tokens_list():
	for file in docFiles:
		document = {}
		with open(f'./jsonnn/{file}.json', encoding='utf8') as json_data:
			document = json.load(json_data)

		# Creating relevant words list
		words = str(document['title'])
		for author in document['authors']:
			words += ' ' + str(author)

		for category in document['categories']:
			words += ' ' + str(category)

		for des in document['desc']:
			words += str(des)

		# Processing relevant words
		temp_doc_tokens = nltk.word_tokenize(words)
		temp_doc_tokens = [w.lower() for w in temp_doc_tokens]
		temp_doc_tokens = [snowball_stemmer.stem(token) for token in temp_doc_tokens]
		temp_doc_tokens = [token for token in temp_doc_tokens if token not in nltk.corpus.stopwords.words('english')]

		document_tokens_list.append(temp_doc_tokens)

	# Creating json
	with open('savers/document_tokens_list.json', 'w', encoding='utf8') as fp:
		json.dump(document_tokens_list, fp, ensure_ascii=False)

# Calling the function
if __name__ == '__main__':
	create_document_tokens_list()
