import config
import cv2
import numpy as np

class Frame:
    def __init__(self, original):
        self.original = original
        self.processed = None

    def process(self):
        # Frame can be processed only once...
        if self.processed is not None: return self.processed

        # convert to grayscale
        gray = cv2.cvtColor(self.original, cv2.COLOR_BGR2GRAY)

        # threshold the image
        # ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY, 11, 2)

        # th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
        #     cv2.THRESH_BINARY,11,2)

        self.processed = thresh

    def find_glints(self):
        # convert to grayscale
        gray = cv2.cvtColor(self.original, cv2.COLOR_BGR2GRAY)

        # threshold the image
        ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        cv2.imshow(config.WINDOW_NAME, thresh)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        self.processed = cv2.drawContours(self.original, contours, -1, (0,255,0), 3)

        # img = img[c1:c1+25,r1:r1+25]

    def show(self):
        cv2.imshow(config.WINDOW_NAME, self.processed)

    def show_original(self):
        cv2.imshow(config.WINDOW_NAME, self.original)
