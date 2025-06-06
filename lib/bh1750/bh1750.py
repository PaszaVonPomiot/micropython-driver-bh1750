from utime import sleep_ms
from machine import I2C


class BH1750State:
    # Change state
    PWR_DOWN = 0x00
    PWR_ON = 0x01
    RESET = 0x07


class BH1750Mode:
    # Start continuous measurement
    CONTINUOUS_LOWRES = 0x13
    CONTINUOUS_HIRES_1 = 0x10
    CONTINUOUS_HIRES_2 = 0x11

    # Start measurement and return to Power Down
    ONCE_HIRES_1 = 0x20
    ONCE_HIRES_2 = 0x21
    ONCE_LOWRES = 0x23


class BH1750:
    """Driver for BH1750 ambient light sensor (lux meter) using I2C."""

    def __init__(self, i2c: I2C, i2c_address: int = 0x23) -> None:
        self.i2c = i2c
        self.i2c_address: int = i2c_address

    def power_down(self) -> None:
        """Power down the sensor to reduce current consumption."""
        self.set_mode(BH1750State.PWR_DOWN)

    def power_on(self) -> None:
        """Power on the sensor."""
        self.set_mode(BH1750State.PWR_ON)

    def reset(self) -> None:
        """Reset data register and go to Power Down mode."""
        self.power_on()
        self.set_mode(BH1750State.RESET)

    def set_mode(self, mode: int) -> None:
        """Set sensor mode."""
        self.mode: int = mode
        self.i2c.writeto(self.i2c_address, bytes([self.mode]))

    def luminance(self, mode: int) -> float:
        """Perform a light measurement and return the result in lux."""
        if mode & 0x10 and mode != getattr(self, "mode", None):
            self.set_mode(mode)
        if mode & 0x20:
            self.set_mode(mode)
        sleep_ms(24 if mode in (0x13, 0x23) else 180)
        data: bytes = self.i2c.readfrom(self.i2c_address, 2)
        factor: float = 2.0 if mode in (0x11, 0x21) else 1.0
        return (data[0] << 8 | data[1]) / (1.2 * factor)
