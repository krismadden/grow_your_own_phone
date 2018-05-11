#!/usr/bin/python

import serial
import time

class m590:
#	ser = serial.Serial("/dev/ttyAMA0", 128000, timeout=5)
	ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=5)
	SMS = {}
	PHONE = {}

	# Wait result
	def wait_result(self):
		lines = ""
		while True:
			ch = self.ser.read()
			if ch == '':
				return 2
			lines = lines + ch.decode()
			if lines[-3:]=="OK\r":
				return 0
			if lines[-6:]=="ERROR\r":
				return 1


	# Send Command to Modem and wait a Result
	def send_command(self, command):
		self.ser.write(command.encode())
		return self.wait_result()

	# Send SMS
	def send_sms(self, number, text):
		encodeThis = 'AT+CMGS=\"'+number+'\"\r'
		encodeThisToo = text
		self.ser.write(encodeThis.encode())
		#while True:
		#	ch = self.ser.read()
		#	if ch == '>':
        	#		break
		#	if ch == '':
		#		return 2
		time.sleep(0.5)
		self.ser.write(text.encode())
		self.ser.write('\x1A'.encode())
		return self.wait_result()

	# Init Modem
	def init(self):
		self.send_command("AT+CMGF=1\r")
		self.send_command("AT+CSMS=1\r")
		self.send_command('AT+CSCS=\"GSM\"\r')

	# Read SMS
	def read_sms(self, type=0):
		#type=0 - (REC UNREAD): received unread SMS
		#type=1 - (REC READ):   received read SMS
		#type=2 - (STO UNSENT): stored unsent SMS
		#type=3 - (STO SENT):   stored sent SMS
		#type=4 - (ALL):        all SMS
		self.ser.write("AT+CMGL="+str(type)+"\r")
		lines = ""
		while True:
			ch = self.ser.read()
			if ch == '':
				return 2
			lines = lines + ch
			if lines[-3:]=="OK\r":
				break
			if lines[-6:]=="ERROR\r":
				break

		#print "Done. All SMS: "+ lines
		# Parse SMS
		self.SMS = {}
		self.PHONE = {}
		lines=lines.split('\r\n')
		SMS_counter = 0
		SMS_phone = ""
		for line in lines:
			if SMS_phone != "":
				self.SMS[SMS_counter] = line
				self.PHONE[SMS_counter] = SMS_phone
				SMS_phone = ""
			if "+CMGL:" in line:
				SMS_phone = line.split(',')[2].replace('"','')
				SMS_counter =  SMS_counter + 1

	# Close Prt
	def deinit(self):
		self.ser.close()
