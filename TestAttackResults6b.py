# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:50:49 2015

@author: bushnelf
"""

import Ship
import AttackResults

# Scum ships
m3ah = Ship.Ship("Hvy Scyk", 3, 3, 2, 1)

# Imperial ships
tie = Ship.Ship("TIE", 2, 3, 3, 0)
tieint = Ship.Ship("Tie Interceptor", 3, 3, 3, 0)
tiedef = Ship.Ship("TIE Defender", 3, 3, 3, 3)

ar = AttackResults.AttackResults(m3ah, tie)
ar.focuscombos()
ar = AttackResults.AttackResults(m3ah, tieint)
ar.focuscombos()
ar = AttackResults.AttackResults(m3ah, tiedef)
ar.focuscombos()

