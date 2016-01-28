#!/usr/bin/python
from dice import die

pool=range(1,16)
numbers=[]
for i in range(9):
    numbers.append(pool.pop(die.roll1dX(len(pool))-1))

for i in range(3):
    print numbers[3*i],numbers[3*i+1],numbers[3*i+2]
