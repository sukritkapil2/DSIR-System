import json
import os

docFiles = [f for f in os.listdir('./jsonnn') if f.endswith(".json")]
category = []

for file in docFiles:

    with open("./jsonnn/" + file, encoding='utf8') as json_data:
        document = json.load(json_data)


    for ct in document["categories"]:
        category.append(ct)

a = set(category)
a = list(a)
a.sort()
print('\n'.join(a))
with open('savers/category.json', 'w', encoding='utf8') as fp:
    json.dump(category, fp)