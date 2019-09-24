#!/usr/bin/env python3
import curses
import smbus
import argparse
import math
import Adafruit_BBIO.GPIO as GPIO

bus = smbus.SMBus(2)
matrix = 0x70

def main():
	size = 8 # static when using 8x8 matrix

	# Setup GPIO
	GPIO.setup("P9_22", GPIO.IN) # left
	GPIO.add_event_detect("P9_22", GPIO.RISING)

	GPIO.setup("P9_24", GPIO.IN) # up
	GPIO.add_event_detect("P9_24", GPIO.RISING)

	GPIO.setup("P9_23", GPIO.IN) # right
	GPIO.add_event_detect("P9_23", GPIO.RISING)

	GPIO.setup("P9_21", GPIO.IN) # down
	GPIO.add_event_detect("P9_21", GPIO.RISING)

	GPIO.setup("P9_26", GPIO.IN) # clear
	GPIO.add_event_detect("P9_26", GPIO.RISING)

	cur_x = 0
	cur_y = 0

	image = new_image()
	board = new_board(size)

	bus.write_i2c_block_data(matrix, 0, image)

	while True:
		changed = False

		# Updates current position based on button pressed
		if GPIO.event_detected("P9_22"):
			if cur_x > 0:
				cur_x = cur_x - 1
				changed = True
		elif GPIO.event_detected("P9_23"):
			if cur_x < size - 1:
				cur_x = cur_x + 1
				changed = True
		elif GPIO.event_detected("P9_21"):
			if cur_y > 0:
				cur_y = cur_y - 1
				changed = True
		elif GPIO.event_detected("P9_24"):
			if cur_y < size - 1:
				cur_y = cur_y + 1
				changed = True
		elif GPIO.event_detected("P9_26"):
			cur_x = 0
			cur_y = 0
			image = new_image()
			board = new_board(size)

		# If x,y was changed and that spot on the board is not on
		if changed and not board[cur_x][cur_y]:
			index = 2 * cur_x + 1
			delta = int(math.pow(2, cur_y))
			image[index] = image[index] + delta
			board[cur_x][cur_y] = True

		bus.write_i2c_block_data(matrix, 0, image)


# Return empty matrix
def new_image():
	return [0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
			0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]


# Return empty board state
def new_board(size):
	new_board = []
	for i in range(0, size):
		new_row = []
		for j in range(0, size):
			new_row.append(False)
		new_board.append(new_row)

	new_board[0][0] = True

	return new_board


if __name__ == '__main__':
	main()
