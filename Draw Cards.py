import random
import copy

# FUNCTIONS

def createDeck(lowerVal, upperVal):
    deck = [num for num in range(lowerVal, upperVal + 1)]
    return deck

def drawNoRemove(deck):
    if len(deck) == 0:
        print("Empty deck. Cannot play a card.")
        return
    
    index = random.randint(0, len(deck) - 1)
    return deck[index]

def drawAndRemove(deck, copyDeck):
    if len(deck) == 0:
        print("Deck empty, resetting deck.")
        resetDeck(deck, copyDeck)

    index = random.randint(0, len(deck) - 1)
    return deck.pop(index)

def draw(removeCards, deck, copyDeck):
    input("Press enter to draw a card")
    if removeCards:
        card = drawAndRemove(deck, copyDeck)
    else:
        card = drawNoRemove(deck)
    return card

def resetDeck(deck, copyDeck):
    if len(deck) != 0:
        return
    for card in copyDeck:
        deck.append(card)

# MAIN

lowerbound = (input("What is the lowest number card you would like? "))

while not lowerbound.isdigit():
    print("Invalid input, an integer wasn't given")
    lowerbound = (input("What is the lowest number card you would like? "))
lowerbound = int(lowerbound)

upperbound = (input("What is the highest number card you would like? "))

while not upperbound.isdigit():
    print("Invalid input, an integer wasn't given")
    upperbound = (input("What is the highest number card you would like? "))
upperbound = int(upperbound)

myDeck = createDeck(lowerbound, upperbound)
copyDeck = copy.deepcopy(myDeck)

removeCards = False
print("Would you like cards to be removed from the deck once you draw them?")
drawType = input("Type \"r\" for removed, and any other key for them not to be removed. ")

if drawType == "r":
    removeCards = True

while True:
    # print(len(myDeck)) # for debugging purposes only
    print("Your card is: ", draw(removeCards, myDeck, copyDeck))