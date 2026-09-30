#  session 4: Lists

# list comprehension

# add 1 to 10 numbers to a list

# method 1
# l = []

# for i in range(1, 11):
#     l.append(i)

# print(l)

# method 2

# l = [i for i in range(1, 11)]

# print(l)

# scalar multiplication on a vector

v = [2, 3, 4]
s = -3

# [-6, -9, -12]

# method 1
# x = []
# for i in v:
#     x.append(i*s)

# print(x)

# method 2
# print([i*s for i in v])

# numbers and their squares

# l = [1,2,3,4,5]

# method 1
# x = []

# for i in l:
#     x.append(i**2)

# print(x)

# method 2
# print([i**2 for i in l])

# Print all numbers divisible by 5 in the range of 1 to 50

# method 1
# l = []

# for i in range(1, 51):
#     if i % 5 == 0:
#         l.append(i)

# print(l)

# method 2
# print([i for i in range(1, 51) if i % 5 == 0])

# find languages which start with letter p
languages = ['java','python','php','c','javascript']

# method 1
x = []

# for i in languages:
#     if i.startswith('p'):
#         x.append(i)
# print(x)  # ['python', 'php']

# method 2
# print([i for i in languages if i.startswith('p')])    # ['python', 'php']


# Nested if with List Comprehension
basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'

# method 1
# e = []

# for i in my_fruits:
#     if i in basket and i.startswith('a'):
#         e.append(i)
# print(e)  # ['apple']

# method 2
# print([i for i in my_fruits if i in basket if i.startswith('a')])     # ['apple']

# Print a (3,3) matrix using list comprehension -> Nested List comprehension

# print([[i*j for i in range(1,4)] for j in range(1,4)])    # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# cartesian products -> List comprehension on 2 lists together
# L1 = [1,2,3,4]
# L2 = [5,6,7,8]

# print([i*j for i in L1 for j in L2])      # [5, 6, 7, 8, 10, 12, 14, 16, 15, 18, 21, 24, 20, 24, 28, 32]

# Write a program to add items of 2 lists indexwise

l1 = [1, 2, 3, 4]
l2 = [-1, -2, -3, -4]

# print(zip(l1, l2)) # <zip object at 0x000001E88F7A3940>

# print(list(zip(l1, l2))) # [(1, -1), (2, -2), (3, -3), (4, -4)]

# print([i + j for i,j in zip(l1, l2)]) # [0, 0, 0, 0]

l = [1, 2, print, type, input]
# print(l)    # [1, 2, <built-in function print>, <class 'type'>, <built-in function input>]


# Create 2 lists from a given list where 
# 1st list will contain all the odd numbers from the original list and
# the 2nd one will contain all the even numbers



# How to take list as input from user



# Write a program to merge 2 list without using the + operator
L1 = [1,2,3,4]
L2 = [5,6,7,8]



# Write a program to replace an item with a different item if found in the list 
L = [1,2,3,4,5,3]
# replace 3 with 300


# Write a program that can convert a 2D list to 1D list



# Write a program to remove duplicate items from a list

L = [1,2,1,2,3,4,5,3,4]



# Write a program to check if a list is in ascending order or not


t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

# print(zip(t1, t2))      # <zip object at 0x0000024888693940>

# print(list(zip(t1, t2)))       # [(1, 5), (2, 6), (3, 7), (4, 8)]     # list of tuples

print(tuple(zip(t1, t2)))       # ((1, 5), (2, 6), (3, 7), (4, 8))      # tuple of tuples - 2D