import numpy as np
import cv2
import cv2.cv as cv
import frame

class Camera:
    # If Camera is initialized with frame_path, Camera will cache a Frame from disk for further reading
    # If image cannot be found from the disk, Camera snapshots a new image and caches it (TODO)
    def __init__(self, frame_path = None):
        self.cap = cv2.VideoCapture(0)
        self.width, self.height = 320, 320
        self.cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, self.height)
        self.cache_frame(frame_path)

    def cache_frame(self, frame_path):
        self.cached_frame = None
        if not frame_path: return
        img = cv2.imread(frame_path)
        self.cached_frame = frame.Frame(img)
        # self.cached_frame.process()

    # Reads raw frame
    def read(self):
        ret, frame = self.cap.read()

        # rotate frame
        rotation_matrix = cv2.getRotationMatrix2D((self.width / 2, self.height / 2), 90, 1)
        rotated = cv2.warpAffine(frame, rotation_matrix, (self.width, self.height))

        return frame

    # Reads raw frame and creates a Frame object
    def read_frame(self):
        if self.cached_frame:
            print self.cached_frame
            return self.cached_frame
        return frame.Frame(self.read())

    def snapshot(self, filename = 'shot.jpg'):
        cv2.imwrite(filename, self.read())
        self.close()

    def close(self):
        self.cap.release()
