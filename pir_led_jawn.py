#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from time import sleep

PIR_OUT_PIN = 11    # pin11
LedPin =  13   # pin13


def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(PIR_OUT_PIN, GPIO.IN)    # Set BtnPin's mode is input
	GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to turn off the led

def loop():
	while True:
		if GPIO.input(PIR_OUT_PIN) == GPIO.LOW:
			print '...Movement not detected!'
			GPIO.output(LedPin, GPIO.HIGH)
			time.sleep(0.5)
		else:
			print 'Movement detected!...'
			GPIO.output(LedPin, GPIO.LOW)  # led on
			time.sleep(0.5)

def destroy():
	GPIO.cleanup() # Release resource
	print('Program Canceled')

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

