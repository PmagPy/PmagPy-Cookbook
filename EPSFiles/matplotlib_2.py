#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import pylab,numpy
t=numpy.arange(0.,5.,0.2)
pylab.plot(t,t,'r--',t,\
    t**2,'bs',t,t**3,'g^')
pylab.legend(['linear','quadratic','cubic'],'upper left')
pylab.annotate('nice curve', xy=(2.9,32),xytext=(1,40),
    arrowprops=dict(facecolor='black',shrink=0.05))
pylab.xlabel('some numbers')
pylab.title('Pretty plot')
pylab.text(2,80,r'diamonds: $y=x^3$')
pylab.show()
