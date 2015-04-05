import config
import cv2
import cv2.cv as cv
import numpy as np

class Frame:
    def __init__(self, original):
        self.original = original
        self.processed = None
        self.printed = False

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
        self.processed = self.original.copy()
        img = cv2.cvtColor(self.processed, cv2.COLOR_BGR2GRAY)

        # get rid of too bright pixels
        # create gray background
        blank_image = np.zeros(img.shape, np.uint8)
        blank_image[:, :] = 100

        # create mask for too bright areas
        ret, mask = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        # paint all normal areas black on background
        img1_bg = cv2.bitwise_and(img, img, mask = mask_inv)

        # paint all bright areas black on foreground
        img2_fg = cv2.bitwise_and(blank_image, blank_image, mask = mask)

        # join two images
        img = cv2.add(img1_bg, img2_fg)

        cv2.imshow(config.WINDOW_NAME, img1_bg)

        # erode remaining white areas
        kernel = np.ones((10,10), np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

        cv2.imshow('4', img)

        # find edges
        # values 50, 130 work well
        edges = cv2.Canny(img, 40, 130)

        # kernel = np.ones((3,3), np.uint8)
        # edges = cv2.dilate(edges, kernel, iterations = 1)
        cv2.imshow('2', edges)

        # find contours
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

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
            if y < 50 or y > 250:
                break

            contour = i
            largest_area = area

        contour = contours[1]
        # if not self.printed:
        #     print len(contours)
        # self.printed = True

        if contour is not None and contour.any():
            (x,y),radius = cv2.minEnclosingCircle(contour)
            center = (int(x),int(y))
            radius = int(radius)
            img = cv2.circle(self.processed, center, radius,(0,255,0),2)
            img = cv2.circle(self.processed, center, 2,(0,0,255),2)
            #
            # cv2.drawContours(self.processed, contour, -1, (0,255,0), 3)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(self.processed, 'Largest contour area: ' + str(largest_area), (10,10), font, 0.5, (255,255,255), 2)
            cv2.putText(self.processed, 'Center of the contour: (' + str(x) + ', ' + str(y) + ')', (10,30), font, 0.5, (255,255,255), 2)
            cv2.putText(self.processed, 'Radius of the contour: ' + str(radius), (10,60), font, 0.5, (255,255,255), 2)

        cv2.imshow('3', self.processed)

        # cv2.imshow(config.WINDOW_NAME, img)
        # edges = cv2.Canny(img, 0, 200)
        # #
        # cv2.imshow(config.WINDOW_NAME, edges)

        # ret, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
        # #
        # contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(self.processed, contours, -1, (0,255,0), 3)
        #
        # if not self.printed:
        #     print len(contours)
        # self.printed = True


        # img = img[c1:c1+25,r1:r1+25]

    def show(self):
        cv2.imshow(config.WINDOW_NAME, self.processed)

    def show_original(self):
        cv2.imshow(config.WINDOW_NAME, self.original)
