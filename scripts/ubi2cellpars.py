#!/usr/bin/python

"""
Print cell parameters from a ubi file
"""

from ImageD11 import indexing
import sys, numpy, math

def norm2(v): return math.sqrt(numpy.dot(v,v))

def try_to_reduce(u):
    # print "reducing",u
    u = u.copy()
    for i in range(3):
        v = u[i]
        best = norm2(v), v
        # print "i,best",i,best
        for j in range(i+1,3):
            for sign in [1,-1]:
                tv = v + u[j]*sign
                ts = norm2(tv),tv
                # print ts, ts[0],best[0]
                while ts[0] < best[0]:
                    # print "got better"
                    best = ts
                    # print "new best",best
                    tv = ts[1] + u[j]*sign
                    ts = norm2(tv),tv
        u[i] = best[1]
    #print "returning",u
    return u
            


for ubifile in sys.argv[1:]:
    print "Reading",ubifile,
    try:
        ul = indexing.readubis(ubifile)
    except:
        print "error"
        continue
    print 
    for u,i  in zip(ul,range(len(ul))):
        print i, 
        print "%.5f "*6 % indexing.ubitocellpars(u)
        #print u
        red = try_to_reduce(u)
        #print red
        #print u
        if (red != u).any():
            print "Reduced ubi"
            print red
            print "%.5f "*6 % indexing.ubitocellpars(red)
    
