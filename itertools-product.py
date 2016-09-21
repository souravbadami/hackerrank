#!usr/bin/env python
from __future__ import print_function
from itertools import product
a=map(int,raw_input().split())
b=map(int,raw_input().split())
_list=list(product(a,b))
for i in xrange(len(_list)):
    print(_list[i],sep="",end=" ")