#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import pylab,numpy
from mpl_toolkits.basemap import Basemap
input=open('eqs7day-M1.txt','rU').readlines()
keys=input[0].split('\t')
Lats,Lons=[],[]
for line in input[1:]:
    D={}
    rec=line.split('\t')
    for col in range(len(keys)):
        D[keys[col]]=rec[col]
    Lats.append(float(D['Lat']))
    Lons.append(float(D['Lon']))
map = Basemap(projection='moll',lat_0=50,lon_0=-100, resolution='c',area_thresh=1000.)
map.drawcoastlines()
map.drawmapboundary()
map.drawmeridians(numpy.arange(0,360,30))
map.drawparallels(numpy.arange(-90,90,30))
X,Y=map(Lons,Lats)
pylab.plot(X,Y,'ro')
pylab.show()
