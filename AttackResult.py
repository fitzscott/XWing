# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 08:48:31 2015

@author: bushnelf
"""

import AggDice
import Ship


class AttackResult:
    """
    Single set of attributes for an attack:
    Ships, dice, range, foci, evade
    """

    def __init__(self, attship, defship, range2tgt, attfoc, deffoc, evade):
        self._attacker = attship
        self._defender = defship
        self._rangetotarget = range2tgt
        self._attackfocus = attfoc
        self._defensefocus = deffoc
        self._defenseevade = evade
        self._avghits = 0
        self._avgrnds = 0
        self._avgrndstillcrit = 0

    @property
    def attacker(self):
        return self._attacker

    @attacker.setter
    def attacker(self, ship):
        self._attacker = ship

    @property
    def defender(self):
        return self._attacker

    @defender.setter
    def defender(self, ship):
        self._defender = ship

    @property
    def rangetotarget(self):
        return self._rangetotarget

    @rangetotarget.setter
    def rangetotarget(self, rng):
        self._rangetotarget = rng

    @property
    def closerange(self):
        return(self.rangetotarget == 1)

    @property
    def longrange(self):
        return(self.rangetotarget == 3)

    @property
    def attackfocus(self):
        return self._attackfocus

    @attackfocus.setter
    def attackfocus(self, foc):
        self._attackfocus = foc

    @property
    def defensefocus(self):
        return self._defensefocus

    @defensefocus.setter
    def defensefocus(self, foc):
        self._defensefocus = foc

    @property
    def defenseevade(self):
        return self._defenseevade

    @defenseevade.setter
    def defenseevade(self, evade):
        self._defenseevade = evade

    @property
    def avghits(self):
        return self._avghits

    @avghits.setter
    def avghits(self, ht):
        self._avghits = ht

    @property
    def avgrnds(self):
        return self._avgrnds

    @avgrnds.setter
    def avgrnds(self, rnds):
        self._avgrnds = rnds

    @property
    def avgrndstillcrit(self):
        return self._avgrndstillcrit

    @avgrndstillcrit.setter
    def avgrndstillcrit(self, rnds):
        self._avgrndstillcrit = rnds

    def calcresults(self):
        ag = AggDice.AggDice()

        if self.rangetotarget == 3:
            defadd = 1
        else:
            defadd = 0

        ag.setupdice(self._attacker.attack(self.closerange, self.longrange), \
                     self._defender.defense + defadd)

        hitsreqd = self._defender.hits
        self.avghits = ag.avghits(self.attackfocus, self.defensefocus,
                                  self.defenseevade)
        self.avgrnds = hitsreqd / self.avghits
        # attdicedpr = self._defender.attack / avgrnds
        self.avgrndstillcrit = self._defender.shields / self.avghits
