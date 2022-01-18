from ast import While
import csv
import random
import string
import time
import os

class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clover"]

    values = [2, 3,
              4, 5, 6, 7,
              8, 9, 10,
              "Jack", "Queen",
              "King", "Ace"]
                
    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s
cardDeck = []

#add all possible cards to deck
for suit in Card.suits:
    for card in Card.values:
        cardDeck.append(Card(card, suit))

random.shuffle(cardDeck)

#Hand value
playerHand = []
dealerHand = []

def PrintHand(hand, name):
    print(" -- " + name + "'s hand -- ")
    for card in hand:
        print(card.suit + " " + str(card.value))
    print(" -- -- -- ")

def CalculateHandValue(hand):
    totalValue = 0
    aceAmount = 0
    for card in hand:
        if type(card.value) == str:
            if card.value == "Ace":
                aceAmount += 1
                totalValue += 11
            else:
                totalValue += 10
        else:
            totalValue += card.value
    if totalValue > 21 and aceAmount > 0:
        for i in range(aceAmount):
            if totalValue > 21:
                totalValue -= 10
    return totalValue

def Hit():
    cardChoice = cardDeck[0]
    cardDeck.pop(0)
    return cardChoice

def print_game_status(playerHandValue, dealerHandValue):
    os.system('cls' if os.name == 'nt' else 'clear')
    PrintHand(dealerHand, "dealer")
    PrintHand(playerHand, "player")
    print("player handvalue: " + str(playerHandValue))
    print("dealer handvalue: " + str(dealerHandValue))

#starting cards
playerHand.append(Hit())
dealerHand.append(Hit())
playerHand.append(Hit())

gameRunning = True

#main game loop
while gameRunning:
    playerActive = True
    playerBust = False
    playerHandValue = 0
    
    #player logic & moves
    while playerActive:
        playerHandValue = CalculateHandValue(playerHand)
        dealerHandValue = CalculateHandValue(dealerHand)
        print_game_status(playerHandValue, dealerHandValue)
        print("(H)it or (S)tand")
        playerChoice = ""
        while playerChoice != "h" and playerChoice != "s":
            playerChoice = input().lower()
        if playerChoice == "s":
            playerActive = False
        elif playerChoice == "h":
            playerHand.append(Hit())
        playerHandValue = CalculateHandValue(playerHand)
        if playerHandValue > 21:
            print("Player busted")
            playerBust = True
            playerActive = False
  
    #Dealer logic
    print("Dealers turn")
    dealerActive = True
    while dealerActive:
        playerHandValue = CalculateHandValue(playerHand)
        dealerHandValue = CalculateHandValue(dealerHand)
        print_game_status(playerHandValue, dealerHandValue)
        if dealerHandValue < 17:
            dealerHand.append(Hit())
            time.sleep(0.5)
        else:
            if dealerHandValue > 21:
                print("Dealer busted!")
                dealerActive = False
            else:
                dealerActive = False
    dealerBust = (dealerHandValue > 21)
    
    #Win logic
    if playerHandValue == dealerHandValue:
        print("Tie")
        gameRunning = False
    elif (playerHandValue > dealerHandValue and not playerBust) or (dealerBust and not playerBust):
        print("Player wins")
        gameRunning = False
    elif (dealerHandValue > playerHandValue and not dealerBust) or (playerBust and not dealerBust):
        print("Dealer wins")
        gameRunning = False
    else:
        gameRunning = False
        print("Tie")


    