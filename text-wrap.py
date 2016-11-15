#!usr/bin/env python
from __future__ import print_function
import textwrap

def main():
  sen=raw_input()
  wl=int(raw_input())
  print(textwrap.fill(sen,wl))

if __name__ == '__main__':
  main()
