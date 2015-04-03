import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width, height = 320, 320
cap.set(3, width)
cap.set(4, height)

# create a window for displaying image and move it to a reasonable spot
cv2.namedWindow('frame')
cv2.moveWindow('frame', 100, 100)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # rotate frame
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
    rotated = cv2.warpAffine(frame, rotation_matrix, (width, height))

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', rotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
