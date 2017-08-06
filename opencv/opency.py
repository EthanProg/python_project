import numpy as np
import cv2

# Load an color image in grayscale
# cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
# Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
img = cv2.imread('C:\Users\liwenqing\Pictures\Camera Roll\PIC\slickeditbooksmall.jpg',1)
# print(img)

# Use the function cv2.imshow() to display an image in a window. The window automatically fits to the image size.
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()