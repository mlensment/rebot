#!/usr/bin/python

import argparse
import config
from lib import camera, frame
# import eye
# import arm
import cv2

class Rebot:
    def __init__(self, frame_path = None):
        self.camera = camera.Camera(frame_path)

        # create a window for displaying image and move it to a reasonable spot
        cv2.namedWindow(config.WINDOW_NAME)
        cv2.moveWindow(config.WINDOW_NAME, 100, 100)

        cv2.namedWindow('2')
        cv2.moveWindow('2', 500, 100)

        cv2.namedWindow('3')
        cv2.moveWindow('3', 1000, 100)

        cv2.namedWindow('4')
        cv2.moveWindow('4', 500, 100)

    def run(self):
        while(1):
            frame = self.camera.read_frame()
            frame.find_glints()
            # frame.show()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.close()
        cv2.destroyAllWindows()

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
