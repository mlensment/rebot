from multiprocessing import Process, Value, Manager
import time
import math
import os
import config
import servo

class ServoProcess(Process):
    def __init__(self):
        print '----> Loading servo driver...'
        os.system("sudo bin/servod --step-size 2> /dev/null")

        if not os.path.exists('/dev/servoblaster'):
            raise Exception('Servo driver was not found. Is servoblaster loaded?')
        print '----> Servo driver loaded'

        Process.__init__(self)
        self.spoon = servo.Servo(config.SPOON_SERVO_ID)
        self.leg = servo.Servo(config.LEG_SERVO_ID)
        self.initialized = Value('b', False)

    def run(self):
        print '----> Initiating servo calibration sequence...'

        i = config.SERVO_MAX_WIDTH - config.SERVO_MIN_WIDTH
        while(i > 0):
            self.spoon.decrease_pwm(10)
            self.leg.decrease_pwm(10)
            i -= 10

        print '----> Servo calibration complete'
        self.initialized.value = True

        while(1):
            self.spoon.update()
            self.spoon.alter_pwm()

            self.leg.update()
            self.leg.alter_pwm()
