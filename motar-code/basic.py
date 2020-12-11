


'''

how l298 works what is dual bridge 


'''

'''

gnd connection raspi ke gnd ko female connector ayega male motar ko jayega 

'''

'''
import RPi.GPIO as GPIO 

from time import sleep 

GPIO.cleanup()      # remove any process if running 


motar1 = 18 
moatr2 = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motar1 , GPIO.OUT)
GPIO.setup(motar2,GPIO.OUT  )

'''


import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.cleanup()

Forward=26
Backward=20
sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

def forward(x):
	GPIO.output(Forward, GPIO.HIGH)
	print("Moving Forward")
	time.sleep(x)
	GPIO.output(Forward, GPIO.LOW)

def reverse(x):
	GPIO.output(Backward, GPIO.HIGH)
	print("Moving Backward")
	time.sleep(x)
	GPIO.output(Backward, GPIO.LOW)

while (1):

	forward(5)

	reverse(5)
	GPIO.cleanup()


