import argparse
import os
import math
import time


class Arm:
    def __init__(self):
        # load driver, redirect stdout to /dev/null
        # although servoblaster seems to be writing errors to stdout too, instead of stderr...
        # os.system("sudo killall servod && sudo ./../bin/servod 1> /dev/null")

        self.spoon_position = 60
        self.spoon_next_pos = 0
        self.spoon_ease = 0.1
        # self.leg_position = 0

    def ease_spoon_to(self, deg):
        start_position = self.spoon_position
        end_position = deg
        millis = int(round(time.time() * 1000))

        direction = 'asc'
        if self.spoon_position > deg:
            direction = 'desc'

        while(1):
            elapsed_time = int(round(time.time() * 1000)) - millis

            self.spoon_position = self.ease_in_out_sine(self.spoon_position, elapsed_time, start_position, end_position, 5000)
            # self.spoon_position = math.ceil(self.spoon_position)
            # self.spoon_position += 1
            if self.spoon_position >= deg and direction == 'asc':
                break

            if self.spoon_position <= deg and direction == 'desc':
                break

            self.move_to(2, self.spoon_position)

    def ease_in_out_sine(self, x, t, b, c, d):
        return -c / 2 * (math.cos(math.pi * t / d) - 1) + b;
        # t = t / (d / 2.0)
        # if (t < 1):
        #      return c/2*t*t + b
        # ti = t - 1
        # return -c/2 * ((ti)*(t-3) - 1) + b

    def move_to(self, servo, deg):
        pwm = deg
        # pwm = deg * 0.94 # 1 degree = 0.094ms high pulse time
        # pwm += 50  # minimum high pulse time is 0.5 milliseconds

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
# a.move_to(5, 0)
a.ease_spoon_to(0)
a.ease_spoon_to(250)
a.ease_spoon_to(0)
a.ease_spoon_to(250)
