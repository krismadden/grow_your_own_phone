
import time
# import os
import RPi.GPIO as GPIO
import serial

import neopixel

LED_COUNT   = 14      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

strip = neopixel.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
# Intialize the library (must be called once before other functions).
strip.begin()

color = 

for i in range(strip.numPixels()):
		strip.neopixel.setPixelColor(i, Color(0, 0, 255))
		strip.neopixel.show()

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

def main():
	
	
	
	checkSignalStrength = True
	
	print("checking signal strength")
	
	while checkSignalStrength:
		ser.write("at+CSQ\r")
		response = ser.readlines(None)
		print(response)
		time.sleep(20.0)


if __name__ == "__main__":
    main()
