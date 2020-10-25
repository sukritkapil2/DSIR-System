#!/usr/bin/python3

# Importing required modules
import json
from math import log
import os
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer

# Initialization
with open('savers/primeDictionary.json', encoding='utf8') as json_data:
    primeDictionary = json.load(json_data)

with open('savers/normaliseddenom.json', encoding='utf8') as json_data:
    documentNormalizedDenominator = json.load(json_data)


class main_class(object):
    smallcorpusSize = 500
    queryStr = ''  # query from userinput

    '''
	Function for inputting query and performing query based operations and finally calculating cosine scores
	'''
    @staticmethod
    def terminal_function():

        with open('savers/score.json', encoding='utf8') as json_data:
            score = json.load(json_data)

        words = main_class.queryStr
        temp_doc_tokens = word_tokenize(words)
        temp_doc_tokens = [w.lower() for w in temp_doc_tokens]
        stemmer = SnowballStemmer('english')
        temp_doc_tokens = [stemmer.stem(w) for w in temp_doc_tokens]
        queryList = temp_doc_tokens

        numOfWords = 0
        queryDict = {}  # Contains frequency till here i.e the tf

        # Calculating frequency
        for q in queryList:
            numOfWords += 1
            queryDict[q] = queryDict.get(q, 0) + 1

        # Getting total Document frequency of the word
        queryDf = {}
        for qkey in queryDict:
            if qkey in primeDictionary:  # now here we have one document, we have to sum over multiple documents
                innerDict = primeDictionary[qkey]
                total_frequency_of_documents = 0
                for i in innerDict:
                    if(innerDict[i]['1'] > 0):
                        total_frequency_of_documents += 1
                queryDf[qkey] = total_frequency_of_documents
            else:
                queryDf[qkey] = 0

        # Check all formulae here
        queryIdf = {}
        for q in queryDf:
            if (queryDf[q] != 0):
                queryIdf[q] = log(main_class.smallcorpusSize / queryDf[q])
            else:
                queryIdf[q] = 1 + \
                    log(main_class.smallcorpusSize / 1 + queryDf[q], 10)

        queryDict = {key: log(1 + (value / float(numOfWords)))
                     for key, value in queryDict.items()}

        # tfWeighting - multiplying tf-raw i.e. tf and Idf
        queryWt = {key: queryIdf[key] * queryDict[key] for key in queryIdf}

        queryNormalizedDenomator = 0
        for q in queryWt:
            queryNormalizedDenomator += queryWt[q] ** 2

        queryNormalizedDenomator = queryNormalizedDenomator ** 0.5

        # queryNormalized = {key: queryWt[key] / queryNormalizedDenomator for key in queryWt}

        # Iterate over the weight of every term, score the summation in score
        for q in queryWt:
            if q in primeDictionary:
                # now parse all documents
                innerDict = primeDictionary[q]
                for i in innerDict:
                    # print(i)
                    # print(documentNormalizedDenominator[i])
                    # print(innerDict[i]['3'])
                    score[i] += queryWt[q] * \
                        (innerDict[i]['3'] / documentNormalizedDenominator[i])

        with open('savers/store.json', 'w', encoding='utf8') as fp:
            json.dump(score, fp, ensure_ascii=False)

    '''
	Sort the pages according tf-idf cosine similarity
	'''
    @staticmethod
    def process_function(query):
        # print('>>>>>')
        # print(query)
        main_class.queryStr = query
        main_class.terminal_function()
        # print('Yes')

        # find max score page
        with open('savers/store.json', encoding='utf8') as json_data:
            score = json.load(json_data)

        sorted_score = sorted(score, key=score.get, reverse=True)
        # print(sorted_score)
        linkNumber_list = sorted_score[:10]
        newlist = []
        for f in linkNumber_list:
            f = int(float(f)) + 1

            with open(f'./jsonnn/{f}.json', encoding='utf8') as json_data:
                document = json.load(json_data)

            contents = '<img src=\"' + document['thumbnailUrl'] + '\" alt=\"' + document['title'] + '\">' + \
                '<br></br> <strong>' + \
                document['title'] + '</strong>' + \
                '<br></br>' + '<span>' + document['desc']

            if(len(document['desc']) != 0):
                contents += '<br></br>'

            contents += "</span><span style='font-family: Arial; color: blueviolet'>"

            for i, content in enumerate(document['authors']):
                if i != len(document['authors']) - 1:
                    contents += f' {content},'
                else:
                    contents += f' {content}'

            contents += '</span>'
            newlist.append(contents)

        return newlist
