import numpy as np
import cv2
import cv2.cv as cv

cap = cv2.VideoCapture(0)
width, height = 320, 320
cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, height)

# create a window for displaying image and move it to a reasonable spot
cv2.namedWindow('frame')
cv2.moveWindow('frame', 100, 100)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # rotate frame
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
    rotated = cv2.warpAffine(frame, rotation_matrix, (width, height))

    # convert to grayscale
    gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)

    # threshold the image
    ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Display the resulting frame
    cv2.imshow('frame', thresh1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
