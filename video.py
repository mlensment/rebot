import cv2
import cv2.cv as cv

cap = cv2.VideoCapture(0)
width, height = 320, 320
cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, height)

print cap.isOpened()

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
