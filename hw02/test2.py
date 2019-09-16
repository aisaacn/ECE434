import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P9_22", GPIO.IN)
 
while True:
	if GPIO.input("P9_22"):
		print("ON")
	else:
		print("OFF")
