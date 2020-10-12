#importing the required libraries from Python
from math import log
import nltk
from nltk import word_tokenize
from nltk import FreqDist
import sys
import math
import os
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import pickle
import  json

#initialising the list and dictionary to store posting lists and Vocabulary
vocabulary = {}
vocabulary_idf = {}         #storing number of documents in which a word is appearing
freqDist = {}               #for storing frequency of each word in a document
document_tokens_list= []
temp_doc_tokens = []        #for storing each quotes in the list.
snowball_stemmer = SnowballStemmer('english')
docFiles = [f for f in os.listdir('./jsonnn') if f.endswith(".json")]
docFiles.sort()

def buildIDF():
    """
    function for building the IDF
    """
    z=0
    for word in vocabulary:
        z+=1
        # print(z)
        for document_tokens in document_tokens_list:
            if word in document_tokens:
                if word in vocabulary_idf:

                    vocabulary_idf[word] = vocabulary_idf[word] + 1


                else:
                    vocabulary_idf[word] = 1


def buildFreqDist(document_tokens_list):
    """
    function for building the FreqDistribution
    """
    i=0
    z=0
    for document_tokens in document_tokens_list:
        z+=1
        # print(z)

        freqDist[i] = FreqDist(document_tokens)

        i = i + 1


def returnTermFrequency(term, document_tokens, document_tokens_index):
    """
    Function to return the term frequency
    """
    return math.log2(1+(freqDist[document_tokens_index][term]/float(len(document_tokens))))

def returnIdf(term):
    """
    Function to return corresponding idf
    searching in the vocabulary
    """
    return math.log2(len(document_tokens_list)/vocabulary_idf[term])

"""
Funnction for computing the primary dictionary necessary for tf-idf calculations
The structure is as follows:
It has nested dictionaries
DICTIONARY1-word in vocabulary:
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
