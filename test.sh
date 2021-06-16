#!/bin/bash

echo hello

mcu=$(ls /dev | grep ttyACM)
echo "Found MCU on: ${mcu}"

for d in $(ls /dev | grep video); do
    echo ${d} | grep 'video[[:digit:]]$'
done

