#!/usr/bin/python3

# Importing required modules
import json
import os
from math import log2

from nltk import FreqDist

# Initialization
with open('./savers/document_tokens_list.json', encoding='utf8') as json_data:
    document_tokens_list = json.load(json_data)

with open('savers/vocabulary.json', encoding='utf8') as json_data:
    vocabulary = json.load(json_data)

vocabulary_idf = {}			# Storing number of documents in which a word is appearing
freqDist = []				# For storing frequency of each word in a document

'''
function for building the FreqDistribution
'''


def buildFreqDist():
    for document_tokens in document_tokens_list:
        freqDist.append(FreqDist(document_tokens))


'''
function for building the IDF
'''


def buildIDF():
    for word in vocabulary:
        for document_tokens in document_tokens_list:
            if word in document_tokens:
                vocabulary_idf[word] = vocabulary_idf.get(word, 0) + 1


'''
Function to return the term frequency
'''


def returnTermFrequency(term, document_tokens, document_tokens_index):
    fd = freqDist[document_tokens_index][term] / float(len(document_tokens))
    return log2(1 + fd)


'''
Function to return corresponding idf searching in the vocabulary
'''


def returnIdf(term):
    return log2(len(document_tokens_list) / vocabulary_idf[term])


'''
Funnction for computing the primary dictionary necessary for tf-idf calculations
The structure is as follows:
It has nested dictionaries
DICTIONARY1-word in vocabulary:
<<<<<<< HEAD
                DICTIONARY2-document_number:
                    DICTIONARY3- TF,IDF,TF-IDF
"""

with open('./savers/document_tokens_list.json') as json_data:
    document_tokens_list = json.load(json_data)


with open('savers/vocabulary.json') as json_data:
    vocabulary = json.load(json_data)

# print("yo")
buildFreqDist(document_tokens_list)

buildIDF()

primaryDictionary=dict()

j=0
for vocab in vocabulary:
    j+=1
    #print(j) #for keeping count of how many words of the vocabulary are done
    if vocab not in primaryDictionary:
        inner_dict=dict()
        k=0
        for document_tokens in document_tokens_list:
            inner_dict[k]=dict()
            termFreq = returnTermFrequency(vocab, document_tokens, k)
            idf = returnIdf(vocab)
            inner_dict[k] = {1:termFreq,2:idf,3:(termFreq*idf)}
            k = k + 1
            #inner_dict[i]=(tf_idf_rapport(vocab,document_tokens_list[i],document_tokens_list))
    primaryDictionary[vocab]=inner_dict
#IDF by searching in the vocabulary
#print (primaryDictionary)
#print (len(vocabulary))


#storing the created prime dictionary in a json file.
with open('savers/primeDictionary.json', 'w') as fp:
    json.dump(primaryDictionary, fp)
=======
	DICTIONARY2-document_number:
		DICTIONARY3- TF,IDF,TF-IDF
'''


def create_megadict():
    buildFreqDist()
    buildIDF()
    primaryDictionary = {}

    for vocab in vocabulary:
        if vocab not in primaryDictionary:
            inner_dict = {}
            for k, document_tokens in enumerate(document_tokens_list):
                inner_dict[k] = {}
                tf = returnTermFrequency(vocab, document_tokens, k)
                idf = returnIdf(vocab)
                inner_dict[k] = {1: tf, 2: idf, 3: (tf * idf)}

            primaryDictionary[vocab] = inner_dict

    # Creating json
    with open('savers/primeDictionary.json', 'w', encoding='utf8') as fp:
        json.dump(primaryDictionary, fp, ensure_ascii=False)


# Calling the function
if __name__ == '__main__':
    create_megadict()
