#!/usr/bin/env python3
import os
import subprocess

def main():
	while(True):
		t1 = int(subprocess.check_output("i2cget -y 1 0x49 00", shell=True), 16)
		t2 = int(subprocess.check_output("i2cget -y 1 0x4a 00", shell=True), 16)
		t1 = (t1 * 9)/5 + 32
		t2 = (t2 * 9)/5 + 32
		os.system("./write.py {0} {1}".format(t1, t2))

if __name__ == '__main__':
	main()
