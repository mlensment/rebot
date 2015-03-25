from SimpleCV import *

cam = Camera(0, {"width":1280, "height":1024})
cam.getImage().save("/home/pi/test.jpg")
