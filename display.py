from SimpleCV import*
cam = Camera(0, {"width":640, "height":480})
while True:
   img = cam.getImage().grayscale().threshold(45)
   blob = img.findBlobs()
   img.show()
