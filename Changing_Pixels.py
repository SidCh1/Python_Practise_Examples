# Author: Siddardha Chelluri
# Github: SidCh1

# ===================================================================================================

# Problem:

# You are given a 2D NumPy array representing a grayscale image. Write a function apply_threshold(image, threshold) that
# thresholds the image such that all pixel values below the threshold are set to 0 and all values equal to or above it are set to 255.


# Example Input:

# import numpy as np

# image = np.array([[100, 200, 50],
#                   [255, 180, 90],
#                   [120, 30, 70]])

# threshold = 100

# Example Output:

# array([[  0, 255,   0],
#        [255, 255,   0],
#        [255,   0,   0]])

# ===================================================================================================

# Solution 1: (not efficient)

import numpy as np


image = np.array([[100, 200, 50], [255, 180, 90], [120, 30, 70]])


def apply_threshold(image, threshold=200):

    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] < threshold:
                image[i][j] = 0
            else:
                image[i][j] = 255
    return image


apply_threshold(image, 100)
print(image)

# ===================================================================================================

# Solution 2: (efficient, using Numpy's vectorised operations)

import numpy as np

image = np.array([[100, 200, 50], [255, 180, 90], [120, 30, 70]])


def apply_threshold(image, threshold=200):
    # Use NumPy's vectorized operations for efficient computation
    return np.where(image < threshold, 0, 255)


# Apply the threshold and return a new array
thresholded_image = apply_threshold(image, 100)
print(thresholded_image)
