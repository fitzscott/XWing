# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:25:23 2015

@author: bushnelf
"""


import Ship

# Rebel ships
xw = Ship.Ship("X-Wing", 3, 2, 2, 3)
yw = Ship.Ship("Y-Wing", 2, 1, 3, 5)
bw = Ship.Ship("B-Wing", 3, 1, 5, 3)
aw = Ship.Ship("A-Wing", 2, 3, 2, 2)

# Imperial ships
tie = Ship.Ship("TIE", 2, 3, 0, 3)
advtie = Ship.Ship("Adv TIE", 2, 3, 2, 3)

xw.attacktarget(tie, evade=True)
print("-----------------------------------------------")
yw.attacktarget(tie, evade=True)
print("-----------------------------------------------")
bw.attacktarget(tie, evade=True)
print("-----------------------------------------------")

tie.attacktarget(xw)
print("-----------------------------------------------")
tie.attacktarget(yw)
print("-----------------------------------------------")
tie.attacktarget(bw)
print("-----------------------------------------------")
tie.attacktarget(aw)

print("-----------------------------------------------")
print("-----------------------------------------------")
print("How about if the TIEs can get in close?")
print("-----------------------------------------------")
tie.attacktarget(xw, True)
print("-----------------------------------------------")
tie.attacktarget(yw, True)
print("-----------------------------------------------")
tie.attacktarget(bw, True)
print("-----------------------------------------------")
tie.attacktarget(aw, True)

print("-----------------------------------------------")
print("-----------------------------------------------")
print("How about if the Rebels can get in close?")
print("-----------------------------------------------")
xw.attacktarget(tie, closerange=True, evade=True)
print("-----------------------------------------------")
yw.attacktarget(tie, closerange=True, evade=True)
print("-----------------------------------------------")
bw.attacktarget(tie, closerange=True, evade=True)
print("-----------------------------------------------")

print("-----------------------------------------------")
print("-----------------------------------------------")
print("And we have to know how much tougher the advanced TIE is...")
print("-----------------------------------------------")
xw.attacktarget(advtie)
print("-----------------------------------------------")
yw.attacktarget(advtie)
print("-----------------------------------------------")
bw.attacktarget(advtie)
print("-----------------------------------------------")
