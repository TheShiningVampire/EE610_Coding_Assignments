# %%
import cv2
import numpy as np 
import matplotlib.pyplot as plt 
# %%
# Function to implement Histogram Histogram_Equalization on image
def Histogram_Equalization(path):
    img = cv2.imread(path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    
    h, s, v = cv2.split(img_hsv)                             # Split the image into H, S, and V channels

    v_hist = np.zeros(256, dtype=np.float32)                 # Make histogram of the V channel using a bin width of 1
    for i in range(v.shape[0]):
        for j in range(v.shape[1]):
            v_hist[v[i,j]] += 1

    v_hist = v_hist/v.size                                   # Normalize the histogram


    # Histogram Equalization
    cdf = v_hist.cumsum()                                   # cumulative distribution function          
    cdf = cdf * 255                                         
    cdf = cdf.astype(np.uint8)                              # Convert the CDF to a uint8 image
    # Apply the histogram to the V channel
    v_equalized = np.zeros(v.shape, dtype=np.uint8)         # Make a zero image of the same size as the V channel

    for i in range(v.shape[0]):
        for j in range(v.shape[1]):
            v_equalized[i,j] = cdf[v[i,j]]                  # Apply the CDF to the V channel to get the equalized V channel


    # Histogram of the v_equalized channel   (for debugging)      
    v_equalized_hist = np.zeros(256, dtype=np.float32)
    for i in range(v_equalized.shape[0]):
        for j in range(v_equalized.shape[1]):
            v_equalized_hist[v_equalized[i,j]] += 1

    v_equalized_hist = v_equalized_hist/v_equalized.size

    img_equalized = cv2.merge((h, s, v_equalized))          # Merge the channels
    img_equalized = cv2.cvtColor(img_equalized, cv2.COLOR_HSV2BGR)   # Convert the image to BGR
    
    return img,img_equalized

# %%
path = r'Images\5.3.01.tiff'
img_rgb, img_corrected = Histogram_Equalization(path) 
cv2.imshow("Original Image", img_rgb)
cv2.imshow("Histogram Equalized Image", img_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()
