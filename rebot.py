from SimpleCV import *
cam = Camera(0, {"width":640, "height":480})

while True:
    img = cam.getImage()
    bm = BlobMaker()
    blobs = bm.extractFromBinary(img.invert().binarize(thresh=240).invert(),img)

    if(len(blobs) > 0):
        blobs[0].draw()
        locationStr = "("+str(blobs[0].x)+","+str(blobs[0].y)+")"
        img.dl().text(locationStr,(0,0),color=Color.RED)
    
    rotate = img.rotate(-45);
    rotate.show()
