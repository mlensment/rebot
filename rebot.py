#!/usr/bin/python

import argparse
import config
from lib import camera, frame, eye, arm, config
# import eye
# import arm
import cv2
import time
import numpy
import RPi.GPIO as GPIO

class Rebot:
    def __init__(self, frame_path = None):
        print '---------- BOOT LOG -----------'
        print '--> Starting Rebot...'
        self.camera = camera.Camera(frame_path)
        self.arm = arm.Arm()

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(config.LED_PIN, GPIO.OUT)
        # self.arm = arm.Arm()

        if config.DEBUG:
            # create a window for displaying image and move it to a reasonable spot
            cv2.namedWindow(config.WINDOW_NAME)
            cv2.moveWindow(config.WINDOW_NAME, 100, 100)

    def calibrate_camera(self):
        print '--> Initiating camera calibration sequence...'
        GPIO.output(config.LED_PIN, 1)

        x_readings = []
        y_readings = []

        while(len(x_readings) <= 40):
            frame = self.camera.read_frame()
            e = frame.find_eye()

            if e.is_visible():
                x_readings.append(e.x)
                y_readings.append(e.y)

        eye.Eye.target = (round(numpy.median(x_readings), 2), round(numpy.median(y_readings), 2))
        # print str(eye.Eye.target)

        GPIO.output(config.LED_PIN, 0)
        time.sleep(2)
        print '--> Camera calibration complete'

    def run(self):
        # Indicate that initialization has started
        GPIO.output(config.LED_PIN, 1)
        time.sleep(.5)
        GPIO.output(config.LED_PIN, 0)
        time.sleep(2)

        self.arm.init()
        self.calibrate_camera()

        # Wait for servos to calibrate
        while(not self.arm.is_initialized()):
            pass

        print '--> Initiating main loop...'
        GPIO.output(config.LED_PIN, 1)
        time.sleep(.5)
        GPIO.output(config.LED_PIN, 0)
        print '--> Rebot is running'
        print '---------- ACTION LOG ---------'
        try:
            while(1):
                frame = self.camera.read_frame()
                e = frame.find_eye()

                if e.is_visible():
                    self.arm.update(e)

                if e.is_looking_at_target():
                    GPIO.output(config.LED_PIN, 1)
                else:
                    GPIO.output(config.LED_PIN, 0)

                if cv2.waitKey(1) & 0xFF == ord('c'):
                    break
        except KeyboardInterrupt:
            pass

        print '-------- SHUT DOWN LOG --------'
        print '--> Received shut down signal'
        self.arm.shut_down()

        print '--> Finishing servo processes...'
        time.sleep(.1)
        while(self.arm.not_finished()):
            pass
        print '--> Servo processes finished'

        print '--> Shutting down camera...'
        self.camera.close()
        cv2.destroyAllWindows()
        print '--> Camera shut down finished'

        GPIO.output(config.LED_PIN, 0)
        print '--> Rebot will shut down NOW!'

parser = argparse.ArgumentParser(description='Rebot.')
parser.add_argument('--frame', nargs='?', const = 'frame.jpg', default = None, help = 'Path to frame you want to process.')
args = parser.parse_args()

r = Rebot(args.frame)
r.run()
