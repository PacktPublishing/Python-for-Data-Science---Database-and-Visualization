import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60]
])

res = np.sum(arr, axis=1)
print(res)
