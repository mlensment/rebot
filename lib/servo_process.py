from multiprocessing import Process, Value, Manager
import time
import math
import os
import config
import servo

class ServoProcess(Process):
    def __init__(self):
        print '-----> Initializing servo process...'
        if not os.path.exists('/dev/servoblaster'):
            raise Exception('Servo driver was not found. Is servoblaster loaded?')

        Process.__init__(self)
        self.spoon = servo.Servo(2, 0.0)
        self.leg = servo.Servo(5, 0.0)

    def run(self):
        print '-----> Calibrating servos...'

        i = config.SERVO_MAX_WIDTH - config.SERVO_MIN_WIDTH
        while(i > 0):
            print i
            # self.spoon.decrease_pwm(1)
            # self.leg.decrease_pwm(1)
            i -= 1

        print '-----> Servo calibration complete'
        print '-----> Servo process initialized'

        while(1):
            self.spoon.update()
            self.spoon.alter_pwm()

            self.leg.update()
            self.leg.alter_pwm()
