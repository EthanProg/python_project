import numpy as np
import cv2

# loading an image in grayscale
img = cv2.imread('C:\Users\liwenqing\Pictures\Camera Roll\PIC\images (2).jpg', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:     # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):         # wait for 's' key to save an exit
    cv2.imwrite('imagegray.png',img)
    cv2.destroyAllWindows()
