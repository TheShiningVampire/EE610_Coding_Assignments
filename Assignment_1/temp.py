import cv2
from Image_Manipulations import *

path = r'Images\house.tiff'
img = cv2.imread(path)
img2 = Gamma_Correction(img,5) 
cv2.imshow("Log Transformed Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Previous_Image/prev_img.jpg", img2)