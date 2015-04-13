import argparse
import os
import math
import time
import servo

class Arm:
    def __init__(self):
        self.init_servos()

    def init_servos(self):
        self.spoon_servo = servo.Servo(2)
        self.spoon_servo.start()

    def run(self):
        i = 0
        self.ease_spoon(180)
        while(1):
            pass
            # is_alive()
            # self.ease_spoon(0)

            # self.spoon_servo.terminate()
            # time.sleep(5)
            # self.ease_spoon(180)
            # i += 1


    def ease_spoon(self, deg):
        self.spoon_servo.angle_to.value = float(deg)
        print 'setting angle'
        print deg
        # self.spoon_servo.start()

a = Arm()
a.run()
