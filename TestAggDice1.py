# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:08:11 2015

@author: bushnelf

Preliminary test of AggDice
"""


import AggDice
import AttackDice
import DefenseDice

ad = AttackDice.AttackDice()
ad.addpips()
dd = DefenseDice.DefenseDice()
dd.addpips()
agg = AggDice.AggDice()
agg.adddie(ad)
agg.prnagg()
print("Hits = " + str(agg.counthits()))
agg.adddie(dd)
agg.prnagg()
print("Hits = " + str(agg.counthits()))
print("Hits attack focused = " + str(agg.counthits(True, False)))
print("Hits defense focused = " + str(agg.counthits(False, True)))
print("Hits both focused = " + str(agg.counthits(True, True)))
agg.adddie(dd)
agg.prnagg()
print("Hits = " + str(agg.counthits()))
