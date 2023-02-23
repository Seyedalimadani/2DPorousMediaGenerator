import numpy as np
from noise import snoise2  # Install the "noise" package using pip

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
threshold = 0.3
binary_image = np.where(perlin_noise > threshold, 1, 0)

# Display the binary image
import matplotlib.pyplot as plt
plt.imshow(binary_image, cmap='gray')
plt.show()
