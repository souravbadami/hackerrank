#!usr/bin/env python
from __future__ import print_function
from __future__ import division
from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *
from random import *

def main():
    cases=int(raw_input())
    for i in xrange(cases):
        l = int(raw_input())
        _list = map(int,raw_input().strip().split())
        print(maxContiguous(_list),maxNonContigous(_list),sep=" ",end="\n")
        
def maxContiguous(_list):
    if max(_list)<0:
        return max(_list)
    else:
        overallMax = 0
        maxToPoint = 0
        for i in _list:
            maxToPoint = maxToPoint + i
            if maxToPoint < 0:
                maxToPoint = 0
            if overallMax < maxToPoint:
                overallMax = maxToPoint
        return overallMax


def maxNonContigous(_list):
    if max(_list)<0:
        return max(_list)
    else:
        return sum([i for i in _list if i>0])


if __name__=='__main__':
    main()
