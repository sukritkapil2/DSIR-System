#!/usr/bin/python3

# Importing required modules
import json

# Initialization
with open('savers/primeDictionary.json', encoding='utf8') as json_data:
    primeDictionary = json.load(json_data)

'''
Function to compute denominator for final calculation
'''


def compute_denominator():
    documentNormalizedDenominator = {}
    score = {}

    # Initializing all documentNormalizedDenominator to zero
    for innerDict in primeDictionary.values():
        for i in innerDict:
            documentNormalizedDenominator[i] = 0
            score[i] = 0

    for innerDict in primeDictionary.values():
        for i in innerDict:
            documentNormalizedDenominator[i] += innerDict[i]['3'] ** 2

    documentNormalizedDenominator = {
        key: value ** 0.5 for key, value in documentNormalizedDenominator.items()}

    # Creating json
    with open('savers/normaliseddenom.json', 'w', encoding='utf8') as fp:
        json.dump(documentNormalizedDenominator, fp, ensure_ascii=False)

    with open('savers/score.json', 'w', encoding='utf8') as fp:
        json.dump(score, fp, ensure_ascii=False)


# Calling the function
if __name__ == '__main__':
    compute_denominator()
