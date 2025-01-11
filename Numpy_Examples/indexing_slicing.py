import numpy as np


# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# # Slice the array from index 2 to index 5 (inclusive).
# # Slice the array starting from index 3 until the end.
# # Slice the array to include every second element.

# print(arr[2:6])
# print(arr[3:])
# print(arr[::2])

###################################################################################################

# arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# # Extract the first two rows and all columns.
# # Extract the last two rows and the first two columns.
# # Extract all rows but only the second column.

# print(arr_2d[:2])
# print(arr_2d[-2:, :2])
# print(arr_2d[:, 2])

###################################################################################################

# arr = np.array([10, 20, 30, 40, 50, 60, 70])
# arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])


# # Create a list of indices [0, 2, 4] and use it to select the corresponding elements from arr.
# # Select elements from the 2D array arr_2d based on row indices [0, 2] and column indices [1, 2].

# ind_list = [0, 2, 4]
# for i in ind_list:
#     print(arr[i])

# row_ind = [0, 2]
# col_ind = [1, 2]

# for i in row_ind:
#     for j in col_ind:
#         print(arr_2d[i, j])

# row_ind = [0, 2]
# col_ind = [1, 2]

# # Using np.ix_ to combine row and column indices for proper indexing
# print(arr_2d[np.ix_(row_ind, col_ind)])


###################################################################################################


# Boolean slicing

# Use boolean indexing to select all elements greater than 30.
# Use boolean indexing to replace all elements less than 30 with 0.

# arr = np.array([10, 20, 30, 40, 50, 60, 70])
# arr_30 = []
# for i in range(len(arr)):
#     if arr[i] > 30:
#         arr_30.append(arr[i])

# for i in range(len(arr)):
#     if arr[i] < 30:
#         arr[i] = 0


# arr = np.array([10, 20, 30, 40, 50, 60, 70])

# # Select all elements greater than 30 using boolean indexing
# arr_30 = arr[arr > 30]
# print("Elements greater than 30:", arr_30)

# # Replace all elements less than 30 with 0 using boolean indexing
# arr[arr < 30] = 0
# print("Modified array:", arr)


###################################################################################################


# def merge_sort(arr):
#     print(f"Splitting: {arr}")  # Trace the splitting of the array
#     if len(arr) <= 1:
#         print(f"Base case reached with: {arr}")  # Base case reached
#         return arr

#     # Split the array into two halves
#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])  # Recursively sort the left half
#     right_half = merge_sort(arr[mid:])  # Recursively sort the right half

#     # Merge the two sorted halves
#     merged = merge(left_half, right_half)
#     print(f"Merged {left_half} and {right_half} into {merged}")  # Trace merging
#     return merged


# def merge(left, right):
#     print(f"Start merging: {left} and {right}")  # Trace the arrays being merged
#     sorted_array = []
#     i = j = 0

#     # Compare elements from both halves and add the smallest to the sorted array
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             sorted_array.append(left[i])
#             print(f"Added {left[i]} from left")  # Trace adding from left
#             i += 1
#         else:
#             sorted_array.append(right[j])
#             print(f"Added {right[j]} from right")  # Trace adding from right
#             j += 1

#     # Append any remaining elements in the left or right half
#     if i < len(left):
#         print(f"Appending remaining from left: {left[i:]}")  # Trace leftovers
#     if j < len(right):
#         print(f"Appending remaining from right: {right[j:]}")  # Trace leftovers

#     sorted_array.extend(left[i:])
#     sorted_array.extend(right[j:])

#     print(f"Finished merging: {sorted_array}")  # Trace final merged array
#     return sorted_array


# # Example usage:
# if __name__ == "__main__":
#     array = [38, 27, 43, 3, 9, 82, 10]
#     print("Original Array:", array)
#     sorted_array = merge_sort(array)
#     print("Sorted Array:", sorted_array)
