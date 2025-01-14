# Author: Siddardha Chelluri
# Github: SidCh1

# ===================================================================================================

# Problem:

# You are given a 2D NumPy array representing a matrix. Write a function rotate_matrix_90(matrix) such that the
# matrix should be rotated by 90 degrees clockwise.


# Example Input:

# 1 2 3
# 4 5 6
# 7 8 9

# Output:

# 7 4 1
# 8 5 2
# 9 6 3

# ===================================================================================================

# Solution 1:

# import numpy as np

# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# def rotate_matrix_90(matrix):
#     t_mat = np.transpose(matrix)
#     t_mat[:, [0, 2]] = t_mat[:, [2, 0]]
#     print(t_mat)


# rotate_matrix_90(matrix)

# ===================================================================================================

# Solution 2: Using the rot90 function from numpy.

import numpy as np


def rotate_matrix_90(matrix):
    """
    Rotates the given 2D NumPy array by 90 degrees clockwise.

    Args:
        matrix (np.ndarray): Input 2D matrix to be rotated.

    Returns:
        np.ndarray: Rotated 2D matrix.
    """
    return np.rot90(matrix, k=-1)  # Rotate 90 degrees clockwise


# Example Input
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Rotate the matrix
rotated_matrix = rotate_matrix_90(matrix)

# Print Output
print("Original Matrix:")
print(matrix)

print("\nRotated Matrix:")
print(rotated_matrix)

# ===================================================================================================
