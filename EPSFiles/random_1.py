#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import random,pylab,sys
N,min,max=500,10,20
bins=(max-min)*2
Nums=[]
for i in range(N):
    Nums.append(random.uniform(min,max))
    random.jumpahead(10)
pylab.hist(Nums,bins=bins,facecolor='orange')
pylab.title('Uniform distribution')
pylab.show()
