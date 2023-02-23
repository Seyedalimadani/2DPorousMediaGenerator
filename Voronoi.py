import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Define image size and Voronoi diagram parameters
width = 512
height = 512
n_points = 1000

# Generate random points
points = np.random.uniform(0, width, (n_points, 2))

# Generate Voronoi diagram
vor = Voronoi(points)

# Plot Voronoi diagram
fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='orange', line_width=0.1, line_alpha=1, point_size=0)
plt.xlim([0, width])
plt.ylim([0, height])
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
plt.show()

# Convert Voronoi diagram to binary image
pixels = np.zeros((height, width))
for i, region in enumerate(vor.regions):
    if -1 not in region:
        mask = np.zeros((height, width))
        polygon = np.array([vor.vertices[j] for j in region])
        polygon = polygon.astype(int)
        cv2.fillPoly(mask, [polygon], 1)
        pixels = np.logical_or(pixels, mask)

# Display the binary image
plt.imshow(pixels, cmap='gray')
plt.show()
