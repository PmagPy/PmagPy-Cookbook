#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import pylab,random
import numpy
from scipy.stats import gaussian_kde
fakedata=[]
N=100
for i in range(N): fakedata.append(random.gauss(0.,1.))
for i in range(N): fakedata.append(random.gauss(2.,0.8))
pdf=gaussian_kde(fakedata)
x=numpy.linspace(numpy.min(fakedata),numpy.max(fakedata),len(fakedata))
pylab.hist(fakedata,bins=N/5,normed=True)
pylab.plot(x,pdf(x),'r')
pylab.show()
