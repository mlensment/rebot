import numpy as np
import cv2
import cv2.cv as cv

cap = cv2.VideoCapture(0)
width, height = 320, 320
cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, height)

# Capture frame
ret, frame = cap.read()

# rotate frame
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
rotated = cv2.warpAffine(frame, rotation_matrix, (width, height))

cv2.imwrite('eye.jpg', frame)

# When everything done, release the capture
cap.release()
