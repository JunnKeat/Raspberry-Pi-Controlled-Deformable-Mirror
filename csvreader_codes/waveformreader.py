#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:29:43 2019

@author: 14keatt1
"""

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/Users/14keatt1/Documents/Imperial/Year3/Project/2019-3-11/01_solder_0v.csv', sep = ",")
df.columns=['time', 'signal']
time = df['time']
signal = df['signal']
plt.plot(time,signal,'-')
plt.axis([min(time),max(time),min(signal)-0.05,max(signal)+0.05])
plt.grid(True)
plt.xlabel('Wavelength (nm)', fontsize=18)
plt.ylabel('Intensity (Wm$^{-2}$)', fontsize=18)
plt.show()
