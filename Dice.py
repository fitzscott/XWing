# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:33:57 2015

@author: bushnelf
"""


class Dice:
    def __init__(self):
        self.sides = 8
        # self.pips = []
        self.pips = ""
        # print("In Dice __init__")

    def sides(self):
        return(self.sides)

    def addpip(self, pip2add):
        self.pips.append(pip2add)

    def addpips(self, pipsasstr):
        self.pips = pipsasstr

    def getpip(self, idx):
        return self.pips[idx]

    def getpips(self):
        return self.pips

if __name__ == '__main__':
    d = Dice()
    d.addpip('X')
    print("0th pip is " + str(d.getpip(0)))
