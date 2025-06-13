import numpy as np
data = ([[1, 2, 3, 4], [5,4,5,6]])


arr = np.array(data)

print(type(arr))
print(arr.min(axis=0))
print(arr.dtype)
print(arr.ndim)