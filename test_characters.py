#!/usr/bin/python
from ROOT import TCanvas,TH1F,TH2F,TGraphErrors
import numpy as np
import math
import dice
import cards
import characters
damagehisto=TH1F("damage","damage",41,-0.5,40.5)
bennyhisto=TH1F("bennies","bennies used",4,-0.5,3.5)
FAR=dice.swWeapon("FAR",2*[8],3,2)
NK=dice.swWeapon("FAR",2*[8],4,0)
TN=5

joe=characters.swCharacter("joe")
jill=characters.swCharacter("jill")
jack=characters.swCharacter("jack")

characters=[joe,jill]
actiondeck=cards.deck52()

for hero in characters:
    hero.AddSkill("Shooting", 12)
    hero.AddWeapon(FAR)
    hero.DrawInitiative(actiondeck)

fight=True
while fight:
    print "New turn. We now deal cards...."
    for hero in characters:
        hero.DrawInitiative(actiondeck)
    characters.sort(key=lambda character:character.inicard, reverse=True)
    for hero in characters:
        if fight==False:
            break
        print "It is "+hero.name+"'s turn ("+str(hero.inicard)+")"
        print hero.name+" has "+str(hero.wounds)+" wounds."
        for enemy in characters:
            if hero!=enemy:
                hero.Attack("FAR",enemy)
                if enemy.wounds>3:
                    print enemy.name+" has lost the fight..."
                    fight=False
            
