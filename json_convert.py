import json
from pprint import pprint


def json_convert ():
    with open('products.json') as data_local:
        raw_data = json.load(data_local)

    data = raw_data['products']

    #all variants
    lstVariants = {}
    #list of lists; product name concat, price, weight
    prodInfo = []
    #uses list of titles for comparison
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

    return prodInfo

#finds smallest product in terms of weight
def find_smallest(lstProducts):
    smallest = lstProducts[0]
    for title, price, weight in prodInfo:
        if weight < smallest[2]:
            smallest = [title,price,weight]
    return smallest

#finds the total weight and price without the smallest item; returns list of price and weight subtotals
def NoSmallestTot (lstProducts):
    smallestItem = find_smallest(lstProducts)
    subTotWeight = 0
    subTotPrice = 0.00
    for item in lstProducts:
        if smallestItem[0] == item[0]:
            lstProducts.remove(item)
        else:
            subTotWeight = subTotWeight + item[2]
            subTotPrice = subTotPrice + float(item[1])
    subTot = [subTotPrice,subTotWeight,lstProducts]
    return subTot

#outputs list of total price, total weight, how many additional of the smallest item
def checkoutTotal (price, weight, smallestItem):
    totPrice = price
    totWeight = weight
    additionalSmall = 0

    while True:
        totPrice = totPrice + float(smallestItem[1])
        totWeight = totWeight + int(smallestItem[2])
        additionalSmall = additionalSmall + 1
        if (totWeight + int(smallestItem[2])) > 100000:
            break

    totals = [totPrice,totWeight,additionalSmall]
    return (totals)

#MAIN
#create list of all computers and keyboards with their variants
prodInfo = json_convert()

#find smallest weight
smallestItem = find_smallest(prodInfo)

lstPriceWeight = NoSmallestTot(prodInfo)
noSmallList = lstPriceWeight[2]
subTotPrice = lstPriceWeight[0]
subTotWeight = lstPriceWeight[1]
checkout = checkoutTotal(subTotPrice,subTotWeight,smallestItem)

for item in noSmallList:
    print ("1 " + item[0] )

print (str(checkout[2]) + " " + smallestItem[0] + "s")

print ("Total Price: {0:.2f}".format(checkout[0]) +" Total Weight: " + str(checkout[1]))
