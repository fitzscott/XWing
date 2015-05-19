# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:42:36 2015

@author: bushnelf
"""

import Dice


class DefenseDice(Dice.Dice):
    def __init__(self):
        Dice.Dice.__init__(self)  # clunky as fuck in Python 2
        # print("In DefenseDice __init__")
        self.dodge = 3
        self.empty = 3
        self.eyeball = 2

    def chancedodge(self):
        return((self.dodge + self.crit) / self.sides)

    def chanceeyeball(self):
        return(self.eyeball / self.sides)

    def chancedodgefocused(self):
        return(self.chancedodge() + self.chanceeyeball())

    def addpips(self):
        # print("Adding pips to Defense")
        Dice.Dice.addpips(self, "DDD   EE")

if __name__ == '__main__':
    dd = DefenseDice()
    dd.addpips()
    print("0th pip is " + str(dd.getpip(0)))
