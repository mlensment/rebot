import argparse
import os
import math
import time
import camera, frame
import cv2


class Arm:
    def __init__(self):
        # load driver, redirect stdout to /dev/null
        # although servoblaster seems to be writing errors to stdout too, instead of stderr...
        # os.system("sudo killall servod && sudo ./../bin/servod 1> /dev/null")

        self.spoon_position = 60
        # temp
        self.camera = camera.Camera()
        cv2.namedWindow('frame')
        cv2.moveWindow('frame', 100, 100)

        cv2.namedWindow('2')
        cv2.moveWindow('2', 500, 100)

        cv2.namedWindow('3')
        cv2.moveWindow('3', 1000, 100)

        cv2.namedWindow('4')
        cv2.moveWindow('4', 100, 500)


    def ease_spoon_to(self, deg):
        start_position = self.spoon_position
        end_position = deg
        millis = int(round(time.time() * 1000))

        direction = 'asc'
        if self.spoon_position > deg:
            direction = 'desc'

        while(1):
            frame = self.camera.read_frame()
            frame.find_glints()

            elapsed_time = int(round(time.time() * 1000)) - millis

            self.spoon_position = self.ease_in_out_sine(elapsed_time, start_position, end_position, 5000)

            if math.ceil(self.spoon_position) >= deg and direction == 'asc':
                break

            if math.floor(self.spoon_position) <= deg and direction == 'desc':
                break

            if self.spoon_position > 250:
                self.spoon_position = 250
            elif self.spoon_position < 50:
                self.spoon_position = 50

            # print str(self.spoon_position) + " - " + str(elapsed_time) + " - " + str(start_position) + " - " + str(end_position)
            self.move_to(2, self.spoon_position)

    def ease_in_out_sine(self, elapsed_time, begin, end, timeframe):
        b = begin
        c = math.fabs(end - begin)
        begin = 0

        pos = -c / 2 * (math.cos(math.pi * elapsed_time / timeframe) - 1)

        if b > end:
            return math.fabs(pos - b)
        else:
            return pos + b


        # c = math.abs(c - b)
        # b = 0
        #
        # return -c / 2 * (math.cos(math.pi * t / d) - 1) + b

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
print 'easing to 60'
a.ease_spoon_to(60)
print 'easing to 250'
a.ease_spoon_to(250)
print 'easing to 60'
a.ease_spoon_to(60)
print 'easing to 250 last'
a.ease_spoon_to(250)
a.ease_spoon_to(60)

# a.camera.close()
# cv2.destroyAllWindows()
