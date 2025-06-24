import time
import board              
import busio            
import adafruit_lsm9ds0
from math import *

i2c = busio.I2C(board.SCL, board.SDA)
#print("Creation de l'interface I2C effectuee") 

sensor = adafruit_lsm9ds0.LSM9DS0_I2C(i2c)
#print("Initialisation du gyroscope effectuee")


while True:
    accel_x, accel_y, accel_z = sensor.acceleration
    gyro_x, gyro_y, gyro_z = sensor.gyro
    mag_x, mag_y, mag_z = sensor.magnetic

    heading = atan2(mag_y, mag_x);
    heading *= 180.0/3.14
    if (heading<0) :
        heading+= 360.0

    #print("Gyroscope (degre/s): X={:.2f} Y={:.2f} Z={:.2f}".format(gyro_x, gyro_y, gyro_z))
    #print("Accelerometre (m/s2): Z={:.2f} Y={:.2f} Z={:.2f}".format(accel_x, accel_y, accel_z))
    print("Magnetometre (uT): X={:.2f} Y={:.2f} Z={:.2f}".format(mag_x, mag_y, mag_z))
    print("VLVLVLLMBLMBA.PK.R3OLRMO valeur en degres : ", heading)
    print("----------------------------------------------------------------------")
    time.sleep(2.0)

