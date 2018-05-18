import time
# import os
import RPi.GPIO as GPIO
import serial


#setup LEDs#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#left bottom pins near power usb mini after ground
1bar = 6
2bar = 13
3bar = 19
4bar = 26

GPIO.setup(1bar,GPIO.OUT)
GPIO.setup(2bar,GPIO.OUT)
GPIO.setup(3bar,GPIO.OUT)
GPIO.setup(4bar,GPIO.OUT)

GPIO.output(1bar,GPIO.LOW)
GPIO.output(2bar,GPIO.LOW)
GPIO.output(3bar,GPIO.LOW)
GPIO.output(4bar,GPIO.LOW)

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
