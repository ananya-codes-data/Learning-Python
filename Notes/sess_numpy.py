import numpy as np

# 1d array (vector)
a = np.array([1, 2, 3, 4])

print(a)    # [1 2 3 4]

print(type(a))      # <class 'numpy.ndarray'>

# 2d array (matrices)
b = np.array([[1, 2, 3], [4, 5, 6]])

print(b)
# [[1 2 3]
#  [4 5 6]]

# 3d array
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(c)
# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]

# dtype

d = np.array([1, 2, 3], dtype= float)

print(d)    # [1. 2. 3.]

# np.arange

print(np.arange(1, 11))     # [ 1  2  3  4  5  6  7  8  9 10]

print(np.arange(1, 11, 2))      # [1 3 5 7 9]

#  with reshape

print(np.arange(1, 11).reshape(5, 2))   # 5 rows 2 columns
# [[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]]

print(np.arange(1, 11).reshape(2, 5))   # 2 rows 5 columns
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

print(np.arange(1, 13).reshape(4, 3))   # 4 rows 3 columns
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

print(np.arange(1, 13).reshape(3, 4))   # 3 rows 4 columns
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(np.arange(1, 13).reshape(2, 6))   # 2 rows 6 columns
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]]

print(np.arange(1, 13).reshape(6, 2))   # 6 rows 2 columns
# [[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]
#  [11 12]]

# np.ones and np.zeros

print(np.ones((3,4)))
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# use case: to initialize values: deep learning (neural networks)

print(np.zeros((3,4)))
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

print(np.random.random((2,2)))      # random numbers between 0 and 1

# np.linspace (linear space)

print(np.linspace(-10, 10, 10))
# [-10.          -7.77777778  -5.55555556  -3.33333333  -1.11111111
#    1.11111111   3.33333333   5.55555556   7.77777778  10.        ]

print(np.linspace(-10, 10, 10, dtype= int))     # [-10  -8  -6  -4  -2   1   3   5   7  10]

# np.identity (identity matrix)
print(np.identity(3))
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

a1 = np.arange(10,dtype=np.int32)
print(a1)   # [0 1 2 3 4 5 6 7 8 9]

a2 = np.arange(12,dtype=float).reshape(3,4)
print(a2)
# [[ 0.  1.  2.  3.]
#  [ 4.  5.  6.  7.]
#  [ 8.  9. 10. 11.]]

a3 = np.arange(8).reshape(2,2,2)
print(a3)
# [[[0 1]
#   [2 3]]

#  [[4 5]
#   [6 7]]]

# Array attributes

# ndim

print(a1.ndim)  # 1
print(a2.ndim)  # 2
print(a3.ndim)  # 3

# shape

print(a1.shape)  # (10,)
print(a2.shape)  # (3, 4) -- 3 rows 4 columns
print(a3.shape)  # (2, 2, 2) -- 2 2d arrays of 2 rows 2 columns

# size

print(a1.size)  # 10
print(a2.size)  # 12
print(a3.size)  # 8

# itemsize

print(a1.itemsize)  # 4 bytes -- int 32
print(a2.itemsize)  # 8 bytes -- float
print(a3.itemsize)  # 8 bytes -- int 64

# dtype

print(a1.dtype)  # int32
print(a2.dtype)  # float64
print(a3.dtype)  # int64

# Changing data type

# astype

print(a3.astype(np.int32).dtype)    # int32


# Array operations

a1 = np.arange(12).reshape(3,4)
print(a1)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a2 = np.arange(12,24).reshape(3,4)
print(a2)
# [[12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]

# scalar operations

# arithmetic operations (+, -, *, /, //, **, %)
print(a1 ** 2)
# [[  0   1   4   9]
#  [ 16  25  36  49]
#  [ 64  81 100 121]]

# relational operators  (>, <, <=, >=, ==, !=)
print(a2 > 15)
# [[False False False False]
#  [ True  True  True  True]
#  [ True  True  True  True]]

# vector operations

# arithmetic
print(a1 + a2)
# [[12 14 16 18]
#  [20 22 24 26]
#  [28 30 32 34]]

# Array functions

a1 = np.random.random((3,3))
a1 = np.round(a1*100)
print(a1)

# max/ min/ sum/ prod

print(np.max(a1))
print(np.min(a1))
print(np.sum(a1))
print(np.prod(a1))

# 0 -> col and 1 -> row
print(np.max(a1, axis= 1))

# mean/ median/ std/ var

print(np.mean(a1))
print(np.median(a1))
print(np.std(a1))
print(np.var(a1))

print(np.mean(a1, axis= 1))

# trigonometric functions
print(np.sin(a1))

# dot product
a2 = np.arange(12).reshape(3,4)
print(a2)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a3 = np.arange(12,24).reshape(4,3)
print(a3)
# [[12 13 14]
#  [15 16 17]
#  [18 19 20]
#  [21 22 23]]

# np.dot

print(np.dot(a2, a3))

# log and exponents

print(np.log(a1))

print(np.exp(a1))

# round/ floor/ ceil
f1 = np.random.random((2, 3)) * 100
print(f1)

print(np.round(f1)) # rounding off to the next integer
print(np.floor(f1)) # round off to the smaller number
print(np.ceil(f1))  # round off to the larger number

# Indexing and Slicing

