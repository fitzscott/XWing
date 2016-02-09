# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:50:49 2015

@author: bushnelf
"""

import Ship
import AttackResults

# Rebel ships
yt = Ship.Ship("YT-1300", 2, 1, 4, 6)

# Imperial ships
tie = Ship.Ship("TIE", 2, 3, 0, 3)

ar1 = AttackResults.AttackResults(tie, yt)
ar1.focuscombos()
ar2 = AttackResults.AttackResults(yt, tie)
ar2.focuscombos()
