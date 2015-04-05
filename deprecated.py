# get rid of too bright pixels
# create gray background
# blank_image = np.zeros(img.shape, np.uint8)
# blank_image[:, :] = 100
#
# # create mask for too bright areas
# ret, mask = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)
#
# # paint all normal areas black on background
# img1_bg = cv2.bitwise_and(img, img, mask = mask_inv)
#
# # paint all bright areas black on foreground
# img2_fg = cv2.bitwise_and(blank_image, blank_image, mask = mask)
#
# # join two images
# img = cv2.add(img1_bg, img2_fg)
#
# cv2.imshow(config.WINDOW_NAME, img1_bg)
#
