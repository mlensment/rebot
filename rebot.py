#!/usr/bin/python

import argparse
import config
from lib import camera, frame, eye
# import eye
# import arm
import cv2
import time

class Rebot:
    def __init__(self, frame_path = None):
        self.camera = camera.Camera(frame_path)
        # self.arm = arm.Arm()

        # create a window for displaying image and move it to a reasonable spot
        cv2.namedWindow(config.WINDOW_NAME)
        cv2.moveWindow(config.WINDOW_NAME, 100, 100)

        cv2.namedWindow('2')
        cv2.moveWindow('2', 500, 100)

        cv2.namedWindow('3')
        cv2.moveWindow('3', 1000, 100)

        cv2.namedWindow('4')
        cv2.moveWindow('4', 100, 500)

    def calibrate(self):
        print '-----> Initiating calibration sequence...'
        readings = []
        # beep / flash
        # time.sleep(1)
        # beep beep

        print '-----> Calibrating...'
        while(len(readings) <= 10):
            frame = self.camera.read_frame()
            e = frame.find_eye()

            if e:
                readings.append((e.x, e.y))

        x_sum = 0.0
        y_sum = 0.0
        for i in readings:
            x_sum = i[0] + x_sum
            y_sum = i[1] + y_sum

        eye.Eye.target = (round(x_sum / len(readings), 2), round(y_sum / len(readings), 2))
        print str(eye.Eye.target)

        # beep
        print '-----> Calibration complete'

    def run(self):
        self.calibrate()

        print '-----> Initiating main loop...'
        while(1):
            frame = self.camera.read_frame()
            e = frame.find_eye()
            print e.is_looking_at_target()
            time.sleep(.5)

            if cv2.waitKey(1) & 0xFF == ord('/'):
                break

        # self.camera.close()
        # cv2.destroyAllWindows()

        # eye = frame.find_eye()
        # if eye.looks_at_target():
        #     arm.eat()
        # else:
        #     arm.take_food()

parser = argparse.ArgumentParser(description='Rebot.')
parser.add_argument('--frame', nargs='?', const = 'frame.jpg', default = None, help = 'Path to frame you want to process.')
args = parser.parse_args()

r = Rebot(args.frame)
r.run()
