import board
import busio
import adafruit_pca9685
import time
import numpy as np
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

hat.frequency = 800

channel0 = hat.channels[0] #middle
channel1 = hat.channels[1] #Up
channel2 = hat.channels[2] #right
channel3 = hat.channels[3] #down
channel4 = hat.channels[4] #left

#Individual Control
channel0.duty_cycle = 17000
channel1.duty_cycle = 15000#5000
channel2.duty_cycle = 0
channel3.duty_cycle = 17000
channel4.duty_cycle = 0

#Middle Exercise
middle = False

while middle == True:
    steps = np.linspace(0,65535,20)
    for i in steps:
        channel1.duty_cycle = int(i)
        print (int(i))
        time.sleep(2)
    steps = np.linspace(65535,0,20)   
    for i in steps:
        channel1.duty_cycle = int(i)
        print (int(i))
        time.sleep(2)    
#    
#    
#    
#Up Down Exercise
updown = True

while updown == True:
    steps13 = np.linspace(0,65535,20)
    for i in steps13:
        channel3.duty_cycle = int(i)
        channel4.duty_cycle = int(i)
        print (int(i))
        time.sleep(0.1)
    steps13 = np.linspace(65535,0,20)   
    for i in steps13:
        channel3.duty_cycle = int(i)
        channel4.duty_cycle = int(i)
        print (int(i))
        time.sleep(0.1) 
    
#Left Right Exercise
#leftright = True
#while leftright == True:
#    steps24 = np.linspace(0,65535,30)
#    for i in steps24:
#        channel2.duty_cycle = int(i)
#        channel4.duty_cycle = int(i)
#        print (int(i))
#        time.sleep(0.1)
#    steps24 = np.linspace(65535,0,30)   
#    for i in steps24:
#        channel2.duty_cycle = int(i)
#        channel4.duty_cycle = int(i)
#        print (int(i))
#        time.sleep(0.1) 
    