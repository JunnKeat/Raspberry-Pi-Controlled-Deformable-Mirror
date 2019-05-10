import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)

pca.frequency = 60 
led_channel = pca.channels[7]
led_channel.duty_cycle = 0
