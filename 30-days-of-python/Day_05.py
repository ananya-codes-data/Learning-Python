# Lists

# four collection data types in Python :

# 1. List
# collection which is ordered and changeable(modifiable)
# Allows duplicate members

# 2. Tuple
# collection which is ordered and unchangeable or unmodifiable(immutable)
# Allows duplicate members

# 3. Set
# collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set
# Duplicate members are not allowed

# 4. Dictionary
# ollection which is unordered, changeable(modifiable) and indexed
# No duplicate members


# How to Create a List

# Using list built-in function
# a = list("Ananya")

# Using square brackets, []
# b = [21, 12, True]

# Lists can have items of different data types

# Accessing List Items Using Positive Indexing
# list index always starts from zero

# test_1 = [12, 21, True, 22.10, "Ananya"]

# print(test_1[0])

# last_index = len(test_1) - 1
# print(test_1[last_index])

# Accessing List Items Using Negative Indexing
# Negative indexing means beginning from the end,
# -1 refers to the last item,
# -2 refers to the second last item

# Unpacking List Items


# Slicing Items from a List
# numbers = [0, 1, 2, 3, 4, 5, 6, 7]

# print(numbers[0:3])     # [0, 1, 2]
# print(numbers[2:])      # [2, 3, 4, 5, 6, 7]
# print(numbers[:5])      # [0, 1, 2, 3, 4]
# print(numbers[:])      # [0, 1, 2, 3, 4, 5, 6, 7]

# Modifying Lists
# random = [22, 64, 78, 73, 89]
# random[3] = 56
# print(random)   # [22, 64, 78, 56, 89]

# Checking Items in a List - using 'in' operator
# test_1 = [12, 21, True, 22.10, "Ananya"]
# check = "Ananya" in test_1
# print(check)    # True
# check_1 = 836 in test_1
# print(check_1)      # False

# Adding Items to a List
# To add item to the end of an existing list

# random_1 = [234, 45, 78, 90, 61, 27]
# random_1.append(2210)
# print(random_1)     # [234, 45, 78, 90, 61, 27, 2210]

# Inserting Items into a List
# insert a single item at a specified index in a list
# list.insert(index, item)

# random_2 = [23, 39, 87, 67, 12, 890]
# random_2.insert(3, 43)
# print(random_2)     # [23, 39, 87, 43, 67, 12, 890]

# Removing Items from a List
# removes a specified item from a list
# random_3 = [34, 56, 78, 90, 32, 43]
# random_3.remove(78)
# print(random_3)     # [34, 56, 90, 32, 43]

# Removing Items Using Pop
# removes the specified index, 
# (or the last item if index is not specified)
# list.pop() -- last item
# list.pop(index)
# random_4 = [87, 65, 69, 31, 453, 689]
# random_4.pop(4)
# print(random_4)     # [87, 65, 69, 31, 689]
# random_4.pop()
# print(random_4)     # [87, 65, 69, 31]

# Removing Items Using Del
# The del keyword removes the specified index 
# and it can also be used to delete items within index range
# It can also delete the list completely
# del list[index]   # only single item
# del list      # to delete the list completely
# del list [index:index]        # this deletes items from given indexes

# test_2 = [25, 81, 49, 61, 75, 43]
# del test_2[2]
# print(test_2)     # [25, 81, 61, 75, 43]
# del test_2[1:3]
# print(test_2)    # [25, 75, 43]
# del test_2
# print(test_2)   # NameError: name 'test_2' is not defined

# Clearing List Items -- empties the list but the list still exists
# name = ["Rahul", "Amit", "Sneha", "Hannah"]
# name.clear()
# print(name)     # []

# Copying a List
# simply doing list_1 = list_2 won't help much
# any change in list_2 will also be reflected in list_1
# to avoid that we use copy()
# test_3 = [23, 45, 67, 89, 12, 34]
# test_4 = test_3
# print(test_4)       # [23, 45, 67, 89, 12, 34]
# test_4.append(82)
# print(test_4)       # [23, 45, 67, 89, 12, 34, 82]
# print(test_3)       # [23, 45, 67, 89, 12, 34, 82]

# using copy()
# test_3 = [23, 45, 67, 89, 12, 34]
# test_4 = test_3.copy()
# print(test_4)     # [23, 45, 67, 89, 12, 34]
# test_4.append(82)
# print(test_4)     # [23, 45, 67, 89, 12, 34, 82]
# print(test_3)     # [23, 45, 67, 89, 12, 34]
# using copy() does not change the original list


# Joining Lists
    # Plus Operator (+)
# random_1 = [21, 12]
# random_2 = [22, 10, 20, 1]
# random_join = random_1 + random_2
# print(random_join)    # [21, 12, 22, 10, 20, 1]

    # extend()
# random_1.extend(random_2)
# print(random_1)   # [21, 12, 22, 10, 20, 1]

# random_3 = [12, 23, 34]
# random_4 = [45, 56, 67]
# random_5 = [78, 89, 90]
# random_3.extend(random_4)
# random_3.extend(random_5)
# print(random_3)     # [12, 23, 34, 45, 56, 67, 78, 89, 90]

# Counting Items in a List
# count() returns the number fo times an item appears in a list
# random_6 = [12, 34, 56, 0, 1, 12, 1, 1]
# number = random_6.count(1)
# print(number)        # 3

# Finding Index of an Item
# index() method returns the index of first occurence of an item in the list
# position = random_6.index(12)
# print(position)   # 0

# Reversing a List
# reverse() method reverses the order of a list
# random_7 = [0, 1, 2, 3, 4, 5, 6, 7]
# random_7.reverse()
# print(random_7)     # [7, 6, 5, 4, 3, 2, 1, 0]

# Sorting List Items
# To sort lists we can use sort() method or sorted() built-in functions
# The sort() method reorders the list items in ascending order 
# and modifies the original list
# If an argument of sort() method reverse is equal to true,
# it will arrange the list in descending order.

# random_8 = [32, 24, 80, 64, 72]
# random_8.sort()
# print(random_8)     # [24, 32, 64, 72, 80]
# random_8.sort(reverse=True)
# print(random_8)         # [80, 72, 64, 32, 24]

# print(sorted(random_8))     # [24, 32, 64, 72, 80]
# print(sorted(random_8,reverse=True))        # [80, 72, 64, 32, 24]


# Exercises: Day 5

# Exercises: Level 1

