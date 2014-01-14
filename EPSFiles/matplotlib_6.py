#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
import pylab,numpy
def tabread(file):
    input=open(file,'rU').readlines()
    keys=input[0].split('\t')
    data=[]
    for line in input[1:]:
        D={}
        rec=line.split('\t')
        for col in range(len(keys)):
            D[keys[col]]=rec[col]
        data.append(D)
    return data
def main():
    """reads in eqs7day-M1.txt file from USGS website 
http://earthquake.usgs.gov/earthquakes/catalogs/index.php
    and plots histogram of magnitudes"""
    file='eqs7day-M1.txt'
    EQs=tabread(file)
    Mags=[]
    for EQ in EQs:
        Mags.append(float(EQ['Magnitude']))
    pylab.hist(Mags,bins=50,normed=True)
    pylab.xlabel('Richter Magnitude')
    pylab.ylabel('Frequency')
    pylab.show()     
main()   
