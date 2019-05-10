import board
import busio
import adafruit_pca9685
import time
import numpy as np
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

hat.frequency = 800
channel0 = hat.channels[0]
#dutycycle = 1.5
channel0.duty_cycle = 40000 #int((65535*dutycycle)/100)
#print (int((65535*dutycycle)/100))

#Vout vs Duty Cycle
#steps = np.linspace(0,3000,15)
#for i in steps:
#    led_channel.duty_cycle = int(i)
#    print (int(i))
#    time.sleep(5)
#    
#largesteps = np.linspace(3001,65535,15)
#for i in largesteps:
#    led_channel.duty_cycle = int(i)
#    print (int(i))
#    time.sleep(5)

    
#Input Freq vs Output Freq
#steps = np.linspace(50,2001,20)
#for i in steps:
    #hat.frequency = int(i)
    #print(int(i))
    #time.sleep(3)