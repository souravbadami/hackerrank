#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    word_map = dict()
    for word in magazine:
        try:
            word_map[word] += 1
        except:
            word_map[word] = 1
    for word in note:
        try:
            if word_map[word] == 0:
                print("No")
                return
            else:
                word_map[word] -= 1
        except:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
