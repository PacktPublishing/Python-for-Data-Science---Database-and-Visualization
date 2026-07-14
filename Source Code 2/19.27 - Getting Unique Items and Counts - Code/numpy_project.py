import numpy as np

scores = np.array([
   [85, 90, 78],
   [92, 88, 92],
   [85, 90, 78],
   [78, 85, 90]
])

unique_scores, counts = np.unique(scores, axis=0, return_counts=True)
print(unique_scores)
print("Count: ", counts)

