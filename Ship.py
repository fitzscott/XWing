# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:16:21 2015

@author: bushnelf
"""

import AggDice


class Ship:
    """
    Base class for different ship types
    """

    def __init__(self, nam, att, dfns, shld, hul):
        self._name = nam
        self._attack = att
        self._defense = dfns
        self._shields = shld
        self._hull = hul

    @property
    def name(self):
        return(self._name)

    @property
    def attack(self):
        return(self._attack)

    @property
    def defense(self):
        return(self._defense)

    @property
    def shields(self):
        return(self._shields)

    @property
    def hits(self):
        return(self._shields + self._hull)

    def attacktarget(self, targetship, closerange=False, longrange=False,
                     evade=False):
        ag = AggDice.AggDice()

        if closerange:
            attadd = 1
        else:
            attadd = 0
        if longrange:
            defadd = 1
        else:
            defadd = 0

        ag.setupdice(self.attack + attadd, targetship.defense + defadd)

        hitsreqd = targetship.hits
        avgrndsnorm = hitsreqd / ag.avghits()
        avgrndsattfoc = hitsreqd / ag.avghits(True, False)
        avgrndsdeffoc = hitsreqd / ag.avghits(False, True)
        if evade:
            avghits = ag.avghits(False, False, True)
            if avghits > 0:
                avgrndsdefevade = hitsreqd / avghits
            else:
                avgrndsdefevade = -1
            avghitsattfoc = ag.avghits(True, False, True)
            if avghitsattfoc > 0:
                avgrndsdefevadeattfoc = hitsreqd / avghitsattfoc
            else:
                avgrndsdefevadeattfoc = -1
        attdicedpr = targetship.attack / avgrndsnorm
        avgrndstillcrits = targetship.shields / ag.avghits()

        print(self.name + " attacking " + targetship.name + ":")
        print("Avg rounds no focus to destroy: " + str(avgrndsnorm))
        print("Avg rounds attack focus to destroy: " + str(avgrndsattfoc))
        print("Avg rounds defense focus to destroy: " + str(avgrndsdeffoc))
        if evade:
            print("Avg rounds defense evade to destroy: " +
                  str(avgrndsdefevade))
            print("Avg rounds attack focus + defense evade to destroy: " +
                  str(avgrndsdefevadeattfoc))
        print("Avg rounds before crits: " + str(avgrndstillcrits))
        print("Attack dice destroyed per round: " + str(attdicedpr))

if __name__ == '__main__':
    xw = Ship("X-Wing", 3, 2, 2, 3)
    print(xw.name + " can take " + str(xw.hits) + " hits.")
