# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:50:49 2015

@author: bushnelf
"""

import Ship
import AttackResults

# Rebel ships
aw = Ship.Ship("A-Wing", 2, 3, 2, 2)

# Imperial ships
deftie = Ship.Ship("TIE Defender", 3, 3, 3, 3)

ar4 = AttackResults.AttackResults(deftie, aw)
ar4.focuscombos()

