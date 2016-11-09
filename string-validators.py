#!usr/bin/env python

def main():
    word=raw_input()
    wl=list(word)
    ct=0
    for i in xrange(len(wl)):
        if(wl[i].isalnum()):
            print "True"
            break
        else:
            ct+=1
    if(ct==len(wl)):
        print "False"
    ct=0
    for i in xrange(len(wl)):
        if(wl[i].isalpha()):
            print "True"
            break
        else:
            ct+=1
    if(ct==len(wl)):
        print "False"
    ct=0
    for i in xrange(len(wl)):
        if(wl[i].isdigit()):
            print "True"
            break
        else:
            ct+=1
    if(ct==len(wl)):
        print "False"
    ct=0
    for i in xrange(len(wl)):
        if(wl[i].islower()):
            print "True"
            break
        else:
            ct+=1
    if(ct==len(wl)):
        print "False"
    ct=0
    for i in xrange(len(wl)):
        if(wl[i].isupper()):
            print "True"
            break
        else:
            ct+=1
    if(ct==len(wl)):
        print "False"

if __name__ == '__main__':
    main()