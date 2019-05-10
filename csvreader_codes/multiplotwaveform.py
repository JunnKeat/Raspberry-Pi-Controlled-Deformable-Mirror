#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:29:43 2019

@author: 14keatt1
"""

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/Users/14keatt1/Documents/Imperial/Year3/Project/2019-2-28/Opto_Waveforms/OptoA_Waveform.CSV', sep = ",")
df.columns=['time', 'signal']
timea = df['time']
signala = df['signal']

df = pd.read_csv('/Users/14keatt1/Documents/Imperial/Year3/Project/2019-2-28/Opto_Waveforms/OptoB_Waveform.CSV', sep = ",")
df.columns=['time', 'signal']
timeb = df['time']
signalb = df['signal']

df = pd.read_csv('/Users/14keatt1/Documents/Imperial/Year3/Project/2019-2-28/Opto_Waveforms/OptoC_Waveform.CSV', sep = ",")
df.columns=['time', 'signal']
timec = df['time']
signalc = df['signal']

df = pd.read_csv('/Users/14keatt1/Documents/Imperial/Year3/Project/2019-2-28/Opto_Waveforms/OptoD_Waveform.CSV', sep = ",")
df.columns=['time', 'signal']
timed = df['time']
signald = df['signal']

df = pd.read_csv('/Users/14keatt1/Documents/Imperial/Year3/Project/2019-2-28/Opto_Waveforms/OptoE_Waveform.CSV', sep = ",")
df.columns=['time', 'signal']
timee = df['time']
signale = df['signal']

df = pd.read_csv('/Users/14keatt1/Documents/Imperial/Year3/Project/2019-2-28/Opto_Waveforms/Optof_Waveform.CSV', sep = ",")
df.columns=['time', 'signal']
timef = df['time']
signalf = df['signal']

def multiplot():
    
    plt.subplot(3,2,1)
    plt.plot(timea,signala,'-')
    #plt.axis([min(timea),max(timea),min(signala)-0.5,max(signala)+0.5])
    plt.grid(True)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Voltage of A (V)', fontsize=12)
    
    plt.subplot(3,2,2)
    plt.plot(timeb,signalb,'-')
    #plt.axis([min(timea),max(timea),min(signala)-0.5,max(signala)+0.5])
    plt.grid(True)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Voltage of B (V)', fontsize=12)
    
    plt.subplot(3,2,3)
    plt.plot(timec,signalc,'-')
    #plt.axis([min(timea),max(timea),min(signala)-0.5,max(signala)+0.5])
    plt.grid(True)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Voltage of C (V)', fontsize=12)
    
    plt.subplot(3,2,4)
    plt.plot(timed,signald,'-')
    #plt.axis([min(timea),max(timea),min(signala)-0.5,max(signala)+0.5])
    plt.grid(True)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Voltage of D (V)', fontsize=12)
    
    plt.subplot(3,2,5)
    plt.plot(timee,signale,'-')
    #plt.axis([min(timea),max(timea),min(signala)-0.5,max(signala)+0.5])
    plt.grid(True)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Voltage of E (V)', fontsize=12)
    
    plt.subplot(3,2,6)
    plt.plot(timef,signalf,'-')
    #plt.axis([min(timea),max(timea),min(signala)-0.5,max(signala)+0.5])
    plt.grid(True)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Voltage of F (V)', fontsize=12)
    
    
    
    plt.show()
    
def oneplot():
    plt.plot(timea,signala,'-', label = 'Opto-Switch A')
    plt.plot(timeb,signalb,'-', label = 'Opto-Switch B')
    plt.plot(timec,signalc,'-', label = 'Opto-Switch C')
    plt.plot(timed,signald,'-', label = 'Opto-Switch D')
    plt.plot(timee,signale,'-', label = 'Opto-Switch E')
    plt.plot(timef,signalf,'-', label = 'Opto-Switch F')
    #plt.axis([min(timea),max(timea),min(signala)-0.5,max(signala)+0.5])
    plt.grid(True)
    plt.legend(loc='best')
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Voltage(V)', fontsize=12)
    plt.show()

#multiplot()
oneplot()