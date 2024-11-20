# Author: Siddardha Chelluri
# Github: SidCh1

# ===================================================================================================

# Problem:

import numpy as np

# Define matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])

# Question:
# 1. Compute the matrix product C = AB.
# 2. Compute the matrix product D = BA.
# 3. Verify if C is equal to D.

# ===================================================================================================

# Solution:

C = np.dot(A, B)
D = np.dot(B, A)

print("C = ", C)
print("D = ", D)

if np.all(C == D):
    print("C equals D")
else:
    print("C not equals D")
