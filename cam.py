from SimpleCV import *
cam = Camera(0, {"width":640, "height":640})

while True:
    img = cam.getImage()
    img = img.rotate(90)

    blob_maker = BlobMaker()
    orig_img = img.colorDistance(Color.WHITE)
    b_img = orig_img.binarize(230)
    b_img.show()
    # m_img = b_img.morphOpen().morphClose()
    # inv_img = m_img.invert()
    # blobs = blob_maker.extractFromBinary(inv_img, orig_img)
    # if(len(blobs) > 0):
    #     # centroid = blobs[0].centroid()
    #     blobs[0].draw()
    # inv_img.show()

#
#
#
# blob_maker = BlobMaker()
# orig_img = image.colorDistance(Color.WHITE)
# b_img = orig_img.binarize(230)
# m_img = b_img.morphOpen().morphClose()
# inv_img = m_img.invert()
# blobs = blob_maker.extractFromBinary(inverted_img, orig_img)
# centroid = blobs[0].centroid()
