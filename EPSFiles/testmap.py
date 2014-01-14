#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import pylab
from mpl_toolkits.basemap import Basemap
m = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49, projection='lcc', lat_1=33, lat_2=45, lon_0=-95, resolution='c', area_thresh=10000) 
m.bluemarble()
pylab.show()

