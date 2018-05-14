
import time
# import os
import RPi.GPIO as GPIO
import serial


#setup LEDs#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.output(23,GPIO.LOW)
#end setup for LEDs#




ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

def main():
	random = 0
	GPIO.output(23,GPIO.LOW)
	time.sleep(2)
	GPIO.output(23,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(23,GPIO.LOW)
	time.sleep(2)
	GPIO.output(23,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(23,GPIO.LOW)
	time.sleep(2)
	checkSignalStrength = True
	
	print("checking signal strength")
	
	while checkSignalStrength:
		ser.write("at+CSQ\r")
		response = ser.readlines(None)
		print(response)


if __name__ == "__main__":
    main()
