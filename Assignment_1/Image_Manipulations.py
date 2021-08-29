# %%
import cv2
import numpy as np 
import matplotlib.pyplot as plt 
# %%

################################################################################
## HISTOGRAM EQUALIZATION ##
################################################################################

# Function to implement Histogram Histogram_Equalization on image
def Histogram_Equalization(im):
    img = im                                                 # im is the original image
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
    
    return img_equalized


################################################################################
## GAMMA CORRECTION ##
################################################################################

# Function to implement Gamma Correction for the image
def Gamma_Correction(im,gamma):
    img_bgr = im                                                                        # im is the original image 
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)                                  # Convert the image to HSV
    h, s, v = cv2.split(img_hsv)                                                        # Split the HSV image into H, S, and V channels
    v = v.astype(np.float32)                                                            # Convert the V channel to float
    v = np.power(v, gamma)                                                              # Gamma correct the image
    v = 255.0 * (v)/(np.max(v))                                                         # Normalize the image
    v = v.astype(np.uint8)                                                              # Convert the image to unsigned 8 bit
    img_corrected_hsv = cv2.merge((h, s, v))                                            # Merge the HSV channels
    img_corrected_bgr = cv2.cvtColor(img_corrected_hsv, cv2.COLOR_HSV2BGR)              # Convert the image to BGR
    
    return img_corrected_bgr                                                   # Return the original image and the gamma corrected image     



##################################################################################
## LOG TRANSFORMATION ##
##################################################################################


def Log_Transformation(im):
    img_bgr =  im                                                                       # im is the original image 
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)                                  # Convert the image to HSV
    h, s, v = cv2.split(img_hsv)                                                        # Splitting the HSV image into its three channels
    v = np.float32(v)                                                                   # Convert the V channel of image to float
    v = np.log10(1 + v)                                                                 # Log transformation of V channel
    v = 255.0 * v/(np.max(v))                                                           # Normalization of V channel
    v = np.uint8(v)                                                                     # Convert the V channel of image to integer
    img_corrected = cv2.merge((h, s, v))                                                # Merge the HSV channels of image
    img_corrected_bgr = cv2.cvtColor(img_corrected, cv2.COLOR_HSV2BGR)                  # Convert the image to BGR

    return img_corrected_bgr                                                            # Return the original image and the gamma corrected image     


##################################################################################
## BLUR (GAUSSIAN BLUR) ##
##################################################################################


# Function to Implement Gaussian Blur
def GaussianBlur(im,size, sigma):
    img = im                                                                        # im is the original image          
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)                                  # Convert image to HSV space
    # Split the HSV image into three channels 
    h, s, v = cv2.split(img_hsv)
    # Apply Gaussian blur to the V channel
    kernel = Gaussian_Mask(size, sigma)                                             # Get a gaussian mask of size with std dev sigma

    v_blur = Convolution(v, kernel)                                                 # Apply the gaussian mask to the V channel
    v_blur = np.uint8(v_blur)                                                       # Convert the V channel to 8 bit   
    img_blurred_hsv = cv2.merge((h, s, v_blur))                                     # Merge the HSV channels back together
    img_blurred = cv2.cvtColor(img_blurred_hsv, cv2.COLOR_HSV2BGR)                  # Convert image back to BGR space
    
    return img_blurred

# Function to implement conolution between image and kernel
def Convolution(img, kernel):
    # Get the dimensions of the kernel
    kernel_dim = kernel.shape

    # Get the number of rows and columns of the kernel
    kernel_rows = kernel_dim[0]
    kernel_cols = kernel_dim[1]

    # Mirror pading on the image
    img_pad = img
    for i in range(max(kernel_rows//2, kernel_cols//2)):
            img_pad = np.pad(img_pad, ((1,1),(1,1)), 'symmetric')

    # Initialize the output image
    img_out = np.zeros(img.shape)
    
    # Apply the kernel to the image
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            img_out[i, j] = np.sum(img_pad[i:i+kernel_rows, j:j+kernel_cols] * kernel)
    return img_out

# Function to get a gaussian mask of a given size and std dev
def Gaussian_Mask(size, std):
    kernel = np.zeros((size, size), dtype=np.float32)
    X = np.arange(-size//2, size//2)
    Y = np.arange(-size//2, size//2)
    X, Y = np.meshgrid(X, Y)
    Z = np.exp(-(X**2 + Y**2)/(2*std**2))
    kernel = Z / np.sum(Z)
    return kernel