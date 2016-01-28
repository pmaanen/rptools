#!/usr/bin/ipython
import dice,ROOT
def doMillenium():
    mydie=dice.die
    ages=1000*[1000]
    for i in range(1000,1,-1):
        for i in range(50):
            ages[mydie.roll1dX(1000)-1]=i
    return ages

agehisto=ROOT.TH1F("age","Age of building",1001,-0.5,1000.5)
for i in range(int(100)):
    for age in doMillenium():
        agehisto.Fill(age)
