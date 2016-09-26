#!usr/bin/env python
from __future__ import print_function

def main():
    n = int(raw_input().strip())
    c = map(int,raw_input().strip().split(' '))
    pairs = 0
    c.sort()
    c.append('-1')
    i = 0
    while i<n:
        if c[i]==c[i+1]:
            pairs = pairs+1
            i+=2
        else:
            i+=1
    print(pairs)
    
if __name__ == '__main__':
    main()