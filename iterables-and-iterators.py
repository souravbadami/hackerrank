#!usr/bin/env python
from __future__ import print_function
from __future__ import division
import itertools
l=int(raw_input())
_list=map(str,raw_input().split())
k=int(raw_input())
_list=list(itertools.combinations(_list,k))
total_com=len(_list)
com=0
for i in xrange(len(_list)):
    if('a' in _list[i]):
        com+=1
print (com/total_com)