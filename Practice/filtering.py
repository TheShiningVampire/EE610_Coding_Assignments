# %%
from skimage import io,img_as_float
import numpy as np
import cv2
from scipy.signal import convolve2d
from scipy.ndimage import convolve

img = img_as_float(io.imread("images\\goi1.jpg" , as_gray = True))
kernel = np.ones((5,5) , dtype=np.float64)/25

gaussian_kernel = np.array([[1/16 , 1/8 , 1/16],
                            [1/8 , 1/4 , 1/8],
                            [1/16 , 1/8 , 1/16]])

conv_using_cv2 = cv2.filter2D(img , -1, kernel , borderType= cv2.BORDER_CONSTANT)

conv_using_scipy_signal = convolve2d(img, kernel , mode = "same")
conv_using_scipy_ndimage = convolve(img , kernel , mode = "constant")

conv = cv2.filter2D(img , -1, gaussian_kernel , borderType = cv2.BORDER_CONSTANT)

cv2.imshow("Original" , img )
cv2.imshow("cv2 filter" , conv_using_cv2)
cv2.imshow("Gaussian Kernel" , conv)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%

