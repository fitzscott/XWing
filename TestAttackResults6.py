# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:50:49 2015

@author: bushnelf
"""

import Ship
import AttackResults

# Scum ships
z95 = Ship.Ship("Z-95", 2, 2, 2, 2)
m3a = Ship.Ship("Scyk", 2, 3, 2, 1)
hwk = Ship.Ship("HWK-290", 1, 2, 4, 1)
fs = Ship.Ship("Firespray-31", 3, 2, 6, 4)

# Imperial ships
tie = Ship.Ship("TIE", 2, 3, 3, 0)
advtie = Ship.Ship("Adv TIE", 2, 3, 3, 2)
tieint = Ship.Ship("Tie Interceptor", 3, 3, 3, 0)
deftie = Ship.Ship("TIE Defender", 3, 3, 3, 3)
phantie = Ship.Ship("TIE Phantom", 4, 2, 2, 2)

ar = AttackResults.AttackResults(z95, tie)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, tie)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, tie)
ar.focuscombos()
ar = AttackResults.AttackResults(fs, tie)
ar.focuscombos()

ar = AttackResults.AttackResults(z95, advtie)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, advtie)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, advtie)
ar.focuscombos()
ar = AttackResults.AttackResults(fs, advtie)
ar.focuscombos()

ar = AttackResults.AttackResults(z95, tieint)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, tieint)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, tieint)
ar.focuscombos()
ar = AttackResults.AttackResults(fs, tieint)
ar.focuscombos()

ar = AttackResults.AttackResults(z95, deftie)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, deftie)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, deftie)
ar.focuscombos()
# this one has trouble on the old machine
#ar = AttackResults.AttackResults(fs, deftie)
#ar.focuscombos()

ar = AttackResults.AttackResults(z95, phantie)
ar.focuscombos()
ar = AttackResults.AttackResults(m3a, phantie)
ar.focuscombos()
ar = AttackResults.AttackResults(hwk, phantie)
ar.focuscombos()
# this one probabably will, too, but it's last
ar = AttackResults.AttackResults(fs, phantie)
ar.focuscombos()

