from multiprocessing import Process, Value, Manager
import time
import math
import os
import config
import servo

class ServoProcess(Process):
    def __init__(self):
        print '----> Initializing servo process...'
        if not os.path.exists('/dev/servoblaster'):
            raise Exception('Servo driver was not found. Is servoblaster loaded?')

        Process.__init__(self)
        self.spoon = servo.Servo(2, 0.0)
        self.leg = servo.Servo(5, 0.0)
        self.initialized = Value('b', False)

    def run(self):
        print '----> Calibrating servos...'

        i = config.SERVO_MAX_WIDTH - config.SERVO_MIN_WIDTH
        while(i > 0):
            self.spoon.decrease_pwm(10)
            self.leg.decrease_pwm(10)
            i -= 10

        self.initialized.value = True
        print '----> Servo calibration complete'
        print '----> Servo process initialized'

        while(1):
            self.spoon.update()
            self.spoon.alter_pwm()

            self.leg.update()
            self.leg.alter_pwm()
