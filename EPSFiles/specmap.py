#!/usr/bin/env python
import matplotlib; matplotlib.use("TkAgg")
import pylab,numpy
data=open('SPECMAP.dat','rU').readlines()
o18,age=[],[]
for line in data:
   rec=line.split()
   age.append(float(rec[0])) 
   o18.append(float(rec[1])) 
pylab.plot(age,o18,'k',age,o18,'ro')
#bounds=pylab.axis([age[0],age[-1],numpy.max(o18)+.1,numpy.min(o18)-.1])
pylab.show()
