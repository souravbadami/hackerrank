#!usr/bin/env python
import re

def main():
	pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
	num=int(raw_input())
	email=list()
	for i in xrange(num):
    		email.append(raw_input())
	valid=list()
	for i in email:
    		if(re.match(pattern,i)):
        		valid.append(i)
	print sorted(valid)

if __name__ == '__main__':
	main()
