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

# TODO: try with example

# Clearing List Items
name = ["Rahul", "Amit", "Sneha", "Hannah"]
name.clear()
print(name)     # []

# Copying a List

