# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:50:49 2015

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

# Scum ships
m3a = Ship.Ship("Scyk", 2, 3, 2, 1)
hwk = Ship.Ship("Hawk", 1, 2, 4, 1)
z95 = Ship.Ship("Z-95", 2, 2, 2, 2)

xw.faceoff(tie)
xw.faceoff(advtie)

m3a.faceoff(tie)
z95.faceoff(tie)
