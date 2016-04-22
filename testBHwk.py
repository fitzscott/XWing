# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:50:49 2015

@author: bushnelf
"""

import Ship
import SplitRangeShip
import AttackResults

# Scum ships
# Hawk with a blaster turret
hwk = SplitRangeShip.SplitRangeShip("HWK-290b", 1, 2, 4, 1, 3)
hwk.addsplit(3)
hwk.addsplit(1)

# Rebel ships
xw = Ship.Ship("X-Wing", 3, 2, 3, 2)
yw = Ship.Ship("Y-Wing", 2, 1, 5, 3)
bw = Ship.Ship("B-Wing", 3, 1, 3, 5)
aw = Ship.Ship("A-Wing", 2, 3, 2, 2)

# Imperial ships
tie = Ship.Ship("TIE", 2, 3, 3, 0)
advtie = Ship.Ship("Adv TIE", 2, 3, 3, 2)
tieint = Ship.Ship("Tie Interceptor", 3, 3, 3, 0)
deftie = Ship.Ship("TIE Defender", 3, 3, 3, 3)
phantie = Ship.Ship("TIE Phantom", 4, 2, 2, 2)

ar = AttackResults.AttackResults(hwk, xw)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, yw)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, bw)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, aw)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, tie)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, advtie)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, tieint)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, deftie)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, phantie)
