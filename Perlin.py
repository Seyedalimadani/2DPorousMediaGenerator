import numpy as np
from noise import snoise2  # Install the "noise" package using pip beforehand 
import cv2
from PIL import Image as im
import os

# Define image size and Perlin noise parameters
width = 512
height = 512
octaves = 6
persistence = 0.5
lacunarity = 2.0
scale = 100.0


# Generate Perlin noise map
perlin_noise = np.zeros((height, width))
for y in range(height):
    for x in range(width):
        perlin_noise[y][x] = snoise2(x/scale, y/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)

# Threshold the Perlin noise map to create a binary image
threshold = 0
binary_image = np.where(perlin_noise > threshold, 1, 0)
binary_image = im.fromarray((binary_image * 255).astype(np.uint8))
binary_image.save('2D.png')

#smoothing image for ease of usage in the simulators and mesh proccesing
# Reading the image
image = cv2.imread('2D.png')
# Apply the bilateral filter to smooth the edges
averageBlur = cv2.blur(image, (5, 5))
gaussian = cv2.GaussianBlur(image, (3, 3), 0)
medianBlur = cv2.medianBlur(image, 9)
os.remove('2D.png')
#Porosity Calculation by Median blur filter image
image_array = np.array(medianBlur)
dimension=image_array.size
blackpix=image_array.sum()
Porosity=1-(blackpix/(255*dimension))
print(Porosity)

cv2.imshow('Raw image', image)
cv2.imshow('Filtered image by Blur', averageBlur)
cv2.imshow('Filtered image by Gaussian', gaussian)
cv2.imshow('Filtered image by MedianBlur', medianBlur)
cv2.waitKey()
cv2.destroyAllWindows()
