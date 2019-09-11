#!/usr/bin/env python3
import curses
import argparse

def main():
	stdscr = curses.initscr()

	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)

	stdscr.addstr(0, 0, "hello")

	#new_frame(stdscr)

	x_size = 8
	y_size = 8

	while True:
		stdscr.refresh()

		key = stdscr.getch()

		if key == curses.KEY_LEFT:
			# do left
			stdscr.addstr(5, 5, "left")
		elif key == curses.KEY_RIGHT:
			# do right
			stdscr.addstr(6, 6, "right")
		elif key == curses.KEY_UP:
			# do up
			stdscr.addstr(7, 7, "up")
		elif key == curses.KEY_DOWN:
			# do down
			stdscr.addstr(8, 8, "down")
		elif key == ord('c'):
			# clear
			stdscr.addstr(4, 4, "clear")




def new_frame(stdscr):
	stdscr.erase()

	stdscr.addstr(0, 0, "hi welcome to the show\n")