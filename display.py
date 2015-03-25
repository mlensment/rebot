from SimpleCV import*
cam = Camera(0, {"width":640, "height":480})
i = 0
while True:
   img = cam.getImage().grayscale().threshold(45)
   blob = img.findBlobs()
   i = i + 1
   print i
