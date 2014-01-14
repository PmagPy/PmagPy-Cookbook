#!/usr/bin/env python
import pmag
dat=open('princ.di','rU').readlines()
x,y,z=[],[],[]
Dirs=[]
for line in dat:
    rec=line.split()
    Dirs=[float(rec[0]),float(rec[1]),float(rec[2])*1e-4]
    cart=pmag.dir2cart(Dirs)
    x.append(cart[0])
    y.append(cart[1]*1.1)
    z.append(cart[2])
from enthought.mayavi.mlab import points3d,savefig,show,outline,plot3d
from numpy import array,sum,transpose
from numpy.linalg import eig
X,Y,Z=array(x),array(y),array(z)
points3d(X,Y,Z,color=(0,0,0),scale_factor=0.25,opacity=.5)
outline(color=(.7,0,0))
T=array([[sum(X*X),sum(X*Y),sum(X*Z)],
   [sum(Y*X),sum(Y*Y),sum(Y*Z)],
   [sum(Z*X),sum(Z*Y),sum(Z*Z)]])
vals,vects=eig(T)
pv=transpose(vects)[0]*3.
plot3d([pv[0],-pv[0]],[pv[1],-pv[1]],[pv[2],-pv[2]],tube_radius=0.1,color=(0,1,0))
show()

