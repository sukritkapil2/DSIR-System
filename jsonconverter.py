import json
import os

with open('books.json', encoding='utf8') as json_data:
    document = json.load(json_data)


def jsonconverter():
    """
    Function for creating json files and then storing in json file for further usage
    """
    count = 0
    i = 0
    for index in document:
        count += 1
        dictt = dict()
        i = i + 1
        dictt['title'] = index['title']
        index['authors'] = [a for a in index['authors'] if a != '' and a[0] >= 'A' and a[0] <= 'Z']
        dictt['authors'] = index['authors']
        index['categories'] = [a.title() for a in index['categories'] if a != '']
        dictt['categories'] = index['categories']

        file = "jsonnn/" + str(i) + ".json"
        if not os.path.exists('jsonnn'):
            os.mkdir('jsonnn')
        with open(file, 'w', encoding='utf8') as fp:
            json.dump(dictt, fp, ensure_ascii=False)


jsonconverter()
