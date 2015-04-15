from multiprocessing import Process, Value, Manager
import time
import math
import os
import config
import servo

class ServoProcess(Process):
    def __init__(self):
        Process.__init__(self)
        self.spoon = servo.Servo()

    def run(self):
        print 'entered run'

        while(1):
            pass
            self.spoon.update()
            self.spoon.alter_pwm()

        print 'thread end'
        return 0
