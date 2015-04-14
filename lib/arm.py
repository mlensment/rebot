import argparse
import os
import math
import time
import servo

class Arm:
    def __init__(self):
        self.init_servos()
        # 'scooping', ''
        self.spoon_status = ''

    def init_servos(self):
        self.spoon_servo = servo.Servo(2)
        self.leg_servo = servo.Servo(5)
        self.spoon_servo.start()
        self.leg_servo.start()

    def run(self):
        i = 0
        # self.ease_spoon(180)
        self.spoon_servo.rotate(180, 2000)
        self.leg_servo.rotate(180, 2000)
        while(1):
            pass
            # self.scoop()
            # # time.sleep(.5)
            # # self.spoon_servo.rotate_instant(180)
            # self.update_spoon_status()

            # time.sleep(5)
            # self.spoon_servo.stop()
            # is_alive()
            # self.ease_spoon(0)

            # self.spoon_servo.terminate()
            # time.sleep(5)
            # self.ease_spoon(180)
            # i += 1



    def scoop(self):
        if self.spoon_status in ['scooping', 'finished_scooping']: return

        self.spoon_status = 'scooping'
        self.spoon_servo.rotate(90, 2000) # rotate to 90 in 2 seconds
        self.leg_servo.rotate(0, 2000) # at the same time rotate to 0 in 2 seconds
        self.spoon_servo.rotate(0, 2000) # rotate to 0 in 2 seconds (scoop)
        self.leg_servo.sleep(2000) # sleep for 2 secs
        self.leg_servo.rotate(20, 2000) # rotate to 20 in 2 seconds

    def update_spoon_status(self):
        if self.spoon_status == 'scooping' and self.spoon_servo.is_finished() and self.leg_servo.is_finished():
            self.spoon_status = 'finished_scooping'

a = Arm()
a.run()
