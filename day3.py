# day3.py: NumPy basics
import numpy as np

# 1. Create arrays
arr = np.array([1, 2, 3, 4, 5])
print('arr:', arr)
print('arr dtype:', arr.dtype)

# 2. Arithmetic operations
print('arr + 10 =', arr + 10)
print('arr * 2 =', arr * 2)

# 3. Multi-dimensional arrays
mat = np.array([[1, 2], [3, 4], [5, 6]])
print('mat shape', mat.shape)
print('mat:
', mat)

# 4. Slice and indexing
print('mat[1, :] =', mat[1, :])
print('column 0:', mat[:, 0])

# 5. Stats
print('mean:', np.mean(arr))
print('std:', np.std(arr))
print('sum:', np.sum(arr))
