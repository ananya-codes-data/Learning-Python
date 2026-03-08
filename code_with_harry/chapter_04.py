# Lists and Tuples

# List
# containers to store a set of values of any data type
# unlike strings, lists are mutable i.e., it can be changed

# friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
# print(friends[0])

# friends[0] = "Grapes"

# print(friends[0])

# lists can be indexed like string
# print(friends[1:4])


# list methods

# in string when we use any method it would result in a new string, we have to print it
# but in list, the list itself gets changed and we don't have to print it

# print(friends)

# friends.append("Ananya")        # add any data at the end of the list

# print(friends)

l1 = [1, 34, 62, 2, 6, 11]

# l1.sort()       # sorting of numerical list in increasing order
# print(l1)

# l1.reverse()      # reversing the complete list
# print(l1)

# l1.insert(3, 2210)      # inserting element at particular index
# print(l1)               # insert 2210 such that its index in the list is 3

# print(l1.pop(3))      # prints the value at the index
# l1.pop(3)       # deletes element at the specific index
# print(l1)       # returns the new list as result

# l1.remove(34)       # removes a particular value from the list
# print(l1)


# Tuples
# similar to list but the only difference is tuple is immutable while list is mutable

# a = (1, 2, 5, 6)    # tuple
# print(type(a))      # checking the data type of a

# b = ()     # empty tuple
# print(type(b))        # checking the data type of b

# c = (1)     # here the data type will be integer
# print(type(c))      # checking the data type of c

# to have a single element in a tuple we have to put comma
# d = (1,)        # here it is a tuple with a single element
# print(type(d))      # checking the data type of d

# e = (1, 54, 2210, 32, False, "Rohan", "Shivam")     # tuple having multiple elements
# print(type(e))      # checking the data type of e
# e[0] = 45     # throws error as tuple is immutable, a new tuple can be made but it cannot be changed
# print(e)

# Tuple methods
# e = (1, 54, 2210, 32, False, "Rohan", 2210, "Shivam")
# print(e)

# no = e.count(2210)      # calculates the number of times an element is present inside the tuple
# print(no)   # prints the number of times the element is present

# i = e.index(2210)       # will return the index of the first occurrence of the element in the tuple
# print(i)        # prints the index number

# print(len(e))   # prints length of the tuple
