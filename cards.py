import numpy.random as npr
from ROOT import TText
import itertools
import codecs

class card:
    # Define the suits
    DIAMONDS = 1
    CLUBS = 4
    HEARTS = 2
    SPADES = 3
    SUITS = {
        CLUBS: 'Clubs',
        HEARTS: 'Hearts',
        DIAMONDS: 'Diamonds',
        SPADES: 'Spades'
    }
 
    # Define the names of special cards
    VALUES = {
        11: 'Jack',
        12: 'Queen',
        13: 'King',
        14: 'Ace',
        15: 'Joker'
    }
 
    def __init__(self, suit, value):
        # Save the suit and card value
        self.suit = suit
        self.value = value
 
    def __lt__(self, other):
        # Compare the card with another card
        # (return true if we are smaller, false if
        # we are larger, 0 if we are the same)
        if self.value < other.value:
            return True
        elif self.value > other.value:
            return False
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        return 0

    def __gt__(self,other):
        if(self.__lt__(other)==0):
            return 0
        else:
            return (not self.__lt(other))

    def __eq__(self,other):
        return selt.__gt__(other)==0
    
    def __str__(self):
        # Return a string description of ourself
        if(self.value==15):
            if self.suit==1:
                return "Red Joker"
            else:
                return "Black Joker"
        if self.value in self.VALUES:
            buf = self.VALUES[self.value]
        else:
            buf = str(self.value)
        buf = buf + ' of ' + self.SUITS[self.suit]
        return buf
class deck:
    def __init__(self):
        self.cards=[]
    def draw(self):
        if(len(self.cards)==0):
            print "No cards left on deck"
            return
        num=npr.randint(0,self.n)
        card=self.cards.pop(num)
        self.n-=1
        return card
    def drawN(self,N=1):
        cards=[]
        for i in range(N):
            cards.append(self.draw)
        return cards
    def shuffle(self):
        self.__init__()

class deck32(deck):
    def __init__(self):
        deck.__init__(self)
        suits=range(1,4)
        ranks=range(7,15)
        for prod in itertools.product(suits,ranks):
             self.cards.append(card(prod[0],prod[1]))
        self.n=len(self.cards)

class deck52(deck):
    def __init__(self):
        deck.__init__(self)
        suits=range(1,5)
        ranks=range(2,15)
        for prod in itertools.product(ranks,suits):
            self.cards.append(card(prod[1],prod[0]))
        self.cards.append(card(1,15))
        self.cards.append(card(3,15))
        self.n=len(self.cards)
