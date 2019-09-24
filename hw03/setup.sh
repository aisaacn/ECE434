#!/bin/sh

config-pin P9_17 i2c
config-pin P9_18 i2c
config-pin P9_19 i2c
config-pin P9_20 i2c

config-pin P8_33 qep
config-pin P8_35 qep
config-pin P8_11 qep
config-pin P8_12 qep

./../../exercises/displays/matrix8x8/i2cmatrix.py
