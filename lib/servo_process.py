from multiprocessing import Process, Value, Manager
import time
import math
import os
import config
import servo

class ServoProcess(Process):
    def __init__(self):
        Process.__init__(self)
        self.spoon = servo.Servo(2, 0.0)
        self.leg = servo.Servo(5, 20.0)

    def run(self):
        print 'entered run'

        while(1):
            self.spoon.update()
            self.spoon.alter_pwm()

            self.leg.update()
            self.leg.alter_pwm()

        print 'thread end'
        return 0
