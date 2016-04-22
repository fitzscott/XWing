# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:50:49 2015

@author: bushnelf
"""

import Ship
import AttackResults

# Rebel ships
yw = Ship.Ship("Y-Wing", 2, 1, 5, 3)

# Imperial ships
deftie = Ship.Ship("TIE Defender", 3, 3, 3, 3)

ar2 = AttackResults.AttackResults(yw, deftie)
ar2.focuscombos()

