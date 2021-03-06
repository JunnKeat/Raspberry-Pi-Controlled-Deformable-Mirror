#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:29:43 2019

@author: 14keatt1
"""

import pandas as pd
import numpy as np
from scipy.signal import find_peaks
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt

df = pd.read_csv('/Users/14keatt1/Documents/Imperial/Year3/Project/2019-3-11/01_solder_0v.csv', sep = ",")
df.columns=['pixel', 'signal']
pixel = df['pixel']
signal = df['signal']

#interpolation to pixel ratio 14.6
interpolated = np.linspace(min(pixel),max(pixel),10000)

#create cos2 fit
cos2fit = []

for t in interpolated:
#    fit = max(signal)*(np.cos((2*np.pi/39)*(t-62.4)))
    fit = max(signal)*(np.cos((np.pi/39)*(t-62.4))**2)-max(signal)/2

    cos2fit.append(fit)
    
#improve cos2 fit
cos2fitimprove = []
    
for fit in cos2fit:
    if fit < 0:
        fit = 0
        cos2fitimprove.append(fit)
    else:
        cos2fitimprove.append(fit)
          
#fitting gradient
#firstderivative = np.gradient(signal)
#
#peaks = []
#for p in pixel:
#    if (firstderivative[p]<0.5) and (firstderivative[p]> -0.5) and (signal[p]>40):
#        peaks.append(p)
#  

peaks, _  = find_peaks(signal, height=10)    
peakvalue = []  
for peak in peaks:
    plt.axvline(x=peak)
    yvalue = signal[peak]
    peakvalue.append(yvalue)
 
f2 = interp1d(peaks, peakvalue, kind='cubic', fill_value='extrapolate')

newsignal = [100*x/y for x,y in zip(signal,f2(pixel))]

   
#periodlist = []
#for i in range(len(peakpixels)-1):
#    period = peakpixels[i+1] - peakpixels[i]
#    periodlist.append(period)

#Plots#########################################################################


#plt.plot(pixel,firstderivative,'-')

plt.plot(pixel,signal,'-')
plt.plot(pixel,newsignal,'-')
plt.plot(interpolated,f2(interpolated),'--')
#plt.plot(interpolated,cos2fit,'-')
#plt.plot(interpolated,cos2fitimprove,'-')

plt.axis([min(pixel),max(pixel),min(signal)-5,max(signal)+5])
plt.grid(True)
plt.xlabel('Pixel', fontsize=18)
plt.ylabel('Grey Value', fontsize=18)
plt.show()
