#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import random,pylab
N,mu,sigma=500,10,2
Nums=[]
for i in range(N):
    Nums.append(random.gauss(mu,sigma))
    random.jumpahead(10)
pylab.hist(Nums,bins=20,facecolor='orange')
pylab.title('Normal distribution')
pylab.show()
