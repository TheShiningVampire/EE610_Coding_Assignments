# %%
import cv2
import numpy as np 
# %%

# Function to implement Gamma Correction for the image
def Gamma_Correction(a,gamma):
    img_bgr =  cv2.imread(a)                                                            # Read the image using OpenCV 2 library 
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)                                  # Convert the image to HSV
    h, s, v = cv2.split(img_hsv)                                                        # Split the HSV image into H, S, and V channels
    v = v.astype(np.float32)                                                            # Convert the V channel to float
    v = np.power(v, gamma)                                                              # Gamma correct the image
    v = 255.0 * (v)/(np.max(v))                                                         # Normalize the image
    v = v.astype(np.uint8)                                                              # Convert the image to unsigned 8 bit
    img_corrected_hsv = cv2.merge((h, s, v))                                            # Merge the HSV channels
    img_corrected_bgr = cv2.cvtColor(img_corrected_hsv, cv2.COLOR_HSV2BGR)             # Convert the image to BGR
    
    return img_bgr, img_corrected_bgr                                                    # Return the original image and the gamma corrected image     
# %%

img_rgb, img2 = Gamma_Correction("Images\house.tiff", 0)
cv2.imshow("Original Image", img_rgb)
cv2.imshow("Gamma corrected Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
