#!/usr/bin/env python3
import curses
import argparse

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

	new_frame(stdscr, size)

	cur_x = 0
	cur_y = 0

	while True:
		stdscr.refresh()

		key = stdscr.getch()

		if key == curses.KEY_LEFT:
			if cur_x > 0:
				cur_x = cur_x - 1
		elif key == curses.KEY_RIGHT:
			if cur_x < size - 1:
				cur_x = cur_x + 1
		elif key == curses.KEY_UP:
			if cur_y > 0:
				cur_y = cur_y - 1
		elif key == curses.KEY_DOWN:
			if cur_y < size - 1:
				cur_y = cur_y + 1
		elif key == ord('c'):
			new_frame(stdscr, size)
			cur_x = 0
			cur_y = 0

		stdscr.addstr(5 + cur_y, 2 + cur_x * 2, 'X')
		stdscr.move(5 + cur_y, 2 + cur_x * 2)


def new_frame(stdscr, size):
	stdscr.erase()

	stdscr.addstr(0, 0, "Welcome to Etch-a-Sketch!\nUse the arrow keys to move the cursor.\nPress 'c' to clear the screen.")
	
	# Draw boundaries
	for i in range(size):
		stdscr.addstr(4, 2 + i * 2, '_') #str(i))
		stdscr.addstr(4 + size, 2 + i * 2, '_')
		stdscr.addstr(5 + i, 0, '|') #str(i))
		stdscr.addstr(5 + i, size * 2 + 1, '|')

	stdscr.addstr(5, 2, 'X')
	stdscr.move(5, 2)
	stdscr.refresh()


curses.wrapper(main)