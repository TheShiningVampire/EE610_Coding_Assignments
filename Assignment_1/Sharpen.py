# %%
import cv2
import numpy as np 
# %%
# Fuunction to sharpen a given image
def Sharpen(im,sharpness):
    img_bgr =  im                                                                       # Read the image using OpenCV 2 library 
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)                                  # Convert the image to HSV
    h, s, v = cv2.split(img_hsv)                                                        # Splitting the HSV image into its three channels
    image_blurred = GaussianBlur(img_bgr,3,2)                                           # Apply Gaussian blur to the image
    image_blurred_hsv = cv2.cvtColor(image_blurred, cv2.COLOR_BGR2HSV)                  # Convert the blurred image to HSV
    h_blurred, s_blurred, v_blurred = cv2.split(image_blurred_hsv)                      # Splitting the HSV image into its three channels
    v_blurred = np.float32(v_blurred)                                                   # Convert the V channel to float
    
    v_sharp = v + (v - v_blurred) * sharpness                                   # Add the sharpness to the V channel
    # Normalize v_sharp
    v_sharp = 255* v_sharp / np.max(v_sharp)
    v_sharp = np.uint8(v_sharp)
    img_sharpened_hsv = cv2.merge((h, s, v_sharp))                                      # Merge the HSV channels back together
    img_sharpened = cv2.cvtColor(img_sharpened_hsv, cv2.COLOR_HSV2BGR)                 # Convert the sharpened image back to BGR
    return img_sharpened

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





# %%

path = r'Images\house.tiff'
img = cv2.imread(path)
img2 = Sharpen(img,2) 
cv2.imshow("Log Transformed Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

