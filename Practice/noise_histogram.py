import numpy as np
import matplotlib.pyplot as plt
import cv2

# Make grayscale image with rectangular black colours in open cv
img = np.zeros((512, 512), np.uint8)
cv2.rectangle(img, (100, 100), (400, 400), 100, -1)
cv2.circle(img, (256, 256), 100, 200, -1)
# Save the images
cv2.imwrite('rectangle.png', img)

# histogram of the numpy array
def Histogram(im):
    # remove negative values
    im = np.abs(im)
    image = np.array(im, dtype=np.uint8)
    hist_ = np.zeros((256,))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            hist_[image[i, j]] += 1
    
    plt.plot(hist_)
    plt.show()


# Make histogram of the image
Histogram(img)
    
# Add gaussian noise to the image
noise = np.random.normal(0, 10, img.shape)
noisy = img + noise
# Remove negative values
noisy = np.abs(noisy)
# Remove values greater than 255
noisy = np.where(noisy > 255, 255, noisy)
cv2.imwrite('noisy.png', noisy)


Histogram(noise)
   

# Histogram of the noisy image
Histogram(noisy)


   
