# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:37:09 2015

@author: bushnelf
"""

import Dice


class AttackDice(Dice.Dice):
    def __init__(self):
        Dice.Dice.__init__(self)  # clunky as fuck in Python 2
        self.hit = 3
        self.crit = 1
        self.empty = 2
        self.eyeball = 2

    def chancehit(self):
        return((self.hit + self.crit) / self.sides)

    def chanceeyeball(self):
        return(self.eyeball / self.sides)

    def chancehitfocused(self):
        return(self.chancehit() + self.chanceeyeball())

    def addpips(self):
        Dice.Dice.addpips(self, "HHH  CAA")

if __name__ == '__main__':
    ad = AttackDice()
    ad.addpips()
    print("0th pip is " + str(ad.getpip(0)))
