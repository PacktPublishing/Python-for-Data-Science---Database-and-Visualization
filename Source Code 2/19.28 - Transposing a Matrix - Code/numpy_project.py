import numpy as np

arr = np.array([
   [
       [1, 2],
       [3, 4]
   ],
   [
       [5, 6],
       [7, 8]
   ]
])

transposed = arr.T

print("Original array: \n", arr)
print("Original array shape: ", arr.shape)
print("Transposed array: \n", transposed)
print("Transposed array shape: ", transposed.shape)
