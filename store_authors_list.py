import json
import os

import nltk

nltk.download('punkt')
nltk.download('stopwords')
authors_list = []
temp_authors_list = []
docFiles = [f for f in os.listdir('./jsonnn') if f.endswith(".json")]

for i in range(len(docFiles)):
    docFiles[i] = int(docFiles[i].split(".")[0])
    # print(docFiles[i])

docFiles.sort()


# print(docFiles)

def create_authors_list():
    """
    Function for creating authors_list and then storing in json file for further usage
    """
    count = 0
    for file in docFiles:
        with open("./jsonnn/" + str(file) + ".json") as json_data:
            document = json.load(json_data)

        count += 1
        words = document['authors']
        for word in words:
            authors_list.append(word)

    # storing in json file
    a = set(authors_list)
    a = list(a)
    a.sort()
    print('\n'.join(a))
    if not os.path.exists('savers'):
        os.mkdir('savers')
    with open('savers/authors_list.json', 'w', encoding='utf8') as fp:
        json.dump(a, fp, ensure_ascii=False)


# calling function
create_authors_list()
