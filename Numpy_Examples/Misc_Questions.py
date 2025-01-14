# Question : Create a 3×3 numpy array of all True’s

import numpy as np

# ===================================================================================================

# Question 1 : Import numpy as np and see the version

print(np.__version__)

# ===================================================================================================


# Question 2 : Create a 1D array of numbers from 0 to 9
# Output : #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr0 = np.arange(10)
# array = np.arange(1, 11)  # start and stop
# array = np.arange(1, 10, 2)  # In steps of 2
print(arr0)

# ===================================================================================================

# Question 3: Create a 3×3 numpy array of all True’s

# arr = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
arr1 = np.full((3, 3), True, dtype=bool)
print(arr1)

# or
# np.full((9), True, dtype=bool).reshape(3,3)

# or
# np.ones((3,3), dtype=bool)

# or
# np.ones((9), dtype=bool).reshape(3,3)

# ===================================================================================================

# Question 4: Extract all odd numbers from array
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: array([1, 3, 5, 7, 9])

arr2 = np.arange(10)

arr3 = []
for arr in arr2:
    if arr % 2 != 0:
        arr3.append(arr)
print(arr3)

# or
# arr[arr % 2 == 1]

# ===================================================================================================

# Question 5: Replace all odd numbers in arr with -1
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])

# arr4 = np.arange(10)

# for arr in arr4:
#     if arr % 2 != 0:
#         arr.append(-1)
# print(arr3)
