#!/usr/bin/env python3
import argparse
import Adafruit_BBIO.GPIO as GPIO

def main():
	# Setup GPIO
	GPIO.setup("P9_22", GPIO.IN) # down
	GPIO.add_event_detect("P9_22", GPIO.RISING)
	GPIO.setup("P9_12", GPIO.OUT)
	led0 = False

	GPIO.setup("P9_24", GPIO.IN) # left
	GPIO.add_event_detect("P9_24", GPIO.RISING)
	GPIO.setup("P9_13", GPIO.OUT)
	led1 = False

	GPIO.setup("P9_23", GPIO.IN) # up
	GPIO.add_event_detect("P9_23", GPIO.RISING)
	GPIO.setup("P9_11", GPIO.OUT)
	led2 = False

	GPIO.setup("P9_21", GPIO.IN) # right
	GPIO.add_event_detect("P9_21", GPIO.RISING)
	GPIO.setup("P9_14", GPIO.OUT)
	led3 = False

	GPIO.setup("P9_20", GPIO.IN) # clear
	GPIO.add_event_detect("P9_20", GPIO.RISING)

	# If button is pressed, switch the appropriate LED
	while True:
		if GPIO.event_detected("P9_23"):
			switch_led(11, led2)
			led2 = not led2

		if GPIO.event_detected("P9_22"):
			switch_led(12, led0)
			led0 = not led0

		if GPIO.event_detected("P9_24"):
			switch_led(13, led1)
			led1 = not led1

		if GPIO.event_detected("P9_21"):
			switch_led(14, led3)
			led3 = not led3

		if GPIO.event_detected("P9_20"):
			GPIO.output("P9_11", GPIO.LOW)
			led2 = False
			GPIO.output("P9_12", GPIO.LOW)
			led0 = False
			GPIO.output("P9_13", GPIO.LOW)
			led1 = False
			GPIO.output("P9_14", GPIO.LOW)
			led3 = False

# Function to toggle an LED in the given GPIO port
def switch_led(gpio, on):
	if on:
		GPIO.output("P9_{}".format(gpio), GPIO.LOW)
	else:
		GPIO.output("P9_{}".format(gpio), GPIO.HIGH)

if __name__ == "__main__":
	main()
