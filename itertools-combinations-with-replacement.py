#!/usr/bin/env python
from __future__ import print_function
import itertools
a,b=map(str,raw_input().split())
_list=list(a)
_list=list(itertools.combinations_with_replacement(_list,int(b)))
for i in xrange(len(_list)):
    _list[i]=sorted(_list[i])
_list=sorted(_list)
for i in xrange(len(_list)):
    for j in xrange(len(_list[i])):
        print(_list[i][j],sep="",end="")
    print()