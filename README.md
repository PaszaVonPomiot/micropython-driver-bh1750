# MicroPython driver for BH1750 sensor

MicroPython driver for BH1750 sensor over I2C

![bh1750](/docs/img/bh1750a.jpg)

## Hardware

-   MicroPython compatible development board with I2C support eg. [Raspberry Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
-   BH1750 sensor module ([datasheet](docs/bh1750fvi-e-186247.pdf))

## Software

-   [MicroPython](https://micropython.org/download/) - firmware for your development board

## Installation

-   Copy the bh1750.py file or lib folder to the root of your MicroPython device filesystem.

## API Interface

`luminance(mode: int) -> float` - measure luminance

Available modes:

```py
class BH1750Mode:
    # Start continuous measurement
    CONTINUOUS_LOWRES = 0x13
    CONTINUOUS_HIRES_1 = 0x10
    CONTINUOUS_HIRES_2 = 0x11

    # Start measurement and return to Power Down
    ONCE_HIRES_1 = 0x20
    ONCE_HIRES_2 = 0x21
    ONCE_LOWRES = 0x23
```

## Code examples

Working examples can be found in [/examples](examples/)

```py
from machine import I2C, Pin
from lib.bh1750 import BH1750, BH1750Mode

i2c = I2C(0, scl=Pin(9), sda=Pin(8))
sensor = BH1750(i2c=i2c)
luminance = sensor.luminance(BH1750Mode.ONCE_HIRES_2)
print(f"{luminance:.2f}")
```

## Credits

[PinkInk](https://github.com/PinkInk) @ [https://github.com/PinkInk/upylib/tree/master/bh1750](https://github.com/PinkInk/upylib/tree/master/bh1750) - for initial code I forked and updated
