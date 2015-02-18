#!/usr/bin/ipython
import cards

mydeck=cards.deck52()

for i in range(53):
	print str(mydeck.draw())

mydeck.shuffle()
for i in range(27):
    card1=mydeck.draw()
    card2=mydeck.draw()
    if (card1<card2):
        print str(card1)+" is less than "+str(card2)
    else:
        print str(card1)+" is not less than "+str(card2)
mydeck.shuffle()
cards=[]
print str(len(mydeck.cards))+ " cards in deck. Drawing each card..."
card=mydeck.draw()
while card != None:
    cards.append(card)
    card=mydeck.draw()
print "I have drawn "+str(len(cards))+" cards."
print "-----------------UNSORTED----------------------"
for card in cards:
    print str(card)
cards.sort()
print "------------------SORTED---------------------"
for card in cards:
    print str(card)


    
