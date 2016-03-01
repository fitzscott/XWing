# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:50:49 2015

@author: bushnelf
"""

import Ship
import AttackResults

# Rebel ships
xw = Ship.Ship("X-Wing", 3, 2, 3, 2)
yw = Ship.Ship("Y-Wing", 2, 1, 5, 3)
bw = Ship.Ship("B-Wing", 3, 1, 3, 5)
aw = Ship.Ship("A-Wing", 2, 3, 2, 2)

# Imperial ships
tie = Ship.Ship("TIE", 2, 3, 3, 0)
advtie = Ship.Ship("Adv TIE", 2, 3, 3, 2)

ar1 = AttackResults.AttackResults(xw, tie)
ar1.focuscombos()
ar2 = AttackResults.AttackResults(yw, tie)
ar2.focuscombos()
ar3 = AttackResults.AttackResults(bw, tie)
ar3.focuscombos()
ar4 = AttackResults.AttackResults(aw, tie)
ar4.focuscombos()
