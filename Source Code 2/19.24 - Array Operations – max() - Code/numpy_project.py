import numpy as np

arr = np.array([
   [
       [5, 40, 25],
       [60, 15, 50]
   ],
   [
       [10, 35, 30],
       [55, 75, 45]
   ]
])

res = np.max(arr, axis=1)
print(res)
