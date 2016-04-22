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
phantie = Ship.Ship("TIE Phantom", 4, 2, 2, 2)

ar2 = AttackResults.AttackResults(xw, phantie)
ar2.focuscombos()

