import time
import board
import busio
import adafruit_lsm9ds0
import math  # Importer le module math pour atan2

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds0.LSM9DS0_I2C(i2c)

while True:
    accel_x, accel_y, accel_z = sensor.acceleration
    gyro_x, gyro_y, gyro_z = sensor.gyro
    mag_x, mag_y, mag_z = sensor.magnetic

    # Calculer l'angle par rapport au nord
    angle_radians = math.atan2(mag_y, mag_x)
    angle_degrees = math.degrees(angle_radians)  # Convertir en degrés
    angle_degrees = angle_degrees + 360 if angle_degrees < 0 else angle_degrees  # Ajuster pour obtenir un angle positif

    print("Angle par rapport au nord (degrés): {:.2f}".format(angle_degrees))
    print("Magnetometre (uT): X={:.2f} Y={:.2f} Z={:.2f}".format(mag_x, mag_y, mag_z))
    print("----------------------------------------------------------------------")
    time.sleep(2.0)
