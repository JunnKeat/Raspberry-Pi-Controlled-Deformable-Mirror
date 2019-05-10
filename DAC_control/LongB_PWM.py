import board
import busio
import time
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)

pca.frequency = 60
led_channel = pca.channels[7]
led_channel.duty_cycle = 32

#for i in range(21):
    #pinumb = i*200
    #print(pinumb)
    #led_channel.duty_cycle = 16*pinumb
    #time.sleep(10)