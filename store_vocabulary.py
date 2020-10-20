#!/usr/bin/python3

# Importing required modules
import json
import os

from nltk.stem.snowball import SnowballStemmer

# Initialization
vocabulary = {}

'''
Function for building the vocabulary i.e. the dictionary which has all the unique words in the corpus
'''
def build_vocabulary(document_tokens):
	
	vocabulary_index = len(vocabulary)
	# Accsessing words in document tokens list
	for word in document_tokens:
		if word not in vocabulary:
			vocabulary[word] = vocabulary_index
			vocabulary_index += 1

'''
Function for retreiving the document_tokens_list for creating the vocabulary,then storing the vocabulary in a json file
'''
def compute_vocabulary():
	with open('./savers/document_tokens_list.json', encoding='utf8') as json_data:
		document_tokens_list = json.load(json_data)

	for document_tokens in document_tokens_list:
		build_vocabulary(document_tokens)

	with open('savers/vocabulary.json', 'w', encoding='utf8') as fp:
		json.dump(vocabulary, fp, ensure_ascii=False)

# Calling the function
if __name__ == '__main__':
	compute_vocabulary()