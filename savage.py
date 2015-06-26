#------------------------------#
# SAVAGE - A RaspberryPi Robot #
#------------------------------#

import RPi.GPIO as gpio
import time

# Init Function
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)   # Front Left Motor
    gpio.setup(11, gpio.OUT)  # Front Right Motor
    gpio.setup(13, gpio.OUT)  # Rear Left Motor
    gpio.setup(15, gpio.OUT)  # Rear Right Motor

# Forward Motion Function with Time Variable
def forward(tf):
	init()
	gpio.output(7, False)
	gpio.output(11, True)
	gpio.output(13, True)
	gpio.output(15, False)
	time.sleep(tf)
	gpio.cleanup()

# Reverse Motion Function with Time Variable
def reverse(tf):
	init()
	gpio.output(7, True)
	gpio.output(11, False)
	gpio.output(13, False)
	gpio.output(15, True)
	time.sleep(tf)
	gpio.cleanup()

# Run Scripts with Time Variable - i.e. forward(2), reverse(2)
forward(2)
reverse(2)
