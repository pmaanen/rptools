#!/usr/bin/ipython
from ROOT import TH1F,TGraph
from dice import *
from numpy import mean,asarray
def counthits(pool,limit=None,edge=False):
    nhits=0
    for i in range(pool):
        roll=die.roll1dX(6)
        if roll>4:
           nhits+=1
        while roll==6 and edge:
            roll=die.roll1dX(6)
            if roll>4:
                nhits+=1
    if nhits>limit and limit and  not edge:
        nhits=limit
    return nhits

def extendedTest(pool,threshold,limit=None):
    iRound=0
    hits=0
    while pool>0:
        if(hits<threshold):
            hits+=counthits(pool,limit)
            iRound+=1
        pool-=1
    if hits>=threshold:
        return iRound
    else:
        return False
    
def main():
    hits=TH1F("nhits","nhits",20,-0.5,19.5)
    evade=TH1F("nevade","nevade",20,-0.5,19.5)
    nethits=TH1F("net","net",41,-20.5,20.5)
    damage=TH1F("damage","damage",31,-0.5,30.5)
    damage=TH1F("damage","damage",31,-0.5,30.5)
    
    attackpool=9+6+2+2-4+5
    accuracy=6
    dv=13
    ap=18
    evadepool=11-3
    armorpool=35

    for i in range(int(1e4)):
        attack=counthits(attackpool,accuracy,edge=True)
        eva=counthits(evadepool-5)
        hits.Fill(attack)
        evade.Fill(eva)
        nethits.Fill(attack-eva)
        if((attack-eva)>0):
            damage.Fill(attack-eva+dv-counthits(armorpool-ap))
        else:
            damage.Fill(0)
    damage.Sumw2()
    hits.Scale(1./hits.GetEntries())
    evade.Scale(1./evade.GetEntries())
    nethits.Scale(1./nethits.GetEntries())
    damage.Scale(1./damage.GetEntries())
    damage.Sumw2()
    damage.Draw()
    return damage

def MeanHits(pool,limit):
    results=[]
    for i in range(int(1e4)):
        results.append(counthits(pool,limit))
    mean_hits=mean(results)
    return mean_hits
def HitsVsPool():
    meanhits=[]
    pools=[]
    for ipool in range(40):
        pools.append(float(ipool))
    for pool in pools:
        meanhits.append(MeanHits(int(pool),6))
    myGraph=TGraph(len(pools),asarray(pools),asarray(meanhits))
    myGraph.Draw("ALP")
    return myGraph

def when(pool,threshold):
    rounds=TH1F("rounds","rounds",20,-0.5,19.5)
    for i in range(10000):
        iround=extendedTest(pool,threshold)
        if(iround):
            rounds.Fill(iround)
    return rounds
        
        
damage=main()
damage.Fit("gaus")
damage.Draw()
#myGraph=HitsVsPool()
#rounds=when(pool=4,threshold=2)
