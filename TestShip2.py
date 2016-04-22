# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:25:23 2015

@author: bushnelf
"""


import Ship
import SplitRangeShip

# Imperial ships
tie = Ship.Ship("TIE", 2, 3, 3, 0)

# Scum ships
# Hawk with a blaster turret
hwk = SplitRangeShip.SplitRangeShip("HWK-290b", 1, 2, 4, 1, 3)
hwk.addsplit(3)
hwk.addsplit(1)

hwk.attacktarget(tie, evade=True)
print("-----------------------------------------------")
hwk.attacktarget(tie, evade=False)
print("-----------------------------------------------")

