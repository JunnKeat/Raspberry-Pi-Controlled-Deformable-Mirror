import board
import busio
import adafruit_pca9685
import time
import numpy as np
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

hat.frequency = 800

channel0 = hat.channels[0]
channel1 = hat.channels[1]
channel2 = hat.channels[2]#B
channel3 = hat.channels[3]#E
channel4 = hat.channels[4]

channel0.duty_cycle = 0
channel1.duty_cycle = 0
channel2.duty_cycle = 0
channel3.duty_cycle = 0
channel4.duty_cycle = 0
#int((65535*dutycycle)/100)
#print (int((65535*dutycycle)/100))

#Vout vs Duty Cycle

#while True:
#    steps = np.linspace(0,65535,30)
#    for i in steps:
#        channel0.duty_cycle = int(i)
#        print (int(i))
#        time.sleep(0.1)
#    steps = np.linspace(65535,0,30)   
#    for i in steps:
#        channel0.duty_cycle = int(i)
#        print (int(i))
#        time.sleep(0.1)    
    
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