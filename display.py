from SimpleCV import*
cam = Camera()
while True:
   img = cam.getImage().grayscale().threshold(45)
   blob = img.findBlobs()
   print blob
   img.show()
