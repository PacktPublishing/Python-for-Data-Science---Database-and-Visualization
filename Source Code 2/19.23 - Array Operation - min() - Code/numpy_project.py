import numpy as np

arr = np.array([
   [
       [90, 45, 30],
       [20, 75, 60]
   ],
   [
       [15, 55, 25],
       [80, 5, 65]
   ]
])

res = np.min(arr, axis=0)
print(res)
