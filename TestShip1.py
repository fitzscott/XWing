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

xw.attacktarget(tie)
print("-----------------------------------------------")
yw.attacktarget(tie)
print("-----------------------------------------------")
bw.attacktarget(tie)
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
