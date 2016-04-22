# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:16:21 2015

@author: bushnelf
"""

import Ship


class SplitRangeShip(Ship.Ship):
    """
    Special ship with split attack values based on range
    """

    def __init__(self, nam, att, dfns, hul, shld, splt=3):
        Ship.Ship.__init__(self, nam, att, dfns, hul, shld)
        self._split = []
        self._splitval = splt

    def addsplit(self, att):
        self._split.append(att)

    def attackatcurrentrange(self, closerange, longrange):
        if (longrange and self._splitval == 3) \
            or (not closerange and self._splitval == 2):
            attval = self._split[1]
            #print("Setting attack to split 1 = " + str(self._split[1]))
        else:
            attval = self._split[0]
        if closerange:
            attadd = 1
        else:
            attadd = 0
	return attval + attadd

    def attack(self, closerange=False, longrange=False):
        return(self.attackatcurrentrange(closerange, longrange))

if __name__ == '__main__':
    hwk = SplitRangeShip("HWK-290", 1, 2, 4, 1, 3)
    hwk.addsplit(3)
    hwk.addsplit(1)
    print(hwk.name + " can take " + str(hwk.hits) + " hits.")
    print(hwk.name + " has split at range " + str(hwk._splitval)+ ".")
