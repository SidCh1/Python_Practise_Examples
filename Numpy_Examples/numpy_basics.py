# Add

# import numpy as np

# a = [1, 2, 3]
# b = [5, 4, 7]

# c = np.add(a, b)

# print(c)

import numpy as np

# Step 1: Create two 3x3 matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Step 2: Add and Subtract Matrices
C = np.add(A, B)
D = np.subtract(A, B)

print("\nA + B:\n", C)
print("\nA - B:\n", D)

# Step 3: Element-wise Multiplication
E = np.multiply(A, B)

print("\nElement-wise Multiplication (A * B):\n", E)

# Step 4: Matrix Multiplication
F = np.dot(A, B)  # Alternatively: F = A @ B
print("\nMatrix Multiplication (A . B):\n", F)

# Step 5: Transpose of Matrix A
AT = np.transpose(A)

print("\nTranspose of A:\n", AT)

# Step 6: Combination: Transpose of A times B
G = np.dot(AT, B)  # Alternatively: G = AT @ B
F = AT @ B

print("\nTranspose of A multiplied by B (A^T . B):\n", F)


import numpy as np

# Step 1: Create a square matrix
A = np.array([[4, 2, 1], [3, 6, 2], [2, 1, 3]])

print("Matrix A:\n", A)

# Step 2: Calculate the Determinant
det_A = np.linalg.det(A)
print("\nDeterminant of A:", det_A)

# Step 3: Check if the matrix is invertible (determinant ≠ 0)
if det_A != 0:
    # Step 4: Calculate the Inverse of the Matrix
    A_inv = np.linalg.inv(A)
    print("\nInverse of A:\n", A_inv)
else:
    print("\nMatrix A is not invertible (determinant is zero).")

# Step 5: Calculate Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues of A:\n", eigenvalues)
print("\nEigenvectors of A:\n", eigenvectors)

# Step 6: Verify Eigenvector-Eigenvalue Relationship (A.v = λ.v)
for i in range(len(eigenvalues)):
    left_side = np.dot(A, eigenvectors[:, i])  # A * v
    right_side = eigenvalues[i] * eigenvectors[:, i]  # λ * v
    print(f"\nVerification for Eigenvalue {eigenvalues[i]}:")
    print("A.v:\n", left_side)
    print("λ.v:\n", right_side)
