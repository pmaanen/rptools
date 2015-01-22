#!/usr/bin/python
from numpy import max
from dice import die
from ROOT import TH1F,TCanvas
inihist=TH1F("ini","ini",20,0.5,20.5)
for ii in range(10000):
	inihist.Fill(max([die.roll1dX(20),die.roll1dX(20)]))
