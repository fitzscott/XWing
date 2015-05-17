# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:28:05 2015

@author: bushnelf
"""

import random


class DiceSimulator:
    """
    DiceSimulator - Instead of calculating the exact probabilities with
        the space of all potential outcomes, generate a ton of random
        checks and see how well they match up.
    """

    def __init__(self, seed=None):
        random.seed(seed)
        self._attk = "HHHC  EE"
        self._dfns = "DDD   EE"
        self._distchk = [0, 0, 0, 0, 0, 0, 0, 0]

    def hitsfromattpip(self, pip, attfocus):
        """
        Return whether a pip indicates 0 or 1 hit
        """

        hits = 0
        if pip == 'H' or pip == 'C':
            hits = 1
        if pip == 'E' and attfocus:
            hits = 1
        return(hits)

    def evadesfromdefpip(self, pip, deffocus):
        """
        Return whether a pip indicates 0 or 1 evades
        """

        evades = 0
        if pip == 'D':
            evades = 1
        if pip == 'E' and deffocus:
            evades = 1
        return(evades)

    def calcattack(self, numatt, numdef, iters=10000, attfocus=False,
                   deffocus=False, targetlock=False, evadetoken=False):
        """
        Run a number of attacks & calculate avg # of hits

        Parameters
        ----------
        numatt : number
            Number of attack dice
        numdef : number
            Number of defense dice
        iters : number
            Iterations to perform

        Returns
        -------
        avgnumhits : number
            Average number of hits
        """

        self._distchk = [0, 0, 0, 0, 0, 0, 0, 0]
        numhits = 0
        divisor = iters
        while iters > 0:
            adjhits = 0
            for a in range(numatt):
                idx = random.randint(0, 7)
                self._distchk[idx] += 1
                pip = self._attk[idx]
                hits = self.hitsfromattpip(pip, attfocus)
                if hits == 0 and targetlock:  # extra chance - roll again
                    idx = random.randint(0, 7)
                    self._distchk[idx] += 1
                    pip = self._attk[idx]
                    hits = self.hitsfromattpip(pip, attfocus)
                adjhits += hits

            for d in range(numdef):
                idx = random.randint(0, 7)
                self._distchk[idx] += 1
                pip = self._dfns[idx]
                adjhits -= self.evadesfromdefpip(pip, deffocus)
            if evadetoken:
                adjhits -= 1

            if adjhits > 0:
                numhits += adjhits

            iters -= 1
        avgnumhits = 1.0 * numhits / (1.0 * divisor)
        # print("Number of total hits: " + str(numhits))
        # print("Average number of hits: " + str(avgnumhits))
        return(avgnumhits)

    def calcroundsreqd(self, numatt, numdef, hitsreqd, iters=10000,
                       attfocus=False, deffocus=False, targetlock=False,
                       evadetoken=False):
        avgnumhits = self.calcattack(numatt, numdef, iters, attfocus,
                                     deffocus, targetlock, evadetoken)
        return(1.0 * hitsreqd / avgnumhits)

    def showdistribution(self):
        print(self._distchk)

if __name__ == '__main__':
    ds = DiceSimulator()
    roundsreqd = ds.calcroundsreqd(3, 3, 3)
    print("Would require " + str(roundsreqd) + " rounds on average")
