#!usr/bin/env python
from __future__ import print_function
from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *

def main():
	_list=set(map(int,raw_input().split()))
	cases=int(raw_input())
	for i in xrange(cases):
	    _sublist=set(map(int,raw_input().split()))
	    eval= _sublist.issubset(_list)
	    if(eval==False):
	        print eval
	        break
	if(eval==True):
	    print eval

if __name__ == '__main__':
	main()