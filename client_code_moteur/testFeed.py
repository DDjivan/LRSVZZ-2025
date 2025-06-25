import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialisation I2C et ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain = 1  # plage ±4.096 V (adaptée à 3.3 V)

# Lecture sur A0
chan = AnalogIn(ads, ADS.P0)

print("Lecture du feedback servo (0–3.3V → 0–360°)")
while True:
    voltage = chan.voltage
    angle = voltage * (360 / 3.3)  # angle = voltage * 109.09
    angle = max(0, min(360, angle))  # clamp
    print(f"Tension : {voltage:.3f} V → Angle estimé : {angle:.1f}°")
    time.sleep(0.2)
