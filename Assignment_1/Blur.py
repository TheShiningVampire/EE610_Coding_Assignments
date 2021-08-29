# %%
import cv2
import numpy as np 
# %%

# Function to Implement Gaussian Blur
def GaussianBlur(path,size, sigma):
    img = cv2.imread(path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   # Convert image to HSV space
    # Split the HSV image into three channels 
    h, s, v = cv2.split(img_hsv)
    # Apply Gaussian blur to the V channel
    kernel = Gaussian_Mask(size, sigma)             # Get a gaussian mask of size with std dev sigma

    v_blur = Convolution(v, kernel)                 # Apply the gaussian mask to the V channel
    v_blur = np.uint8(v_blur)                       # Convert the V channel to 8 bit   
    img_blurred_hsv = cv2.merge((h, s, v_blur))     # Merge the HSV channels back together
    img_blurred = cv2.cvtColor(img_blurred_hsv, cv2.COLOR_HSV2BGR) # Convert image back to BGR space
    
    return img, img_blurred

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

# %%
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

img_rgb, img2 = GaussianBlur(path,100,50) 
cv2.imshow("Original Image", img_rgb)
cv2.imshow("Blurred Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%






# %%
# path = r'Images\house.tiff'
# img = cv2.imread(path)

# # Convert image to HSV space
# img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # Split the HSV image into three channels 
# h, s, img = cv2.split(img_hsv)
# # Apply Gaussian blur to the V channel


# kernel = np.array(
# [[0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]]
# )
# kernel = kernel / np.sum(kernel)

# kernel_dim = kernel.shape

# # Get the number of rows and columns of the kernel
# kernel_rows = kernel_dim[0]
# kernel_cols = kernel_dim[1]

# # Mirror pading on the image
# img_pad = img
# for i in range(max(kernel_rows//2, kernel_cols//2)):
#         img_pad = np.pad(img_pad, ((1,1),(1,1)), 'symmetric')

# # Initialize the output image
# img_out = np.zeros(img.shape)
# # %%
# # Apply the kernel to the image
# for i in range(0, img.shape[0]):
#     for j in range(0, img.shape[1]):
#         img_out[i, j] = np.sum(img_pad[i:i+kernel_rows, j:j+kernel_cols] * kernel)

# %%