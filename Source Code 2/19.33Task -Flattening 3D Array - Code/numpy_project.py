import numpy as np

arr = np.array([
   [
       [1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]
   ],
   [
       [13, 14, 15, 16],
       [17, 18, 19, 20],
       [21, 22, 23, 24]
   ]
])
print("Original shape: \n", arr.shape)
flatten_arr = arr.reshape(-1,4)
print("Partially flattened shape:", flatten_arr.shape)
print(flatten_arr)
