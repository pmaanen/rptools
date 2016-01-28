#!/usr/bin/env python
import dice
suc=0
for i in range(int(1e5)):
    roll=max(dice.die.roll1dX(12,True),dice.die.roll1dX(6,True))-2
    if roll>=4:
        suc+=1
print "Chance of success=",float(suc/1e5)*100,"%"
