from machine import I2C, Pin
from utime import sleep_ms
from lib.bh1750 import BH1750, BH1750Mode

i2c = I2C(0, scl=Pin(9), sda=Pin(8))
sensor = BH1750(i2c=i2c)

while True:
    r = sensor.luminance(BH1750Mode.ONCE_HIRES_2)
    print(f"{r:.2f}")
    sleep_ms(50)
