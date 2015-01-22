#!/usr/bin/python
from ROOT import TCanvas,TH1F,TH2F,TGraphErrors
import numpy as np
import math
import dice

damagehisto=TH1F("damage","damage",41,-0.5,40.5)
damagehisto=TH1F("damage","damage",41,-0.5,40.5)
bennyhisto=TH1F("bennies","bennies used",4,-0.5,3.5)
FAR=dice.swWeapon("FAR",2*[8],3,2)
NK=dice.swWeapon("FAR",2*[8],4,0)
TN=5
myWeapon=NK
for ii in range(int(1e4)):
    benny=3
    damage=myWeapon.attack(TN,8)
    while int(damage)==0 and benny>0:
        damage=myWeapon.attack(TN,8)
        benny-=1
    bennyhisto.Fill(3-benny)
    damagehisto.Fill(damage)
bennyhisto.Scale(1/bennyhisto.GetEntries())
damagehisto.Scale(1/damagehisto.GetEntries())
c1=TCanvas("attacks","attacks",800,600)
c1.Divide(1,2)
prob1=0
prob2=0
for ii in range(damagehisto.FindBin(7),damagehisto.GetNbinsX()):
    prob1+=damagehisto.GetBinContent(ii)
for ii in range(damagehisto.FindBin(11),damagehisto.GetNbinsX()):
    prob2+=damagehisto.GetBinContent(ii)
print "Probality to shake:"+str(prob1*100)+"%"
print "Probality to kill:"+str(prob2*100)+"%"
print "Average number of bennies used:"+str(bennyhisto.GetMean())
c1.cd(1)
damagehisto.Draw()
c1.cd(2)
bennyhisto.Draw()
