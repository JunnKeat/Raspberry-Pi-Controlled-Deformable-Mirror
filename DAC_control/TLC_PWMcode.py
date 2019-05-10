import board
import busio
import adafruit_tlc59711
import time
import numpy as np

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
leds = adafruit_tlc59711.TLC59711(spi)
#leds[0]=(30000,0,0)

freq = 5000
dutycycle = 0.5

#steps = np.linspace(0,1,50)

#for i in steps:
    #leds[0] = (0,0,int(i))
    #print(int(i))
    #time.sleep(10)
    

#leds.b0 = 1000
starttime = time.time()
while True:
    #print(time.time()-starttime)
    leds[0] = (10000,65535,0)
    time.sleep((1/(freq))*dutycycle)
    leds[0] = (0,0,0)
    time.sleep((1/(freq))*(1-dutycycle))
    #print ("Running")
    