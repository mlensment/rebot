import SimpleCV
import time
webcam_stream = SimpleCV.Camera(0,threaded=True)
start = time.time()
i = 0
while (time.time()-start)<1:
    raw_image = webcam_stream.getImage()
    i = i + 1
print(i)
