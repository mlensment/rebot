from SimpleCV import*
cam = Camera(0, {"width":640, "height":480})
while True:
   img = cam.getImage()
   blob = img.findBlobs()
   print blob
   img.show()
