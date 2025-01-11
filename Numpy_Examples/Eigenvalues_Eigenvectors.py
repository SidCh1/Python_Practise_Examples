# Author: Siddardha Chelluri
# Github: SidCh1

# ===================================================================================================

# Problem:

import numpy as np

# Define matrix
M = np.array([[4, -2], [1, 1]])

# Question:
# 1. Compute the eigenvalues of M.
# 2. Compute the eigenvectors of M.
# 3. Verify if Mv = λv for each eigenvalue λ and eigenvector v.

# ===================================================================================================

# Solution:

values, vectors = np.linalg.eig(M)

for i in range(2):

    if np.allclose(np.dot(M, vectors[:, i]), np.dot(values[i], vectors[:, i])):
        print(True)
    else:
        print(False)

# ===================================================================================================

# Solution 2: Optimal

eigen_system = np.linalg.eig(M)

values = eigen_system[0]
vectors = eigen_system[1]

for i in range(len(values)):
    # Verify Mv = λv using np.allclose() to account for floating point precision errors
    if np.allclose(np.dot(M, vectors[:, i]), values[i] * vectors[:, i]):
        print(f"Eigenvalue {values[i]} and Eigenvector {vectors[:, i]} satisfy Mv = λv")
    else:
        print(
            f"Eigenvalue {values[i]} and Eigenvector {vectors[:, i]} do not satisfy Mv = λv"
        )
