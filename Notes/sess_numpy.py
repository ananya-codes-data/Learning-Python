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

# Indexing

a1 = np.arange(10)
print(a1)   # [0 1 2 3 4 5 6 7 8 9]

a2 = np.arange(12).reshape(3,4)
print(a2)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a3 = np.arange(8).reshape(2, 2, 2)
print(a3)
# [[[0 1]
#   [2 3]]

#  [[4 5]
#   [6 7]]]

print(a1[-1])   # 9

print(a2[1, 2])     # 6

print(a2[2, 3])     # 11

print(a2[1, 0])     # 4

print(a3[1, 0, 1])      # 5

print(a3[0, 1, 0])      # 2

print(a3[0, 0, 0])      # 0

print(a3[1, 1, 0])      # 6


# Slicing

print(a1[2:5])      # [2 3 4]

print(a1[2:5:2])      # [2 4]

print(a1[2:7:2])      # [2 4 6]

print(a2[0,:])      # [0 1 2 3]

print(a2[:,2])      # [ 2  6 10]

print(a2[1:,1:3])
# [[ 5  6]
#  [ 9 10]]

print(a2[::2, ::3])
# [[ 0  3]
#  [ 8 11]]

print(a2[::2, 1::2])
# [[ 1  3]
#  [ 9 11]]

print(a2[1, ::3])      # [4 7]

print(a2[:2, 1:])
# [[1 2 3]
#  [5 6 7]]

a3 = np.arange(27).reshape(3, 3, 3)
print(a3)
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]

#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]

#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]

print(a3[1])
# [[ 9 10 11]
#  [12 13 14]
#  [15 16 17]]

print(a3[::2])
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]

#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]

print(a3[0, 1, :])      # [3 4 5]

print(a3[1, :, 1])      # [10 13 16]

print(a3[2, 1:, 1:])
# [[22 23]
#  [25 26]]

print(a3[::2, 0, ::2])
# [[ 0  2]
#  [18 20]]


# Iterating

for i in a1:
    if i % 2 == 0:
        print(i)
# 0
# 2
# 4
# 6
# 8

for i in a2:
    print(i)        # iterates and prints one row each time
# [0 1 2 3]
# [4 5 6 7]
# [ 8  9 10 11]

for i in a3:
    print(i)        # iterates and prints one 2d array each time
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# [[ 9 10 11]
#  [12 13 14]
#  [15 16 17]]
# [[18 19 20]
#  [21 22 23]
#  [24 25 26]]

for i in np.nditer(a3):
    print(i)    # converts into 1d and then prints every item
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26


# Reshaping

print(a2)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.transpose(a2))
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

print(a2.T)
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

print(a2.ravel())       # [ 0  1  2  3  4  5  6  7  8  9 10 11]


# Stacking

a4 = np.arange(12).reshape(3,4)
print(a4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a5 = np.arange(12,24).reshape(3,4)
print(a5)
# [[12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]

# horizontal stacking

print(np.hstack((a4, a5)))
# [[ 0  1  2  3 12 13 14 15]
#  [ 4  5  6  7 16 17 18 19]
#  [ 8  9 10 11 20 21 22 23]]

# vertical stacking

print(np.vstack((a4, a5)))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]


# Splitting

# horizontal splitting

print(np.hsplit(a4, 2))
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), 
# array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]

print(np.hsplit(a4, 4))
# [array([[0],
#        [4],
#        [8]]), 
# array([[1],
#        [5],
#        [9]]),
# array([[ 2],
#        [ 6],
#        [10]]),
# array([[ 3],
#        [ 7],
#        [11]])]


print(np.vsplit(a5, 3))     # [array([[12, 13, 14, 15]]), array([[16, 17, 18, 19]]), array([[20, 21, 22, 23]])]


# numpy advanced

# advanced indexing

# Normal Indexing and slicing

a = np.arange(12).reshape(4,3)
print(a)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

print(a[1,2])       # 5

print(a[1:3, 1:3])
# [[4 5]
#  [7 8]]

# Fancy indexing

print(a[[0, 2, 3]])
# [[ 0  1  2]
#  [ 6  7  8]
#  [ 9 10 11]]

print(a[:, [1, 2]])
# [[ 1  2]
#  [ 4  5]
#  [ 7  8]
#  [10 11]]

b = np.arange(24).reshape(6,4)
print(b)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]

print(b[[0,2,3,-1]])
# [[ 0  1  2  3]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [20 21 22 23]]

print(b[:, [0, 2, 3]])
# [[ 0  2  3]
#  [ 4  6  7]
#  [ 8 10 11]
#  [12 14 15]
#  [16 18 19]
#  [20 22 23]]

# boolean indexing

# sometimes we may need to filter out items on the basis of certain conditions at that point we would need boolean indexing

a = np.random.randint(1, 100, 24).reshape(6,4)

print(a)

# numbers greater than 50
print(a[a > 50])

# numbers which are even
print(a[a % 2 == 0])

# numbers greater than 50 and even
print(a[(a % 2 == 0) & (a > 50)])

# when we work with boolean values we have to use bitwise operators rather than logical operators

# numbers not divisible by 7
print(a[a % 7 != 0])