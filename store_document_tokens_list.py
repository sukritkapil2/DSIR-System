import json
import os

import nltk
from nltk.stem.snowball import SnowballStemmer

nltk.download('punkt')
nltk.download('stopwords')
vocabulary = {}
vocabulary_idf = {}
freqDist = {}
document_tokens_list = []
temp_doc_tokens = []
snowball_stemmer = SnowballStemmer('english')
docFiles = [f for f in os.listdir('./jsonnn') if f.endswith(".json")]

for i in range(len(docFiles)):
    docFiles[i] = int(docFiles[i].split(".")[0])
    # print(docFiles[i])

docFiles.sort()


# print(docFiles)

def create_document_tokens_list():
    """
    Function for creating document_tokens_list and then storing in json file for further usage
    """
    count = 0
    for file in docFiles:
        document = dict()
        with open("./jsonnn/" + str(file) + ".json", encoding='utf8') as json_data:
            document = json.load(json_data)

        count += 1
        words = str(document["title"])
        for author in document["authors"]:
            words += str(" " + author)

        for category in document["categories"]:
            words += str(" " + category)

        print(count)
        temp_doc_tokens = nltk.word_tokenize(words)
        # print(temp_doc_tokens)
        temp_doc_tokens = [w.lower() for w in temp_doc_tokens]
        temp_doc_tokens = [snowball_stemmer.stem(token) for token in temp_doc_tokens]
        temp_doc_tokens = [token for token in temp_doc_tokens if token not in nltk.corpus.stopwords.words('english')]
        # print(temp_doc_tokens)
        document_tokens_list.append(temp_doc_tokens)

    # storing in json file
    with open('savers/document_tokens_list.json', 'w', encoding='utf8') as fp:
        json.dump(document_tokens_list, fp)


# calling function
create_document_tokens_list()
