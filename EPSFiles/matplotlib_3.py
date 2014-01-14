#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import pylab,numpy
x=numpy.arange(0.,5.,0.2)
y=x**3
fig=pylab.plot(x,y)
pylab.setp(fig, color='r', linewidth=2.0)
pylab.show()
