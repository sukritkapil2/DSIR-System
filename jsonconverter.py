import json

with open('quotes.json', encoding='utf-8') as json_data:
    document = json.load(json_data)


def jsonconverter():
    """
    Function for creating json files and then storing in json file for future use
    """
    i = 0
    for count, index in enumerate(document):
        if count % 2 == 1:
            dictt = {}
            if len(index['Quote']) > 20:
                i += 1
                dictt['Quote'] = index['Quote']
                dictt['Author'] = index['Author']
                dictt['Category'] = index['Category']
                with open(f'jsonnn/{i}.json', 'w', encoding='utf8') as fp:
                    json.dump(dictt, fp, ensure_ascii=False)


jsonconverter()
