Isaac Austin
ECE434 - HW02

I modified etchasketch.py to take advantage of the buttons rather than a keypad.
Move the cursor using the buttons as if they were a directional pad.
Use the button not in the arrangement of four as the clear button.
Same as before, run the script with ./etchasketch.py with the optional --size
flag to modify the board size.

I also added led_controller.py, a python script that toggles the LEDs on the
board by pressing the buttons.
Run this script with ./led_controller.py

Oscilloscope Questions
1) 	Min Voltage: 1.61V 
	Max Voltage: 2.96V
2) 	296.82ms
3)	Not close at all, almost three times
4)	I have no idea why they differ
5) 	About 20%
6)	The mean period always stays around 300ms
	Smaller values increase the processor usage
7)	The period is quite stable, always around 300ms
8)	Period stayed the same
9)	No
10)	Period stayed the same
11)	Drops as low as 55ms with sleep time of 0.01,
	but average stays around 300
