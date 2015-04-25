#!/usr/bin/python

import argparse
import config
from lib import camera, frame, eye, arm
# import eye
# import arm
import cv2
import time
import numpy

class Rebot:
    def __init__(self, frame_path = None):
        self.camera = camera.Camera(frame_path)
        self.arm = arm.Arm()
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

    def calibrate_camera(self):
        print '--> Initiating camera calibration sequence...'
        x_readings = []
        y_readings = []
        # beep / flash
        # time.sleep(1)
        # beep beep

        print '--> Calibrating camera...'
        while(len(x_readings) <= 10):
            frame = self.camera.read_frame()
            e = frame.find_eye()

            if e.is_visible():
                x_readings.append(e.x)
                y_readings.append(e.y)

        eye.Eye.target = (round(numpy.median(x_readings), 2), round(numpy.median(y_readings), 2))
        # print str(eye.Eye.target)

        # beep
        print '--> Camera calibration complete'

    def run(self):
        self.arm.init()
        self.calibrate_camera()

        # Wait for servos to calibrate
        print not self.arm.is_initialized()
        while(not self.arm.is_initialized()):
            if cv2.waitKey(1) & 0xFF == ord('/'):
                break

        print '--> Initiating main loop...'
        print '--> Rebot is running'
        while(1):
            frame = self.camera.read_frame()
            e = frame.find_eye()

            if e.is_visible():
                self.arm.update(e)

            # print e.is_looking_at_target()

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
