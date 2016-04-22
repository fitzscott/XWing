# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:50:49 2015

@author: bushnelf
"""

import Ship
import AttackResults

# Rebel ships
xw = Ship.Ship("X-Wing", 3, 2, 3, 2)

# Imperial ships
deftie = Ship.Ship("TIE Defender", 3, 3, 3, 3)

ar2 = AttackResults.AttackResults(deftie, xw)
ar2.focuscombos()

