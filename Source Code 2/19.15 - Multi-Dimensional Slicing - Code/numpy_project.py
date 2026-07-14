import numpy as np

arr = np.array([
   [
       [1, 2, 3],
       [4, 5, 6]
   ],
   [
       [10, 20, 30],
       [40, 50, 60]
   ]
])

sliced = arr[0, :, :2]
sliced[0,0] = 44
print(arr)
