import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Init I2C et ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain = 1  # plage ±4.096 V

# Canal analogique sur A0
chan = AnalogIn(ads, ADS.P0)

print("Lecture de la position du servo en degrés (FB5311M-360):")
while True:
    voltage = chan.voltage
    # Conversion tension → angle
    angle = (voltage - 0.5) * 180  # (360 / 2.0)
    # Clamp
    angle = max(0, min(360, angle))

    print(f"Tension : {voltage:.3f} V → Angle : {angle:.1f}°")
    time.sleep(0.2)
