#!/usr/bin/env python
import matplotlib; matplotlib.use("TkAgg")
import random,math,numpy,pylab
from scipy.interpolate import interp1d,splrep, splev
cycles,d,xinc,Xs,Ys,Y=10,.1,.2,[],[],[]
Xlin=numpy.linspace(0,cycles*math.pi,)
for x in Xlin:
    Xs.append(x+random.gauss(0,d))
    Ys.append(math.sin(Xs[-1])+random.gauss(0,d))
    Y.append(math.sin(Xs[-1]))
fig=pylab.figure(1,(8,3))
pylab.plot(Xlin,Y,'k') #plot the data
pylab.plot(Xs,Ys,'g^') #plot the data
Xnew = numpy.arange(numpy.min(Xs),numpy.max(Xs),xinc)
S=splrep(Xs,Ys) #spline representation
Yspl=splev(Xnew,S) # evaluate the spline
#L=interp1d(Xs,Ys) # linear interpolation
#Ylin=L(Xnew)
pylab.plot(Xnew,Yspl,'r')
pylab.plot(Xnew,Yspl,'r+')
#pylab.plot(Xnew,Ylin,'c')
#pylab.plot(Xnew,Ylin,'c+')
pylab.show()

