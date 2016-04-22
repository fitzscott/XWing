# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:50:49 2015

@author: bushnelf
"""

import Ship
import AttackResults

# Scum ships
z95 = Ship.Ship("Z-95", 2, 2, 2, 2)
m3a = Ship.Ship("Scyk", 2, 3, 2, 1)
hwk = Ship.Ship("HWK-290", 1, 2, 4, 1)
fs = Ship.Ship("Firespray-31", 3, 2, 6, 4)

# Rebel ships
xw = Ship.Ship("X-Wing", 3, 2, 3, 2)
yw = Ship.Ship("Y-Wing", 2, 1, 5, 3)
bw = Ship.Ship("B-Wing", 3, 1, 3, 5)
aw = Ship.Ship("A-Wing", 2, 3, 2, 2)

ar = AttackResults.AttackResults(z95, xw)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, xw)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, xw)
ar.focuscombos()
ar = AttackResults.AttackResults(fs, xw)
ar.focuscombos()

ar = AttackResults.AttackResults(z95, yw)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, yw)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, yw)
ar.focuscombos()
ar = AttackResults.AttackResults(fs, yw)
ar.focuscombos()

ar = AttackResults.AttackResults(z95, bw)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, bw)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, bw)
ar.focuscombos()
ar = AttackResults.AttackResults(fs, bw)
ar.focuscombos()

ar = AttackResults.AttackResults(z95, aw)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, aw)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, aw)
ar.focuscombos()
ar = AttackResults.AttackResults(fs, aw)
ar.focuscombos()

