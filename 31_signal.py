
import time
# import os
import RPi.GPIO as GPIO
import serial

	

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
