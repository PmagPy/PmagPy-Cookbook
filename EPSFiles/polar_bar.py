#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.cm as cm # color map
import random,math,pylab
fig = pylab.figure(figsize=(8,8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
N,mu,sigma = 100,180.,20.
Dirs,thetas,radii=[],[],[]
for i in range(N):
    Dirs.append(random.gauss(mu,sigma))
Thetas=range(0,360,10)
for t in Thetas:
    cnt=0
    for d in Dirs:
        if d<t and d>t0:
            cnt+=1
    if cnt>0:
        radii.append(cnt)
        thetas.append(t*math.pi/180.)
    t0=t
bars = ax.bar(thetas, radii, width=width*math.pi/180., bottom=0.0)
for r,bar in zip(radii, bars):
    bar.set_facecolor( cm.jet(r/grad))
    bar.set_alpha(0.5)
pylab.show()
