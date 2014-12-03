#!/usr/bin/python
from ROOT import TCanvas,TH1F,TH2F,TGraphErrors
import numpy as np
import math
import dice
from subprocess import call
damagehisto=TH1F("damage","damage",1001,-0.5,1000.5)
dmhisto=TH2F("dam","dam",70,-0.5,69.5,1001,-0.5,1000.5)
bethune=dice.fighter("Bethune")
gs=dice.pfWeapon("Greatsword",[27,24,19,14],2*[6],35,4,2,10*[6])
bethune.add(gs)

dragon=dice.fighter("Mature Adult Red Dragon")
bite=dice.pfWeapon("Bite",[28],2*[8],16,2,2)
claw=dice.pfWeapon("Claws",2*[28],2*[6],11)
wings=dice.pfWeapon("Wings",2*[26],[8],5)
tail=dice.pfWeapon("tailslap",[26],2*[6],16)
dragon.add(bite)
dragon.add(claw)
dragon.add(wings)
dragon.add(tail)
AC=[]
dam_pa=[]
dam_err_pa=[]
ac_err=[]
nevents=5000
acrange=range(10,50)
AC=[]
dam=[]
dam_err=[]
ac_err=[]
 
for ac in acrange:
    for ii in range(nevents):
        dama=bethune.fullAttack(ac)
        damagehisto.Fill(dama)
        dmhisto.Fill(ac,dama)
    print "AC= "+str(ac)+" Damage= "+str(damagehisto.GetMean())+"+/-"+str(damagehisto.GetRMS())
    AC.append(ac+0.01)
    dam.append(damagehisto.GetMean())
    dam_err.append(damagehisto.GetRMS()/math.sqrt(nevents))
    ac_err.append(0.01)
    damagehisto.Reset()



    
can=TCanvas("Damage","Damage",800,600)
graph=TGraphErrors(len(dam),np.asarray(AC),np.asarray(dam),np.asarray(ac_err),np.asarray(dam_err))
graph.SetFillColor(0)
graph.SetMarkerStyle(20)
graph.GetXaxis().SetTitle("enemy AC")
graph.GetYaxis().SetTitle("DPR")
graph.SetTitle("Dragon")
graph.Draw("ALP")
can.BuildLegend()
can.SetTitle("Weapon Damage")
can.Print("dragon.pdf")
dmhisto.Draw()
can.Print("dragon2dplot.pdf")
call(["open", "comp.pdf"])
call(["open","2dplot.pdf"])
