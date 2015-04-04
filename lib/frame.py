import config
import cv2
import numpy as np

class Frame:
    def __init__(self, original):
        self.original = original
        self.processed = None

    def process(self):
        # Frame can be processed only once...
        return if self.processed

        # convert to grayscale
        gray = cv2.cvtColor(self.original, cv2.COLOR_BGR2GRAY)

        # threshold the image
        ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        self.processed = thresh

    def show(self):
        cv2.imshow(config.WINDOW_NAME, self.processed)

    def show_original(self):
        cv2.imshow(config.WINDOW_NAME, self.original)
