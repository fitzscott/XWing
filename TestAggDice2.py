# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:10:38 2015

@author: bushnelf
"""


import AggDice

agg = AggDice.AggDice()

print("1 attack die vs. 1 defense die")
agg.setupdice(2, 1)
print("Avg hits = " + str(agg.avghits()))
print("Avg hits attack focused = " + str(agg.avghits(True, False)))
print("Avg hits defense focused = " + str(agg.avghits(False, True)))
print("Avg hits both focused = " + str(agg.avghits(True, True)))
print("Avg crits = " + str(agg.avgcrits()))
print("Avg crits defense focused = " + str(agg.avgcrits(True)))
print("")

print("2 attack dice vs. 1 defense die")
agg.setupdice(2, 1)
print("Avg hits = " + str(agg.avghits()))
print("Avg hits attack focused = " + str(agg.avghits(True, False)))
print("Avg hits defense focused = " + str(agg.avghits(False, True)))
print("Avg hits both focused = " + str(agg.avghits(True, True)))
print("Avg crits = " + str(agg.avgcrits()))
print("Avg crits defense focused = " + str(agg.avgcrits(True)))
print("")

print("1 attack die vs. 2 defense dice")
agg.setupdice(1, 2)
print("Avg hits = " + str(agg.avghits()))
print("Avg hits attack focused = " + str(agg.avghits(True, False)))
print("Avg hits defense focused = " + str(agg.avghits(False, True)))
print("Avg hits both focused = " + str(agg.avghits(True, True)))
print("Avg crits = " + str(agg.avgcrits()))
print("Avg crits defense focused = " + str(agg.avgcrits(True)))
print("")

print("2 attack dice vs. 2 defense dice")
agg.setupdice(2, 2)
print("Avg hits = " + str(agg.avghits()))
print("Avg hits attack focused = " + str(agg.avghits(True, False)))
print("Avg hits defense focused = " + str(agg.avghits(False, True)))
print("Avg hits both focused = " + str(agg.avghits(True, True)))
print("Avg crits = " + str(agg.avgcrits()))
print("Avg crits defense focused = " + str(agg.avgcrits(True)))
print("")

print("2 attack dice vs. 3 defense dice")
agg.setupdice(2, 3)
print("Avg hits = " + str(agg.avghits()))
print("Avg hits attack focused = " + str(agg.avghits(True, False)))
print("Avg hits defense focused = " + str(agg.avghits(False, True)))
print("Avg hits both focused = " + str(agg.avghits(True, True)))
print("Avg crits = " + str(agg.avgcrits()))
print("Avg crits defense focused = " + str(agg.avgcrits(True)))
print("")

print("3 attack dice vs. 2 defense dice")
agg.setupdice(3, 2)
print("Avg hits = " + str(agg.avghits()))
print("Avg hits attack focused = " + str(agg.avghits(True, False)))
print("Avg hits defense focused = " + str(agg.avghits(False, True)))
print("Avg hits both focused = " + str(agg.avghits(True, True)))
print("Avg crits = " + str(agg.avgcrits()))
print("Avg crits defense focused = " + str(agg.avgcrits(True)))
print("")

print("3 attack dice vs. 3 defense dice")
agg.setupdice(3, 3)
print("Avg hits = " + str(agg.avghits()))
print("Avg hits attack focused = " + str(agg.avghits(True, False)))
print("Avg hits defense focused = " + str(agg.avghits(False, True)))
print("Avg hits both focused = " + str(agg.avghits(True, True)))
print("Avg crits = " + str(agg.avgcrits()))
print("Avg crits defense focused = " + str(agg.avgcrits(True)))
print("")

print("3 attack dice vs. 4 defense dice")
agg.setupdice(3, 4)
print("Avg hits = " + str(agg.avghits()))
print("Avg hits attack focused = " + str(agg.avghits(True, False)))
print("Avg hits defense focused = " + str(agg.avghits(False, True)))
print("Avg hits both focused = " + str(agg.avghits(True, True)))
print("Avg crits = " + str(agg.avgcrits()))
print("Avg crits defense focused = " + str(agg.avgcrits(True)))
print("")

print("4 attack dice vs. 3 defense dice")
agg.setupdice(4, 3)
print("Avg hits = " + str(agg.avghits()))
print("Avg hits attack focused = " + str(agg.avghits(True, False)))
print("Avg hits defense focused = " + str(agg.avghits(False, True)))
print("Avg hits both focused = " + str(agg.avghits(True, True)))
print("Avg crits = " + str(agg.avgcrits()))
print("Avg crits defense focused = " + str(agg.avgcrits(True)))
print("")

print("4 attack dice vs. 2 defense dice")
agg.setupdice(4, 2)
print("Avg hits = " + str(agg.avghits()))
print("Avg hits attack focused = " + str(agg.avghits(True, False)))
print("Avg hits defense focused = " + str(agg.avghits(False, True)))
print("Avg hits both focused = " + str(agg.avghits(True, True)))
print("Avg crits = " + str(agg.avgcrits()))
print("Avg crits defense focused = " + str(agg.avgcrits(True)))
print("")