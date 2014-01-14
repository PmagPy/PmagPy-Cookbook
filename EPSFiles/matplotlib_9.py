#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import pylab,numpy
from mpl_toolkits.mplot3d import axes3d
def g(X,Y):
    G=6.67e-11 # grav constant in Nm^2/kg^2 (SI)
    R=2. # radius in meters
    drho=500 # density contrast in kg/m^3
    h=numpy.sqrt(X**2+Y**2)
    return 1e8*(G*4.*numpy.pi*R**3.*drho)/(3.*(h**2+z**2))
z=3. # depth of burial
x=numpy.arange(-2.*z,2.*z,0.1)
y=numpy.arange(-2.*z,2.*z,0.1)
X,Y=pylab.meshgrid(x,y)
grav=g(X,Y)
fig=pylab.figure()
ax=axes3d.Axes3D(fig)

ax.plot_surface(X,Y,grav)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
pylab.show()
