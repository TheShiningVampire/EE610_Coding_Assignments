# %%
import cv2
import numpy as np 
# %%
def Log_Transformation(path):
    """ Function for Log transformation of an image.

    Args:
        path (string): Path of the image to be gamma corrected
    Returns:
        img_rgb (np.array): Original Image without log transformation
        img (np.array): Original Image with log transformation 
    """
    img_bgr =  cv2.imread(path)                                                         # Read the image using OpenCV 2 library 
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)                                  # Convert the image to HSV
    h, s, v = cv2.split(img_hsv)                                                        # Splitting the HSV image into its three channels
    v = np.float32(v)                                                                   # Convert the V channel of image to float
    v = np.log10(1 + v)                                                                 # Log transformation of V channel
    v = 255.0 * v/(np.max(v))                                                           # Normalization of V channel
    v = np.uint8(v)                                                                     # Convert the V channel of image to integer
    img_corrected = cv2.merge((h, s, v))                                                # Merge the HSV channels of image
    img_corrected_bgr = cv2.cvtColor(img_corrected, cv2.COLOR_HSV2BGR)                  # Convert the image to BGR

    return img_bgr, img_corrected_bgr                                                    # Return the original image and the gamma corrected image     
# %%

path = r'Images\house.tiff'
img_rgb, img2 = Log_Transformation(path) 
cv2.imshow("Original Image", img_rgb)
cv2.imshow("Log Transformed Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
