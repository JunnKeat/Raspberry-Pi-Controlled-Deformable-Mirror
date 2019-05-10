#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:29:43 2019

@author: 14keatt1
"""

import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import find_peaks
from scipy.interpolate import interp1d

Folderpath = '/Users/14keatt1/Documents/Imperial/Year3/Project/2019-3-21/gluedown/' 

filenames = os.listdir(Folderpath)
filenames = [file for file in filenames if '.csv' in file]

def normalisation(pixel, signal):
    peaks, _  = find_peaks(signal, height=100, distance=10)    
    peakvalue = []  
    for peak in peaks:
#        plt.axvline(x=peak)
        yvalue = signal[peak]
        peakvalue.append(yvalue)
 
    f2 = interp1d(peaks, peakvalue, kind='cubic', fill_value='extrapolate')
    intsig = f2(pixel)
    print(peaks)

    newsignal = [100*x/y for x,y in zip(signal,intsig)]
    
    return intsig, newsignal

def test(file):
    df = pd.read_csv(file, sep = ",")
    df.columns=['pixel', 'signal']
    pixel = df['pixel']
    signal = df['signal']
    intsig, newsignal = normalisation(pixel, signal)
    plt.plot(pixel,signal,'-', label = 'Original Signal')
    plt.plot(pixel,newsignal,'-', label = 'Normalised Signal')
    plt.plot(pixel,intsig,'--', label = 'Normalizing Function')
    
    plt.axis([400,800,0,200])
    plt.grid(True)
    plt.xlabel('Pixel', fontsize=12)
    plt.ylabel('Pixel Intensity', fontsize=12)
    plt.legend(loc='best')
    plt.show()

#test('/Users/14keatt1/Documents/Imperial/Year3/Project/2019-3-20/solderup/09_solder.csv')

def oneplot(filenames):
#    voltagelabel = 0
    for file in filenames:
        df = pd.read_csv(Folderpath + file, sep = ",")
        df.columns=['pixel', 'signal']
        pixel = df['pixel']
        signal = df['signal']
        intsig, newsignal = normalisation(pixel, signal)
        plt.plot(pixel,newsignal,'-')#, label = '%dV' %(voltagelabel))
#        voltagelabel = voltagelabel + 5
        plt.pause(5)
        
    plt.axis([400,800,0,200])
    plt.grid(True)
    plt.legend(loc='best')
    plt.xlabel('Pixel', fontsize=12)
    plt.ylabel('Grey Value', fontsize=12)
    plt.show()

def multiplot(filenames):
    numberoffiles = len(filenames)
#    voltagelabel = 0
    filenumber = 0
    fig, ax = plt.subplots(ncols=1,nrows=numberoffiles,sharex=True,sharey=True,squeeze=False)
    fig.text(0.5, 0.04, 'Pixel', va='center', ha='center', fontsize=12)
    fig.text(0.04, 0.5, 'Pixel Intensity', va='center', ha='center', rotation='vertical', fontsize=12)
    
    for file in filenames:
        print(file)
        filenumber = filenumber + 1
        df = pd.read_csv(Folderpath + file, sep = ",")
        df.columns=['pixel', 'signal']
        pixel = df['pixel']
        signal = df['signal']
        intsig, newsignal = normalisation(pixel, signal)
#        plt.subplot(5,1,filenumber)
        plt.subplots_adjust(hspace = .0001)
#        plt.plot(pixel,newsignal,'-')#, label = '%dV' %(voltagelabel))
        ax[filenumber-1][0].plot(pixel,newsignal,'-')
        plt.axis([400,800,0,100])
#        plt.xticks(np.arange(200, 701, 50))
#        plt.yticks(np.arange(0, 101, 50))
#        ax[filenumber-1][0].grid(True)

#        if filenumber == 5:
#            break
    
      
    
        
    
    plt.show()

#oneplot(filenames)
multiplot(filenames)

#solder

N = 1/17

voltageup = [0, 16.25, 23.52, 28.86, 33.82, 38.56, 43.08, 47.54, 52.05, 56.73, 
             61.56, 66.49, 71.28, 76.00, 80.59, 85.10, 89.48, 93.81, 98.06, 
             102.15, 106.16, 110.16, 113.97, 117.75, 121.43, 125.07, 128.64,
             132.20, 135.97, 135.97]

voltagedown = [135.97, 135.97, 132.2, 128.64, 125.07, 121.43, 117.75, 113.97,
               110.16, 106.16, 102.15, 98.06, 93.81, 89.48, 85.1, 80.59, 76.0,
               71.28, 66.49, 61.56, 56.73, 52.05, 47.54, 43.08, 38.56, 33.82,
               28.86, 23.52, 16.25, 0]

pixelup = [735, 716, 705, 695, 687, 680, 673, 666, 659, 651, 644, 637, 630,
           625, 619, 613, 607, 603, 600, 595, 591, 586, 583, 579, 577, 573,
           570, 567, 564, 564]

distup = [0.0,
 297.1823529411764,
 469.235294117647,
 625.6470588235294,
 750.7764705882353,
 860.2647058823528,
 969.7529411764706,
 1079.2411764705882,
 1188.7294117647057,
 1313.8588235294117,
 1423.3470588235293,
 1532.835294117647,
 1642.3235294117644,
 1720.5294117647056,
 1814.3764705882352,
 1908.2235294117645,
 2002.070588235294,
 2064.635294117647,
 2111.5588235294117,
 2189.764705882353,
 2252.3294117647056,
 2330.535294117647,
 2377.4588235294113,
 2440.0235294117642,
 2471.305882352941,
 2533.870588235294,
 2580.7941176470586,
 2627.7176470588233,
 2674.641176470588,
 2674.641176470588]

pixeldown = [555, 555, 557, 558, 561, 563, 566, 568, 570, 573, 577, 579, 583, 
             587, 587, 596, 600, 605, 610, 615, 621, 628, 635, 643, 650, 658, 
              669, 679, 695, 735]

distdown = [2815.411764705882,
 2815.411764705882,
 2784.1294117647058,
 2768.488235294117,
 2721.564705882353,
 2690.282352941176,
 2643.358823529412,
 2612.076470588235,
 2580.7941176470586,
 2533.870588235294,
 2471.305882352941,
 2440.0235294117642,
 2377.4588235294113,
 2314.8941176470585,
 2314.8941176470585,
 2174.1235294117646,
 2111.5588235294117,
 2033.3529411764705,
 1955.1470588235295,
 1876.941176470588,
 1783.0941176470587,
 1673.605882352941,
 1564.1176470588234,
 1438.9882352941177,
 1329.4999999999998,
 1204.370588235294,
 1032.3176470588235,
 875.905882352941,
 625.6470588235294,
 0.0]

plt.scatter(voltageup,distup, label = 'Solder Forward')
plt.scatter(voltagedown,distdown, label = 'Solder Reverse')
plt.xlabel('Voltage (V)', fontsize=12)
plt.ylabel('Distance (nm)', fontsize=12)  
plt.legend(loc='best')
plt.show

#Glue

voltageup = [0, 16.25, 23.52, 28.86, 33.82, 38.56, 43.08, 47.54, 52.05, 56.73, 
             61.56, 66.49, 71.28, 76.00, 80.59, 85.10, 89.48, 93.81, 98.06, 
             102.15, 106.16, 110.16, 113.97, 117.75, 121.43, 125.07, 128.64,
             132.20, 135.97, 135.97]

voltagedown = [135.97, 135.97, 132.2, 128.64, 125.07, 121.43, 117.75, 113.97,
               110.16, 106.16, 102.15, 98.06, 93.81, 89.48, 85.1, 80.59, 76.0,
               71.28, 66.49, 61.56, 56.73, 52.05, 47.54, 43.08, 38.56, 33.82,
               28.86, 23.52, 16.25, 0]

gluepixelup = [760, 737, 722, 712, 712, 689, 681, 669, 661, 654, 644, 634, 628, 
           620, 614, 607, 600, 595, 588, 584, 581, 572, 567, 564, 561, 556,
           553, 549, 544, 544]

gluepixeldown = [543, 545, 548, 552, 553, 556, 561, 564, 568, 572, 577, 581, 
                 586, 591, 597, 603, 609, 617, 622, 631, 638, 644, 653, 665, 
                 674, 685, 698, 715, 734, 758]

gluedistup = [0.0,
 265.9,
 439.3130434782608,
 554.9217391304347,
 554.9217391304347,
 820.8217391304347,
 913.3086956521738,
 1052.0391304347825,
 1144.5260869565216,
 1225.4521739130435,
 1341.0608695652172,
 1456.669565217391,
 1526.0347826086954,
 1618.5217391304348,
 1687.886956521739,
 1768.8130434782609,
 1849.7391304347825,
 1907.5434782608693,
 1988.4695652173912,
 2034.7130434782607,
 2069.395652173913,
 2173.4434782608696,
 2231.2478260869566,
 2265.9304347826082,
 2300.613043478261,
 2358.417391304348,
 2393.1,
 2439.3434782608692,
 2497.1478260869562,
 2497.1478260869562]

gluedistdown = [2508.708695652174,
 2485.586956521739,
 2450.904347826087,
 2404.660869565217,
 2393.1,
 2358.417391304348,
 2300.613043478261,
 2265.9304347826082,
 2219.686956521739,
 2173.4434782608696,
 2115.6391304347826,
 2069.395652173913,
 2011.591304347826,
 1953.786956521739,
 1884.4217391304346,
 1815.0565217391302,
 1745.6913043478257,
 1653.2043478260869,
 1595.3999999999999,
 1491.3521739130433,
 1410.4260869565217,
 1341.0608695652172,
 1237.013043478261,
 1098.282608695652,
 994.2347826086956,
 867.0652173913044,
 716.7739130434783,
 520.2391304347825,
 300.58260869565214,
 23.12173913043478]

plt.scatter(voltageup,gluedistup, label = 'Glue Forward')
plt.scatter(voltagedown,gluedistdown, label = 'Glue Reverse')
plt.xlabel('Voltage (V)', fontsize=12)
plt.ylabel('Distance (nm)', fontsize=12)  
plt.legend(loc='best')
plt.show







