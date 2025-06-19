import RPi.GPIO as GPIO
import time

delay=1

GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
GPIO.setwarnings(False) #Disable warnings

#Use pin 32 for PWM signal
pwm_gpio = 32
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)

pwm.start(10)
time.sleep(delay)

pwm.ChangeDutyCycle(95)
time.sleep(delay)

#Close GPIO & cleanup
pwm.stop()
GPIO.cleanup()
