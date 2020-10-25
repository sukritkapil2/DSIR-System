import json

with open("./savers/category.json", encoding='utf8') as json_data:
    document = json.load(json_data)

htmlString = ""

for category in document:
    htmlString += "<form action='/result' method='POST'><input type='hidden' name='query' value='" + category + \
        "'/>" + "<button class='btn btn-dark-green btn-rounded ml-3' type='submit'>" + \
        category + "</button></form>"

print(htmlString)

with open('savers/htmlfinalCat.json', 'w', encoding='utf8') as fp:
    json.dump(htmlString, fp, ensure_ascii=False)
