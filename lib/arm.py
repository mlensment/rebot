import argparse
import os
import math

class Arm:
    def __init__(self):
        # load driver, redirect stdout to /dev/null
        # although servoblaster seems to be writing errors to stdout too, instead of stderr...
        os.system("sudo killall servod && sudo ./../bin/servod 1> /dev/null")

    def move_to(self, deg):

        pwm = deg + 50  # minimum high pulse time is 0.5 milliseconds

        if os.path.exists('/dev/servoblaster'):
            os.system("echo 2=" + str(pwm) + " > /dev/servoblaster")
            os.system("echo 5=" + str(pwm) + " > /dev/servoblaster")
        else:
            raise 'ERROR: Servo driver was not found. Is servoblaster loaded?'

parser = argparse.ArgumentParser()
parser.add_argument('--deg', required=True, type=int)
args = parser.parse_args()

a = Arm()
a.move_to(args.deg)

180 - 180
1   -
