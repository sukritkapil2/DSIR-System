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
import json

smallcorpusSize=500
queryStr = ""       #query from userinput
vocabulary = {}
vocabulary_idf = {}
freqDist = {}
document_tokens_list= []
temp_doc_tokens = []
    #score={}
snowball_stemmer = SnowballStemmer('english')
    # docFiles = [f for f in os.listdir('./jsonnn') if f.endswith(".json")]
    # docFiles.sort()


with open('./savers/document_tokens_list.json') as json_data:
        document_tokens_list = json.load(json_data)

with open('savers/vocabulary.json') as json_data:
        vocabulary = json.load(json_data)

with open('savers/primeDictionary.json') as json_data:
        primeDictionary = json.load(json_data)


documentNormalizedDenominator={}
score = {}
        #initializing all documentNormalizedDenominator to zero
for q in primeDictionary:
    innerDict=primeDictionary[q]
    for i in innerDict:
        documentNormalizedDenominator[i]=0
        score[i]=0

#print(score)
for q in primeDictionary:
    innerDict=primeDictionary[q]
    for i in innerDict:
        documentNormalizedDenominator[i]+=(math.pow(innerDict[i]['3'],2))


for d in documentNormalizedDenominator:

        documentNormalizedDenominator[d]=documentNormalizedDenominator[d]**0.5

with open('savers/normaliseddenom.json','w') as fp:
		json.dump(documentNormalizedDenominator,fp)

with open('savers/score.json','w') as fp:
		json.dump(score,fp)

        
