#!/usr/bin/env python
from __future__ import print_function
from itertools import permutations
#import os
_str,pl=map(str,raw_input().split())
_str2=list(permutations(_str,int(pl)))
_str2.sort()
for i in xrange(len(_str2)):
    for j in xrange(len(_str2[i])):
        print(_str2[i][j],sep="",end="")
    print()