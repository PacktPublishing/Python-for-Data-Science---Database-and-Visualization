import numpy as np
import string

# arr = np.array([chr(int(i)) for i in np.arange(65,91)], dtype=str)
# print(arr)

letters = string.ascii_uppercase
arr = np.array(list(letters))
print(arr)
