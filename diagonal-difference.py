#!usr/bin/env python
from __future__ import print_function
from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *
 
def getDiagonalDifference(var):
    diff = 0
    v_len = len(var)
    for idx in xrange(v_len):
        diff += var[idx][idx]
        diff -= var[idx][v_len-idx-1]
 
    return abs(diff)    
         
if __name__ == '__main__':
    t = input()
    var = []
    for _ in xrange(t):
        e = map(int, raw_input().split())
        var.append(e)
         
    print(getDiagonalDifference(var))
