import json

<<<<<<< HEAD
with open("./savers/authors_list.json", encoding='utf8') as json_data:
=======
with open('./savers/authors_list.json', encoding='utf8') as json_data:
>>>>>>> pranjal
    document = json.load(json_data)

htmlString = "<div class='row mt-2'>"

i = 0

for author in document:
    i += 1
    htmlString += "<div class='ml-2' style='display: block; padding: 20px; background-color: blueviolet;border-radius: 10px';><form action='/result' method='POST'><input type='hidden' name='query' value=" + str(author) + "/><button class='text-white' style='font-family: Montserrat; font-weight: 400; background: none; border: none; outline: none; cursor: pointer'>" + \
        str(author) + "</button></form></div>"
    if (i % 5 == 0):
        htmlString += "</div><div class='row mt-2'>"

print(htmlString)

with open('savers/htmlfinal.json', 'w', encoding='utf8') as fp:
    json.dump(htmlString, fp, ensure_ascii=False)
