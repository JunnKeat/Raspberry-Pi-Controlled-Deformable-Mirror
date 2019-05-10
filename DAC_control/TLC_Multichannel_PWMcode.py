import board
import busio
import adafruit_tlc59711
import time
import numpy as np

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
leds = adafruit_tlc59711.TLC59711(spi)
leds[0]=(10000,10000,0)

#steps = np.linspace(0,65535,50)

#for i in steps:
    #leds[0] = (int(i),int(i),0)
    #print(int(i))
    #time.sleep(1)

#freq = 5000
#dutycycle = 0.7

#starttime = time.time()
#while True:
    #print(time.time()-starttime)
    #leds[0] = (65535,0,0)
    #time.sleep((1/(freq))*dutycycle)
    #leds[0] = (0,0,0)
    #time.sleep((1/(freq))*(1-dutycycle))
    #print ("Running")
    