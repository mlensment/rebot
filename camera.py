import numpy as np
import cv2
import cv2.cv as cv

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.width, self.height = 320, 320
        self.cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, self.height)

    def read(self):
        ret, frame = self.cap.read()

        # rotate frame
        rotation_matrix = cv2.getRotationMatrix2D((self.width / 2, self.height / 2), 90, 1)
        rotated = cv2.warpAffine(frame, rotation_matrix, (self.width, self.height))

        return frame

    def snapshot(self, filename = 'shot.jpg'):
        cv2.imwrite(filename, self.read())
        self.close()

    def close(self):
        self.cap.release()
