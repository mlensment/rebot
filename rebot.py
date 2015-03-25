from SimpleCV import *

cam = Camera(0, {"width":1280, "height":1024})
img = cam.getImage()
blobs = img.findBlobs()
blobs.draw()

img.save("/home/pi/test.jpg")
