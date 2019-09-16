#!/usr/bin/env python3
import curses
import argparse
import Adafruit_BBIO.GPIO as GPIO

def main(stdscr):
	# Use --size to specify size of board. Defaults to 8x8
	parser = argparse.ArgumentParser()
	parser.add_argument("--size", type=int, default=8)
	args = parser.parse_args()
	size = args.size

	# Setup curses
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)
	curses.curs_set(1)

	# Setup GPIO
	GPIO.setup("P9_22", GPIO.IN) # down
	GPIO.add_event_detect("P9_22", GPIO.RISING)

	GPIO.setup("P9_24", GPIO.IN) # left
	GPIO.add_event_detect("P9_24", GPIO.RISING)

	GPIO.setup("P9_23", GPIO.IN) # up
	GPIO.add_event_detect("P9_23", GPIO.RISING)

	GPIO.setup("P9_21", GPIO.IN) # right
	GPIO.add_event_detect("P9_21", GPIO.RISING)

	GPIO.setup("P9_20", GPIO.IN) # clear
	GPIO.add_event_detect("P9_20", GPIO.RISING)

	new_frame(stdscr, size)

	cur_x = 0
	cur_y = 0

	while True:
		stdscr.refresh()

		# Updates current position based on button pressed
		if GPIO.event_detected("P9_24"):
			if cur_x > 0:
				cur_x = cur_x - 1
		elif GPIO.event_detected("P9_21"):
			if cur_x < size - 1:
				cur_x = cur_x + 1
		elif GPIO.event_detected("P9_23"):
			if cur_y > 0:
				cur_y = cur_y - 1
		elif GPIO.event_detected("P9_22"):
			if cur_y < size - 1:
				cur_y = cur_y + 1
		elif GPIO.event_detected("P9_20"):
			new_frame(stdscr, size)
			cur_x = 0
			cur_y = 0

		# Prints an X in the current position
		stdscr.addstr(5 + cur_y, 2 + cur_x * 2, 'X')
		stdscr.move(5 + cur_y, 2 + cur_x * 2)

# Resets to an empty frame
def new_frame(stdscr, size):
	stdscr.erase()

	stdscr.addstr(0, 0, "Welcome to Etch-a-Sketch!\nUse the directional buttons to move the cursor.\nPress the lone button to clear the screen.")
	
	# Draw boundaries
	for i in range(size):
		stdscr.addstr(4, 2 + i * 2, '_') #str(i))
		stdscr.addstr(4 + size, 2 + i * 2, '_')
		stdscr.addstr(5 + i, 0, '|') #str(i))
		stdscr.addstr(5 + i, size * 2 + 1, '|')

	stdscr.addstr(5, 2, 'X')
	stdscr.move(5, 2)
	stdscr.refresh()

# Calls main with a wrapper around curses
curses.wrapper(main)
