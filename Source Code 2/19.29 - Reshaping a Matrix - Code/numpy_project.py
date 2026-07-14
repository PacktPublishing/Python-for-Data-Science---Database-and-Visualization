import numpy as np

arr = np.array([
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12]
])

reshaped_arr = arr.reshape(4, 3)

print("Original: \n", arr)
print("Shape:", arr.shape)
print("Reshaped array: \n", reshaped_arr)
print("New shape: ", reshaped_arr.shape)
