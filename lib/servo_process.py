from multiprocessing import Process, Value, Manager
import time
import math
import os
import config
import servo

class ServoProcess(Process):
    def __init__(self):
        print '----> Loading servo driver...'
        # TODO: Start servod
        if not os.path.exists('/dev/servoblaster'):
            raise Exception('Servo driver was not found. Is servoblaster loaded?')
        print '----> OK'

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

        print '----> OK'
        self.initialized.value = True

        while(1):
            self.spoon.update()
            self.spoon.alter_pwm()

            self.leg.update()
            self.leg.alter_pwm()
