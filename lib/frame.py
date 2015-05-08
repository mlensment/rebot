import config
import cv2
import cv2.cv as cv
import numpy as np
# from pylab import array
import eye

class Frame:
    def __init__(self, original):
        self.original = original
        self.processed = None
        self.printed = False

    def find_eye(self):
        cv2.imshow('1', self.original)
        self.processed = self.original.copy()

        # convert to grayscale
        img = cv2.cvtColor(self.processed, cv2.COLOR_BGR2GRAY)

        # erode remaining white areas
        # kernel = np.ones((10, 10), np.uint8)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

        cv2.imshow('2', img)

        # find edges
        # values 50, 130 work well
        # values 40, 130 work well
        edges = cv2.Canny(img, 40, 130)
        cv2.imshow('3', edges)
        # find contours
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # find largest contour
        largest_area = 0
        contour = None
        for i in contours:
            area = cv2.contourArea(i)
            # find only largest contour
            if area < largest_area:
                continue

            # discard contours that are not in the center of the image
            # discard contours which bounding circle is too large
            (x,y),radius = cv2.minEnclosingCircle(i)
            if y < 50 or y > 280 or (x - radius) < 20 or radius > 30 or radius < 15:
                continue

            contour = i
            largest_area = area

        if contour is not None and contour.any():
            # find center and encosing circle
            (x,y), radius = cv2.minEnclosingCircle(contour)

            if config.DEBUG:
                center = (int(x), int(y))
                radius = int(radius)

                # draw the enclosing circle
                img = cv2.circle(self.processed, center, radius, (0, 255, 0), 2)

                # draw a red dot in the center of the circle
                img = cv2.circle(self.processed, center, 2, (0, 0, 255), 2)

                # write debug information
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(self.processed, 'Largest contour area: ' + str(round(largest_area, 2)), (10,30), font, 0.5, (255,255,255), 2)
                cv2.putText(self.processed, 'Center of the contour: (' + str(round(x, 2)) + ', ' + str(round(y, 2)) + ')', (10,60), font, 0.5, (255,255,255), 2)
                cv2.putText(self.processed, 'Radius of the contour: ' + str(round(radius, 2)), (10,90), font, 0.5, (255,255,255), 2)
                self.show()

            return eye.Eye(round(x, 2), round(y, 2))

        return eye.Eye()

    def show(self):
        cv2.imshow(config.WINDOW_NAME, self.processed)

    def show_original(self):
        cv2.imshow(config.WINDOW_NAME, self.original)
