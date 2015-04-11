import argparse
import os
import math

class Arm:
    def __init__(self):
        # load driver, redirect stdout to /dev/null
        # although servoblaster seems to be writing errors to stdout too, instead of stderr...
        os.system("sudo killall servod && sudo ./../bin/servod 1> /dev/null")

        self.spoon_position = 0
        self.leg_position = 0

    def ease_spoon_to(self, deg):
        self.move_to(5, deg)

    def move_to(self, servo, deg):
        pwm = deg * 0.94 # 1 degree = 0.094ms high pulse time
        pwm += 50  # minimum high pulse time is 0.5 milliseconds

        if os.path.exists('/dev/servoblaster'):
            # os.system("echo 2=" + str(math.ceil(pwm)) + " > /dev/servoblaster")
            os.system("echo " + str(servo) + "=" + str(math.ceil(pwm)) + " > /dev/servoblaster")
        else:
            raise 'ERROR: Servo driver was not found. Is servoblaster loaded?'

# parser = argparse.ArgumentParser()
# parser.add_argument('--deg', required=True, type=int)
# args = parser.parse_args()
#
a = Arm()
a.move_to(5, 0)
a.ease_spoon_to(180)
