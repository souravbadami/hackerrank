#!usr/bin/env python
from __future__ import print_function
from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *

def isStrFunny(st):
    s_len = len(st)
    idx = 0
    while idx < s_len//2:
        left_diff = abs(ord(st[idx]) - ord(st[idx+1]))
        right_diff = abs(ord(st[s_len-idx-1]) - ord(st[s_len-idx-2]))
        if left_diff != right_diff:
            return False
        idx += 1
     
    return True
     
 
if __name__ == '__main__':
    t = input()
    for _ in range(t):
        st = raw_input()
        if isStrFunny(st):
            print("Funny")
        else:
            print("Not Funny")
