from SimpleCV import *
cam = Camera(0, {"width":640, "height":640})

while True:
    img = cam.getImage()
    img = img.rotate(90)
    bm = BlobMaker()
    blobs = bm.extractFromBinary(img.invert().binarize(thresh=240).invert(),img)

    if(len(blobs) > 0):
        blobs[0].draw()
        locationStr = "("+str(blobs[0].x)+","+str(blobs[0].y)+")"
        img.dl().text(locationStr,(0,0),color=Color.RED)
    
    img.show()
