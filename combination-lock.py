#!usr/bin/env python
from __future__ import print_function
from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *

def main():
    c1=map(int,raw_input().split())
    c2=map(int,raw_input().split())
    operations=0
    for i in xrange(len(c1)):
        if c1[i]==c2[i]:
            continue
        ma=max(c1[i],c2[i])
        mi=min(c1[i],c2[i])
        operations+=min((ma-mi),(10+mi-ma))
    print(operations) 

if __name__=='__main__':
	main()
