#!/opt/local/bin/python
from ROOT import TCanvas,TH1F,TH2F,TGraphErrors
import numpy as np
import math
import dice
#damagehisto=TH1F("damage","damage",61,-0.5,50.5)
colt=dice.swWeapon("Colt 1911",[6,6],fixed=1,atkb=0,wildcard=False)
eagle=dice.swWeapon("Desert Eagle",[8,8],fixed=0,atkb=0,wildcard=False)
tn=4
toughness=6
noMercy=False
skill=6
maxbenny=5
weapon=eagle
def try_weapon(function,name,printout=False):
    damage=[]
    for ii in range(int(1e4)):
        damage.append(function())
    woundhisto=TH1F(name,name,reduce(lambda x,y:max(x,y),damage)+2,-1.5,reduce(lambda x,y:max(x,y),damage)+0.5)
    woundhisto.GetXaxis().SetTitle("Wounds")
    woundhisto.GetYaxis().SetTitle("Prob. [%]")
    for ii in range(int(1e4)):
        damage=function()
        woundhisto.Fill(damage)
    woundhisto.Sumw2()
    woundhisto.Scale(1/woundhisto.GetEntries())
    if printout:
        prob1=0
        prob2=0
        prob3=0
        prob4=0
        prob5=0
        for ii in range(woundhisto.FindBin(0),woundhisto.GetNbinsX()):
            prob1+=woundhisto.GetBinContent(ii)
        for ii in range(woundhisto.FindBin(1),woundhisto.GetNbinsX()):
            prob2+=woundhisto.GetBinContent(ii)
        for ii in range(woundhisto.FindBin(2),woundhisto.GetNbinsX()):
            prob3+=woundhisto.GetBinContent(ii)
        for ii in range(woundhisto.FindBin(3),woundhisto.GetNbinsX()):
            prob4+=woundhisto.GetBinContent(ii)
        for ii in range(woundhisto.FindBin(4),woundhisto.GetNbinsX()):
            prob5+=woundhisto.GetBinContent(ii)
        print 10*"-",name,10*"-"
        print "Probality to at least shake:",round(prob1*100,0),"%"
        print "Probality 1 or more wound:",round(prob2*100,0),"%"
        print "Probality 2 or more wounds:",round(prob3*100,0),"%"
        print "Probality 3 or more wounds:",round(prob4*100,0),"%"
        print "Probality for incapacitation:",round(prob5*100,0),"%"
        print 22*"-"+str(len(name)*"-")+2*"\n"
        #print "Average number of bennies used:"+str(bennyhisto.GetMean())
    return woundhisto

def two_rapid():
    f=lambda :weapon.rapid_attack(TN=tn,Skill=skill,Toughness=toughness)
    dam=[f() for _ in range(2)]
    benny=maxbenny
    for i in range(len(dam)):
        while dam[i]==-1 and benny>0:
            dam[i]=f()
    return dice.multiple_attacks(dam)

def two_rapid_called():
    f=lambda :weapon.rapid_attack(TN=tn+4,Skill=skill,Toughness=toughness-4)
    dam=[f() for _ in range(2)]
    benny=maxbenny
    for i in range(len(dam)):
        while dam[i]==-1 and benny>0:
            dam[i]=f()
    return dice.multiple_attacks(dam)

def two_double():
    f=lambda :weapon.double_tap(TN=tn,Skill=skill,Toughness=toughness)
    dam=[f() for _ in range(2)]
    benny=maxbenny
    for i in range(len(dam)):
        while dam[i]==-1 and benny>0:
            dam[i]=f()
    return dice.multiple_attacks(dam)

def two_double_called():
    f=lambda :weapon.double_tap(TN=tn+4,Skill=skill,Toughness=toughness-4)
    dam=[f() for _ in range(2)]
    benny=maxbenny
    for i in range(len(dam)):
        while dam[i]==-1 and benny>0:
            dam[i]=f()
    return dice.multiple_attacks(dam)

def two_aimed_called():
    f=lambda :weapon.attack(TN=tn+2,Skill=skill,Toughness=toughness-4)
    dam=[f() for _ in range(2)]
    benny=maxbenny
    for i in range(len(dam)):
        while dam[i]==-1 and benny>0:
            dam[i]=f()
    return dice.multiple_attacks(dam)

histos=[]
printout=False
name="Aimed Shot"
histos.append(try_weapon(two_aimed_called,name,printout))
name="Double Tap"
histos.append(try_weapon(two_double,name,printout))
name="Rapid Fire"
histos.append(try_weapon(two_rapid,name,printout))
name="Double Tap (Called Shot)"
histos.append(try_weapon(two_double_called,name,printout))
name="Rapid Fire (Called Shot)"
histos.append(try_weapon(two_rapid_called,name,printout))


c1=TCanvas("attacks","attacks",800,600)
xlen=int(math.sqrt(len(histos)))
ylen=int(len(histos)/xlen+1)
c1.Divide(xlen,ylen)
for ii in range(len(histos)):
    c1.cd(ii+1)
    histos[ii].Draw()
c1.Print(weapon.name+str(".pdf"))
