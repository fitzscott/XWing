# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:54:25 2015

@author: bushnelf
"""

import AttackDice
import DefenseDice


class AggDice():
    """
    AggDice - accumulate a set of dice into a two-dimensional
    array, producing a set of potential results for the interaction
    of those dice.
    """

    def __init__(self):
        self.aggddice = []

    def adddie(self, die2add):
        """
        Add a die, die2add, to the set of agg'd dice.

        Paramters
        ---------
        die2add : Dice.Dice

        Returns
        -------
        Nothing
        """

        if len(self.aggddice) == 0:  # this is the 1st die to add
            # print("Adding initial die to AggDice")
            for idx in range(len(die2add.getpips())):
                tmparr = []
                tmparr.append(die2add.getpips()[idx])
                self.aggddice.append(tmparr)
        else:
            # print("Adding subsequent die to AggDice")
            newmat = []
            for matidx in range(len(self.aggddice)):
                tmparr = []
                for nidx in range(len(self.aggddice[matidx])):
                    pip = self.aggddice[matidx][nidx]
                    tmparr.append(pip)
                for idx in range(len(die2add.getpips())):
                    newarr = []
                    for ti in range(len(tmparr)):
                        newarr.append(tmparr[ti])
                    pip = die2add.getpip(idx)
                    # print("Adding new pip " + pip)
                    newarr.append(pip)
                    # print("New arr is " + str(newarr))
                    newmat.append(newarr)
            self.aggddice = newmat

    def counthits(self, attackfocus=False, defensefocus=False, evade=False):
        totalhits = 0
        for matidx in range(len(self.aggddice)):
            rowhits = 0
            for ridx in range(len(self.aggddice[matidx])):
                pip = self.aggddice[matidx][ridx]
                if pip == 'H' or pip == 'C':
                    rowhits += 1
                if pip == 'D':
                    rowhits -= 1
                if attackfocus and pip == 'E':
                    rowhits += 1
                if defensefocus and pip == 'E':
                    rowhits -= 1
            if evade:   # This only happens once per roll
                rowhits -= 1
            if rowhits > 0:    # skip negative - can't have negative hits
                totalhits += rowhits
        return(totalhits)

    def avghits(self, attackfocus=False, defensefocus=False, evade=False):
        totalrolls = len(self.aggddice)
        if (totalrolls > 0):
            return((1.00 * self.counthits(attackfocus, defensefocus, evade)) /
                   (1.00 * totalrolls))
        else:
            return -1

    def countcrits(self, defensefocus=False):
        totalcrits = 0
        for matidx in range(len(self.aggddice)):
            rowcrits = 0
            for ridx in range(len(self.aggddice[matidx])):
                pip = self.aggddice[matidx][ridx]
                if pip == 'C':
                    rowcrits += 1
                if pip == 'D':
                    rowcrits -= 1
                if defensefocus and pip == 'E':
                    rowcrits -= 1
            if rowcrits > 0:    # skip negative - can't have negative crits
                totalcrits += rowcrits
        return(totalcrits)

    def avgcrits(self, defensefocus=False):
        totalrolls = len(self.aggddice)
        if (totalrolls > 0):
            return((1.00 * self.countcrits(defensefocus)) /
                   (1.00 * totalrolls))
        else:
            return -1

    def setupdice(self, attackcount, defensecount):
        self.aggddice = []
        ad = AttackDice.AttackDice()
        ad.addpips()
        dd = DefenseDice.DefenseDice()
        dd.addpips()
        for a in range(attackcount):
            self.adddie(ad)
        for d in range(defensecount):
            self.adddie(dd)

    def prnagg(self):
        print self.aggddice
