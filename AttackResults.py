# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 07:44:42 2015

@author: bushnelf
"""

import Ship
import AttackResult


class AttackResults:
    """
    Saved results of calculations for one ship attacking another
    and vice versa.
    """

    def __init__(self, attship, defship):
        self._attacker = attship
        self._defender = defship

    def allranges(self, attkr, dfndr, attfocus=False,
                  deffocus=False, evade=False):
        """
        Compare results for attacker & defender at all ranges
        """

        rslts = []
        for rng2tgt in range(3):
            rslts.append(AttackResult.AttackResult(attkr, dfndr,
                                                   rng2tgt+1, attfocus,
                                                   deffocus, evade))
            rslts[rng2tgt].calcresults()
        return rslts

    def ratios(self, r1, r2):
        for rng2tgt in range(3):
            print("Range: " + str(rng2tgt+1))
            print("Avg rounds for " + self._attacker.name + " to destroy " +
                  self._defender.name + ": " + str(r1[rng2tgt].avgrnds))
            print("Avg rounds for " + self._defender.name + " to destroy " +
                  self._attacker.name + ": " + str(r2[rng2tgt].avgrnds))
            print("Rounds to destroy ratio (" + self._attacker.name +
                  " : " + self._defender.name + "): " +
                  str(r1[rng2tgt].avgrnds / r2[rng2tgt].avgrnds))

    def focuscombos(self):
        # none
        print("Focus:  None")
        r0_1a = self.allranges(self._attacker, self._defender)
        r0_1d = self.allranges(self._defender, self._attacker)
        self.ratios(r0_1a, r0_1d)
        # attack / attack
        print("Focus:  Attack / Attack")
        r0_1a = self.allranges(self._attacker, self._defender, attfocus=True)
        r0_1d = self.allranges(self._defender, self._attacker, attfocus=True)
        self.ratios(r0_1a, r0_1d)
        # attack / defense
        print("Focus:  Attack / Defense")
        r0_1a = self.allranges(self._attacker, self._defender, attfocus=True,
                               deffocus=True)
        r0_1d = self.allranges(self._defender, self._attacker)
        self.ratios(r0_1a, r0_1d)
        # defense / defense
        print("Focus:  Defense / Defense")
        r0_1a = self.allranges(self._attacker, self._defender, deffocus=True)
        r0_1d = self.allranges(self._defender, self._attacker, deffocus=True)
        self.ratios(r0_1a, r0_1d)
        # defense / attack
        print("Focus:  Defense / Attack")
        r0_1a = self.allranges(self._attacker, self._defender)
        r0_1d = self.allranges(self._defender, self._attacker, attfocus=True,
                               deffocus=True)
        self.ratios(r0_1a, r0_1d)

if __name__ == '__main__':
    print("Not sure what we're doing in AttackResults yet")
