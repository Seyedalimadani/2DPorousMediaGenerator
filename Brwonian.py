import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import gaussian

# Define image size and fBM parameters
width = 512
height = 512
H = 0.8
octaves = 6
frequency_factor = 2
amplitude_factor = 0.5

# Generate fBM noise
noise = np.zeros((height, width))
for octave in range(octaves):
    frequency = frequency_factor ** octave
    amplitude = amplitude_factor ** octave
    noise += amplitude * gaussian(np.random.randn(height, width), sigma=1) * frequency ** (-H)

# Normalize noise to [0, 1]
noise -= noise.min()
noise /= noise.max()

# Threshold noise to create binary image
threshold = 0.6
binary_image = np.where(noise > threshold, 1, 0)

# Display binary image
plt.imshow(binary_image, cmap='gray')
plt.show()
