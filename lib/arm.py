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
        # self.ease_spoon(180)
        while(1):
            time.sleep(5)
            self.spoon_servo.stop()
            pass
            # is_alive()
            # self.ease_spoon(0)

            # self.spoon_servo.terminate()
            # time.sleep(5)
            # self.ease_spoon(180)
            # i += 1

    # def scoop(self):
    #     return if self.scooping
    #     self.scooping = True
    #     self.spoon_servo.rotate_to(90, 2000) # rotate to 90 in 2 seconds
    #     self.leg_servo.rotate_to(0, 2000) # at the same time rotate to 0 in 2 seconds
    #     self.spoon_servo.rotate_to(0, 2000) # rotate to 0 in 2 seconds (scoop)
    #     self.leg_servo.sleep(2000) # sleep for 2 secs
    #     self.leg_servo.rotate_to(20, 2000) # rotate to 20 in 2 seconds

    def ease_spoon(self, deg):
        self.spoon_servo.angle_to.value = float(deg)
        print 'setting angle'
        print deg
        # self.spoon_servo.start()

a = Arm()
a.run()
