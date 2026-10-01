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

# print(tuple(zip(t1, t2)))       # ((1, 5), (2, 6), (3, 7), (4, 8))      # tuple of tuples - 2D


s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# print(s1.union(s2))
# s1.update(s2)
# print(s1)
# print(s2)

# print 1st 10 numbers and their squares

# print({i: i**2 for i in range(1, 11)})      # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# using existing dict
distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}

# print({key: value*0.62 for (key, value) in distances.items()})      # {'delhi': 620.0, 'mumbai': 1240.0, 'bangalore': 1860.0}

# using zip
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

# print({i: j for (i, j) in zip(days, temp_C)})   # {'Sunday': 30.5, 'Monday': 32.6, 'Tuesday': 31.8, 'Wednesday': 33.4, 'Thursday': 29.8, 'Friday': 30.2, 'Saturday': 29.9}

# using if condition
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}

# print({i: j for (i,j) in products.items() if j > 0})    # {'phone': 10, 'charger': 32}

# Nested Comprehension
# print tables of number from 2 to 4

# print({i: {j: i*j for j in range(1, 11)} for i in range(2, 5)})

# {2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20}, 
# 3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15, 6: 18, 7: 21, 8: 24, 9: 27, 10: 30}, 
# 4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20, 6: 24, 7: 28, 8: 32, 9: 36, 10: 40}}


# # # # # # # #
# Functions   #
# # # # # # # #

# function to check even number

def is_even(num):
    """
    This function returns if a given number is odd or even
    input - any valid integer
    output - odd/even
    created on - 1st october 2026
    """
    if type(num) == int:
        if num % 2 == 0:
            return 'even'
        else:
            return 'odd'
    else:
        return 'inappropriate data type'

# function calling

for i in range(1, 11):
    x = is_even(i)
    print(f"{i} is {x}")

# 1 is odd
# 2 is even
# 3 is odd
# 4 is even
# 5 is odd
# 6 is even
# 7 is odd
# 8 is even
# 9 is odd
# 10 is even

