#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import pylab
import numpy as np
def f(t):
    return np.exp(-t)*np.cos(2.*np.pi*t)
t1=np.arange(0.,5.,0.1)
t2=np.arange(0.,5.,0.02)
fig=pylab.figure(1,(7,5)) # creates a figure
fig.add_subplot(211) # makes a subplot 
pylab.plot(t1,f(t1),'bo') # makes blue dots
pylab.plot(t1,f(t1),'k-') # makes black line
fig.add_subplot(212) # makes 2nd subplot 
pylab.plot(t2,np.cos(2*np.pi*t2),'r--') # red dashed 
pylab.xlabel('Time (ms)') # x-label
pylab.show()
