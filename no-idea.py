#!usr/bin/env python
from __future__ import print_function

def main():
    raw_input()
    X=[int(e) for e in raw_input().split()]
    A={int(e) for e in raw_input().split()}
    B={int(e) for e in raw_input().split()}
    r=0
    for e in X:
    	r+=(e in A)-(e in B)
    print(r)

if __name__ == '__main__':
    main()