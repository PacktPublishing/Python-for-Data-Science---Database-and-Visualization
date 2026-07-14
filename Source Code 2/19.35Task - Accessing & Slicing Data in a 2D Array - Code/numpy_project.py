import numpy as np

arr = np.arange(1,21).reshape(4,5)
print("Original array:\n", arr)

row_2 = arr[1]
print("\n2nd Row:", row_2)

col_4 = arr[:, 3]
print("4th Column:", col_4)

submatrix = arr[0:3, 1:4]
print("\nSubmatrix (Rows 1-3, Cols 2-4):\n", submatrix)

reversed_arr = np.flip(arr).reshape(-1)
print("\nReversed array:\n", reversed_arr)
