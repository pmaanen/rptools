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
SMG=dice.swWeapon("SMG",2*[6],6,0)
TN=5

zed=characters.swCharacter("zombie")
knight=characters.swCharacter("Knight Mustermann",toughness=12)

characters=[zed, knight]
actiondeck=cards.deck52()

zed.AddSkill("Shooting",6)
zed.AddWeapon(SMG)
for hero in characters:
    hero.DrawInitiative(actiondeck)

fight=True
shuffle=False
while fight:
    print "New turn. We now deal cards...."
    for hero in characters:
        hero.DrawInitiative(actiondeck)
        if not hero.inicard:
            actiondeck.shuffle()
            hero.DrawInitiative(actiondeck)
        if hero.inicard.value==15:
            shuffle=True
    characters.sort(key=lambda character:character.inicard, reverse=True)
    for hero in characters:
        if hero.name=="knight":
            continue
        if fight==False:
            break
        print "It is "+hero.name+"'s turn ("+str(hero.inicard)+")"
        if hero.shaken:
            print hero.name+" tries to unshake...:",hero.UnShake()
        if not hero.canAct:
            print hero.name+" can not act in this round!"
            continue
        for enemy in characters:
            if hero!=enemy:
                hero.Attack("SMG",enemy)
                if enemy.wounds>3:
                    print enemy.name+" has lost the fight..."
                    fight=False
            
