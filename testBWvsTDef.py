# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:50:49 2015

@author: bushnelf
"""

import Ship
import AttackResults

# Rebel ships
bw = Ship.Ship("B-Wing", 3, 1, 3, 5)

# Imperial ships
deftie = Ship.Ship("TIE Defender", 3, 3, 3, 3)

ar3 = AttackResults.AttackResults(bw, deftie)
ar3.focuscombos()

