#!/bin/sh

temp1=`i2cget -y 1 0x49 00`
temp2=`i2cget -y 1 0x4a 00`

temp1f=$(($temp1 *9 /5 +32))
temp2f=$(($temp2 *9 /5 +32))

echo "Temp 1:"
echo "$temp1f F"
echo "Temp 2:"
echo "$temp2f F"
