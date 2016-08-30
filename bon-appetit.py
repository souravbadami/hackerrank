#!usr/bin/env python
from __future__ import print_function
from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *

def main():
    n,k=map(int,raw_input().split())
    c=map(int,raw_input().split())
    b=int(raw_input())
    s=sum(c)-c[k]
    if s/2 == b:
        print("Bon Appetit")
    else:
        print(b-(s/2))

if __name__=='__main__':
	main()
