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
        self.processed = self.original
        img = cv2.cvtColor(self.processed, cv2.COLOR_BGR2GRAY)

        # get rid of too bright pixels
        # create gray background
        blank_image = np.zeros(img.shape, np.uint8)
        blank_image[:, :] = 30

        ret, mask = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        img1_bg = cv2.bitwise_and(img, img, mask = mask_inv)
        img2_fg = cv2.bitwise_and(blank_image, blank_image, mask = mask)

        img = cv2.add(img1_bg, img2_fg)
        # img = cv2.GaussianBlur(img,(5,5),0)
        cv2.imshow(config.WINDOW_NAME, img1_bg)

        kernel = np.ones((2,2),np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

        cv2.imshow('4', img1_bg)

        # threshold the image
        # img = cv2.GaussianBlur(img,(5,5),0)


        edges = cv2.Canny(img, 50, 130)
        cv2.imshow('2', edges)
        circles = cv2.HoughCircles(edges, cv.CV_HOUGH_GRADIENT, 1, 20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
        #
        # # circles = np.uint16(np.around(circles))
        #
        if(circles is not None and len(circles) > 0):
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
        #
        cv2.imshow('3', img)
        # ret, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
        # contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


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
