import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialisation I2C et ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain = 1  # adapté à 3.3 V

def lire_feedback_servos(ads):
    chan1 = AnalogIn(ads, ADS.P0)
    chan2 = AnalogIn(ads, ADS.P1)

    angle1 = chan1.voltage * (360 / 3.3)
    angle2 = chan2.voltage * (360 / 3.3)

    angle1 = max(0, min(360, angle1))
    angle2 = max(0, min(360, angle2))

    return angle1, angle2

# Boucle principale
while True:
    a1, a2 = lire_feedback_servos(ads)
    print(f"Servo 1 : {a1:.1f}°\tServo 2 : {a2:.1f}°")
    time.sleep(0.2)
