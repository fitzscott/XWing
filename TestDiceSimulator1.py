# -*- coding: utf-8 -*-
"""
Created on Sat May 9 12:18:44 2015

@author: bushnelf
"""

import DiceSimulator

times2run = 10000000

ds = DiceSimulator.DiceSimulator()

print("X-Wing attacking TIE:")
print("Avg rounds no focus to destroy: " +
      str(ds.calcroundsreqd(3, 3, 3, iters=times2run)))
print("Avg rounds attack focus to destroy: " +
      str(ds.calcroundsreqd(3, 3, 3, iters=times2run, attfocus=True)))
print("Avg rounds defense focus to destroy: " +
      str(ds.calcroundsreqd(3, 3, 3, iters=times2run, deffocus=True)))
print("Avg rounds defense evade to destroy: " +
      str(ds.calcroundsreqd(3, 3, 3, iters=times2run, evadetoken=True)))
print("Avg rounds attack focus + defense evade to destroy: " +
      str(ds.calcroundsreqd(3, 3, 3, iters=times2run, attfocus=True,
                            evadetoken=True)))
print("Avg rounds target lock to destroy: " +
      str(ds.calcroundsreqd(3, 3, 3, iters=times2run, targetlock=True)))
print("Avg rounds attack focus + target lock to destroy: " +
      str(ds.calcroundsreqd(3, 3, 3, iters=times2run, attfocus=True,
                            targetlock=True)))
print("------------------------------------")
# ds.showdistribution()

print("Y-Wing attacking TIE:")
print("Avg rounds no focus to destroy: " +
      str(ds.calcroundsreqd(2, 3, 3, iters=times2run)))
print("Avg rounds attack focus to destroy: " +
      str(ds.calcroundsreqd(2, 3, 3, iters=times2run, attfocus=True)))
print("Avg rounds defense focus to destroy: " +
      str(ds.calcroundsreqd(2, 3, 3, iters=times2run, deffocus=True)))
print("Avg rounds defense evade to destroy: " +
      str(ds.calcroundsreqd(2, 3, 3, iters=times2run, evadetoken=True)))
print("Avg rounds attack focus + defense evade to destroy: " +
      str(ds.calcroundsreqd(2, 3, 3, iters=times2run, attfocus=True,
                            evadetoken=True)))
print("Avg rounds target lock to destroy: " +
      str(ds.calcroundsreqd(2, 3, 3, iters=times2run, targetlock=True)))
print("Avg rounds attack focus + target lock to destroy: " +
      str(ds.calcroundsreqd(2, 3, 3, iters=times2run, attfocus=True,
                            targetlock=True)))
print("------------------------------------")
# ds.showdistribution()

print("TIE attacking X-Wing:")
print("Avg rounds no focus to destroy: " +
      str(ds.calcroundsreqd(2, 2, 5, iters=times2run)))
print("Avg rounds attack focus to destroy: " +
      str(ds.calcroundsreqd(2, 2, 5, iters=times2run, attfocus=True)))
print("Avg rounds defense focus to destroy: " +
      str(ds.calcroundsreqd(2, 2, 5, iters=times2run, deffocus=True)))
print("------------------------------------")
# ds.showdistribution()

print("TIE attacking Y-Wing:")
print("Avg rounds no focus to destroy: " +
      str(ds.calcroundsreqd(2, 1, 8, iters=times2run)))
print("Avg rounds attack focus to destroy: " +
      str(ds.calcroundsreqd(2, 1, 8, iters=times2run, attfocus=True)))
print("Avg rounds defense focus to destroy: " +
      str(ds.calcroundsreqd(2, 1, 8, iters=times2run, deffocus=True)))
print("------------------------------------")
# ds.showdistribution()

print("TIE attacking A-Wing:")
print("Avg rounds no focus to destroy: " +
      str(ds.calcroundsreqd(2, 3, 4, iters=times2run)))
print("Avg rounds attack focus to destroy: " +
      str(ds.calcroundsreqd(2, 3, 4, iters=times2run, attfocus=True)))
print("Avg rounds defense focus to destroy: " +
      str(ds.calcroundsreqd(2, 3, 4, iters=times2run, deffocus=True)))
print("------------------------------------")
# ds.showdistribution()
