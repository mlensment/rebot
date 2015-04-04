import config
import cv2
import numpy as np

class Frame:
    def __init__(self, img):
        self.img = img

    def process(self):
        # convert to grayscale
        # gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        #
        # # threshold the image
        # ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        #
        # self.img = thresh
        pass

    def show(self):
        cv2.imshow(config.WINDOW_NAME, self.img)
