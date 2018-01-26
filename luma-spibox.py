#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import argparse
import atexit
import sys
import os
import RPi.GPIO as GPIO

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, LCD_FONT

debug = 0

# SPI-Box Setup
PIR = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN, GPIO.PUD_DOWN)

# MAX7219 configuration:
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)

# Scroll message across the LCD Panel
msg = "Hello"

# Turn off all the LEDs
def lightsOut():
    # Reset MAX7219
    device.cleanup()
    # Reset GPIO
    GPIO.cleanup()
    print ' - Exiting'

# Run lightsOut at exit
atexit.register(lightsOut)


# Main program logic follows:
if __name__ == '__main__':
    try:
        print "Turning on motion sensor..."

        # Loop until PIR indicates nothing is happening
        while GPIO.input(PIR)==1:
            Current_State  = 0

        print "Sensor ready, Waiting for movement..."

        while True:
            motion = GPIO.wait_for_edge(PIR,GPIO.RISING, timeout=1000)
            if motion is None:
                pass
            else:
                print "Motion Detected!"
                print(msg)
                show_message(device, msg, fill="white", font=proportional(LCD_FONT))

    except KeyboardInterrupt:
        lightsOut()

        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
