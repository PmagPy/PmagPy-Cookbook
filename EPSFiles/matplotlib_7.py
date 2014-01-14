#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import pylab,numpy
input=open('eqs7day-M1.txt','rU').readlines()
keys=input[0].split('\t')
Mags,Fracs,Labels=[],[],[]
for line in input[1:]:
    D={}
    rec=line.split('\t')
    for col in range(len(keys)):
        D[keys[col]]=rec[col]
    Mags.append(float(D['Magnitude']))
bin0=1
for m in range(2,7):
    num=0
    for eqm in Mags:
        if eqm<m and eqm>bin0:
            num+=1
    Fracs.append(float(num))
    Labels.append(str(bin0)+'-'+str(m))
    print m,Fracs[-1]
    bin0+=1
pylab.pie(Fracs,labels=Labels)
pylab.axis('equal')
pylab.show()     
