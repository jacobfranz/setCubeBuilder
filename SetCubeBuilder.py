import requests
import json

#declare a global variable that will count the total number of cards that will be in the cube
#mostly for debugging
totalCards = 0


#this will be passed fetch which is a json blob from scryfall, number which is the number of cards used for that rarity, 
# and f which is the file object for writing
def getNames(fetch, number, f):
    #get the correct json blob

    #this tells python that the global variable will be used in the method
    global totalCards

    #get the last item in the json blob and store it as item
    #need to figure out a better way to do this
    for x in fetch.items():
        item = x

    #switch to the list of cards rather than the first part of the blob
    cardList = item[1]

    #this will print the number of cards for each search which is primarily for debugging
    #print(len(cardList))

    #iterate through the list of cards to write them and confirm that they are not promotional cards
    for card in cardList:

        #the key 'promo_types' will only be in the dictionary if the card is a promo
        #that means that we skip any card that has that key in its dictionary
        if 'promo_types' not in card:
            #add to the global counter a number which corresponds to how many copies of that rarity are being added
            totalCards = totalCards + number
            f.write(str(number))
            f.write(' ')
            f.write(card['name'])
            f.write('\n')

#get the set code for the scryfall query
setCode = input('What set code corresponds to the set you are using for your cube? Ex: DOM ')
print()

#open the file that the card names and numbers will be written to
f = open("cardnames.txt", "w+")

#get the json blob from scryfall and store it in fetch which will be passed to getNames
response = requests.get('https://api.scryfall.com/cards/search?order=set&q=set%3A{}+rarity%3Am+not%3Apwdeck'.format(setCode))
fetch = response.json()

#find the number of cards that they want from each rarity
number = int(input("How many copies do you want of each Mythic? "))

#write the rarity to the text document
f.write('Mythics \n')

#call get names
getNames(fetch, number, f)

#go to the next line on the console and on the text document
f.write('\n')
print()

response = requests.get("https://api.scryfall.com/cards/search?order=set&q=set%3A{}+rarity%3Ar+not%3Apwdeck".format(setCode))
fetch = response.json()

number = int(input("How many copies do you want of each Rare? "))
f.write('Rares \n')
getNames(fetch, number, f)
f.write('\n')
print()

response = requests.get("https://api.scryfall.com/cards/search?order=set&q=set%3A{}+rarity%3Au+not%3Apwdeck".format(setCode))
fetch = response.json()

number = int(input("How many copies do you want of each Uncommon? "))
f.write('Uncommons \n')
getNames(fetch, number, f)
f.write('\n')
print()

response = requests.get("https://api.scryfall.com/cards/search?order=set&q=set%3A{}+rarity%3Ac+not%3Apwdeck+-t%3Abasic".format(setCode))
fetch = response.json()

number = int(input("How many copies do you want of each Common? "))
f.write('Commons \n')
getNames(fetch, number, f)
f.write('\n')

#print the total cards needed for the cube
print('You need ' + str(totalCards) + ' cards.')

#close the file
f.close()









