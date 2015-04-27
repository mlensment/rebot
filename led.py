import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(25, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.output(25,True) #

time.sleep(5)
GPIO.output(25,False) #
