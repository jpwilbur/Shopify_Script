import json
from pprint import pprint


def json_convert ():
    with open('products.json') as data_local:
        raw_data = json.load(data_local)

    data = raw_data['products']

    lstVariants = {}
    #list of lists; product name concat, price, weight
    prodInfo = []
    dictKeys = []

    for d in data:
        for key, value in d.items():
            if key == 'title' and ('Computer' in value or 'Keyboard' in value):
                lstVariants[value] = d['variants']
                dictKeys.append(value)

    for dkey in dictKeys:
        for d in lstVariants[dkey]:
            for key, value in d.items():
                if key == 'title':
                    titleValue = value + ' ' + dkey
                elif key == 'price':
                    priceValue = value
                elif key == 'grams':
                    weightValue = value
            prodInfo.append([titleValue, priceValue, weightValue])

    print (prodInfo)



json_convert()
