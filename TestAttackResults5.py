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
deftie = Ship.Ship("TIE Defender", 3, 3, 3, 3)
phantie = Ship.Ship("TIE Phantom", 4, 2, 2, 2)

ar1 = AttackResults.AttackResults(xw, deftie)
ar1.focuscombos()
ar2 = AttackResults.AttackResults(yw, deftie)
ar2.focuscombos()
ar3 = AttackResults.AttackResults(bw, deftie)
ar3.focuscombos()
ar4 = AttackResults.AttackResults(aw, deftie)
ar4.focuscombos()

ar1 = AttackResults.AttackResults(xw, phantie)
ar1.focuscombos()
ar2 = AttackResults.AttackResults(yw, phantie)
ar2.focuscombos()
ar3 = AttackResults.AttackResults(bw, phantie)
ar3.focuscombos()
# These don't work so well on the old machine.
#ar4 = AttackResults.AttackResults(aw, phantie)
#ar4.focuscombos()

