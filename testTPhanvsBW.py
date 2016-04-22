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
phantie = Ship.Ship("TIE Phantom", 4, 2, 2, 2)

ar3 = AttackResults.AttackResults(phantie, bw)
ar3.focuscombos()

