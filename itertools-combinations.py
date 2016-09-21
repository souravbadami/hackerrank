#!/usr/bin/env python
from __future__ import print_function
import itertools,sys
a,b=map(str,raw_input().split())
_list=sorted(list(a))
for i in xrange(1,int(b)+1):
    _modlist=list(itertools.combinations(_list,i))
    _modlist.sort()
    for j in xrange(len(_modlist)):
        for k in xrange(len(_modlist[j])):
            print(_modlist[j][k],sep="",end="")
        print()