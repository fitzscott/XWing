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
phantie = Ship.Ship("TIE Phantom", 4, 2, 2, 2)

ar2 = AttackResults.AttackResults(phantie, yw)
ar2.focuscombos()

