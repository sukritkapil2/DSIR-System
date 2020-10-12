import json
import os

import numpy as np

docFiles = [f for f in os.listdir('./jsonnn') if f.endswith(".json")]
category = []

for file in docFiles:

    document = dict()
    with open("./jsonnn/" + file, encoding='utf8') as json_data:
        document = json.load(json_data)

    # print(document["Category"])
    # print(file)
    for ct in document["categories"]:
        category.append(ct)

category = np.unique(category).tolist()
with open('savers/category.json', 'w', encoding='utf8') as fp:
    json.dump(category, fp)
