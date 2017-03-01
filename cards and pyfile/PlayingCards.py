# Clint Johnson
# k276x854
# program 12 chapter 10
# Feb. 26, 2015
#
# Function: Playing cards class
# Inputs: None
# Outputs: display 5 cards
# retrun: None
#
# class 'constructor'
#   def __init__()
#   def getRank(self)
#   def getSuit(self)
#   def BJValue(self)
#   def __str__(self)
#
# main()
#   print out n randomly generate cards and the associate BJ value
#   n is inputed by user

# Imported classes
import random
from Graphics import *

class Card:
   
    def __init__(self, rank = 0, suit = "h"):
        'Initializes a playing card. Rank = 1-13, Suit = s, c, d, or h'
        self.myRank = rank
        self.mySuit = suit
    
    def getRank(self):
        'Gets the rank of the playing card'
        return self.myRank
    
    def getSuit(self):
        'Gets the Suit of the playing card'
        return self.mySuit

    def BJValue(self):
        'Gets the Blackjack Value of the card;'
        if ((1 <= self.myRank) and (self.myRank < 10)):
            BJValue = self.myRank
        else:
            BJValue = 10
        return BJValue

    
    def __str__(self):
        if (self.myRank == 1):
            sRank = "Ace"
        elif(self.myRank == 2):
            sRank = "2"
        elif(self.myRank == 3):
            sRank = "3"
        elif(self.myRank == 4):
            sRank = "4"
        elif(self.myRank == 5):
            sRank = "5"
        elif(self.myRank == 6):
            sRank = "6"
        elif(self.myRank == 7):
            sRank = "7"
        elif(self.myRank == 8):
            sRank = "8"
        elif(self.myRank == 9):
            sRank = "9"
        elif(self.myRank == 10):
            sRank = "10"
        elif(self.myRank == 11):
            sRank = "Jack"
        elif(self.myRank == 12):
            sRank = "Queen"
        elif(self.myRank == 13):
            sRank = "King"
        else:
            sRank = "Not a valid card Rank"
        if(self.mySuit == 's'):
            sSuit = "Spades"
        elif(self.mySuit == 'h'):
            sSuit = "Hearts"
        elif(self.mySuit == 'c'):
            sSuit = "Clubs"
        elif(self.mySuit == 'd'):
            sSuit = "Dimands"
        else:
            sSuit = " Not a vaild Suit"
        return (sRank + ' of ' + sSuit)

    def randCard():
        suitList = ('s', 'h', 'd', 'c')
        rank = random.randint(1, 13)
        suit = suitList[random.randint(0,3)]
        new = Card(rank, suit)
        return new

    def draw(self, win, center):
        string = (self.myRank + "_of_" + self.myRank + ".png")
        cardImage = Image(Point(center, 150), string)
        cardImage_draw(win)

    def getName(self):
        if(self.mySuit== 'd'):
            if(self.myRank == 1):
                return "ace_of_diamonds"
            elif(self.myRank == 2):
                return "2_of_diamonds"
            elif(self.myRank == 3):
                return "3_of_diamonds"
            elif(self.myRank == 4):
                return "4_of_diamonds"
            elif(self.myRank == 5):
                return "5_of_diamonds"
            elif(self.myRank == 6):
                return "6_of_diamonds"
            elif(self.myRank == 7):
                return "7_of_diamonds"
            elif(self.myRank == 8):
                return "8_of_diamonds"
            elif(self.myRank == 9):
                return "9_of_diamonds"
            elif(self.myRank == 10):
                return "10_of_diamonds"
            elif(self.myRank == 11):
                return "jack_of_diamonds"
            elif(self.myRank == 12):
                return "queen_of_diamonds"
            elif(self.myRank == 13):
                return "king_of_diamonds"
        elif(self.mySuit== 's'):
            if(self.myRank == 1):
                return "ace_of_spades"
            elif(self.myRank == 2):
                return "2_of_spades"
            elif(self.myRank == 3):
                return "3_of_spades"
            elif(self.myRank == 4):
                return "4_of_spades"
            elif(self.myRank == 5):
                return "5_of_spades"
            elif(self.myRank == 6):
                return "6_of_spades"
            elif(self.myRank == 7):
                return "7_of_spades"
            elif(self.myRank == 8):
                return "8_of_spades"
            elif(self.myRank == 9):
                return "9_of_spades"
            elif(self.myRank == 10):
                return "10_of_spades"
            elif(self.myRank == 11):
                return "jack_of_spades"
            elif(self.myRank == 12):
                return "queen_of_spades"
            elif(self.myRank == 13):
                return "king_of_spades"
        elif(self.mySuit== 'h'):
            if(self.myRank == 1):
                return "ace_of_hearts"
            elif(self.myRank == 2):
                return "2_of_hearts"
            elif(self.myRank == 3):
                return "3_of_hearts"
            elif(self.myRank == 4):
                return "4_of_hearts"
            elif(self.myRank == 5):
                return "5_of_hearts"
            elif(self.myRank == 6):
                return "6_of_hearts"
            elif(self.myRank == 7):
                return "7_of_hearts"
            elif(self.myRank == 8):
                return "8_of_hearts"
            elif(self.myRank == 9):
                return "9_of_hearts"
            elif(self.myRank == 10):
                return "10_of_hearts"
            elif(self.myRank == 11):
                return "jack_of_hearts"
            elif(self.myRank == 12):
                return "queen_of_hearts"
            elif(self.myRank == 13):
                return "king_of_hearts"
        elif(self.mySuit== 'c'):
            if(self.myRank == 1):
                return "ace_of_clubs"
            elif(self.myRank == 2):
                return "2_of_clubs"
            elif(self.myRank == 3):
                return "3_of_clubs"
            elif(self.myRank == 4):
                return "4_of_clubs"
            elif(self.myRank == 5):
                return "5_of_clubs"
            elif(self.myRank == 6):
                return "6_of_clubs"
            elif(self.myRank == 7):
                return "7_of_clubs"
            elif(self.myRank == 8):
                return "8_of_clubs"
            elif(self.myRank == 9):
                return "9_of_clubs"
            elif(self.myRank == 10):
                return "10_of_clubs"
            elif(self.myRank == 11):
                return "jack_of_clubs"
            elif(self.myRank == 12):
                return "queen_of_clubs"
            elif(self.myRank == 13):
                return "king_of_clubs"
#def main():
# ask user for # of cards
#    numberOfCards = eval(input("Please enter the number of cards ")) 
#    count = 1
#    while(count <= numberOfCards):
#        a = Card.randCard()
#        print(a)
#        count += 1
# get a set of 5 card and display

def main():
    numberOfCards = 5
    count = 1
    win = GraphWin("Your Hand", 750, 300)
    win.setBackground('green')
    while (count <= numberOfCards):
        card = Card.randCard()
        image = Image(Point((count*125),150), card.getName() + ".png")
        image.draw(win)
        count = count + 1
    #wait = input("Press return to close") #for .exe file
    
if __name__ == '__main__': main()
