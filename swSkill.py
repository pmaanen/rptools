#!/opt/local/bin/python
import ROOT
import dice

def rollSkill(skill):
    return max(dice.die.roll1dX(skill,True),dice.die.roll1dX(6,True))

suc=ROOT.TH1F("suc","suc",20,-0.5,19.5)
ben=ROOT.TH1F("ben","ben",15,-0.5,14.5)
for i in range(1000000):
    bennies=3
    nSuc=int((rollSkill(12))/4)
    while nSuc<8 and bennies>0:
        nSuc=rollSkill(8)
        bennies-=1
    ben.Fill(bennies)
    suc.Fill(nSuc)

suc.Scale(1/float(suc.GetEntries()))
ben.Scale(1/float(ben.GetEntries()))
    
