import json
import os

authors_list = []
categories_list = []
docFiles = [f for f in os.listdir('./jsonnn') if f.endswith(".json")]

"""
Function for creating authors_list and categories_list and then storing in json file for further usage
"""
for file in docFiles:
    with open("./jsonnn/" + file, encoding='utf8') as json_data:
        document = json.load(json_data)

    for word in document['authors']:
        authors_list.append(word)
    
    for ct in document["categories"]:
        categories_list.append(ct)

# storing in json file
a = set(authors_list)
a = list(a)
a.sort()
print('\n'.join(a))

b = set(categories_list)
b = list(b)
b.sort()
print('\n'.join(b))

if not os.path.exists('savers'):
    os.mkdir('savers')
with open('savers/authors_list.json', 'w', encoding='utf8') as fp:
    json.dump(a, fp, ensure_ascii=False)

with open('savers/category.json', 'w', encoding='utf8') as fp:
    json.dump(b, fp, ensure_ascii=False)
