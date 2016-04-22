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
yw = Ship.Ship("Y-Wing", 2, 1, 5, 3)

# Imperial ships
tie = Ship.Ship("TIE", 2, 3, 3, 0)
tieint = Ship.Ship("Tie Interceptor", 3, 3, 3, 0)
tiedef = Ship.Ship("TIE Defender", 3, 3, 3, 3)

ar = AttackResults.AttackResults(z95, tie)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, tie)
ar.focuscombos()
ar = AttackResults.AttackResults(yw, tie)
ar.focuscombos()

ar = AttackResults.AttackResults(z95, tieint)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, tieint)
ar.focuscombos()
ar = AttackResults.AttackResults(yw, tieint)
ar.focuscombos()

ar = AttackResults.AttackResults(z95, tiedef)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, tiedef)
ar.focuscombos()
ar = AttackResults.AttackResults(yw, tiedef)
ar.focuscombos()

