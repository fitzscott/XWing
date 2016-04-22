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
phantie = Ship.Ship("TIE Phantom", 4, 2, 2, 2)

ar4 = AttackResults.AttackResults(phantie, aw)
ar4.focuscombos()

