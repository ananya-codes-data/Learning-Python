# Dictionary and Sets

# Dictionary is a collection of keys-value pairs

d = {}      # empty dictionary

marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}
print(marks, type(marks))
print(marks["Harry"])   # 100

# properties of python dictionaries
# 1. It is unordered
# 2. It is mutable
# 3. It is indexed
# 4. Cannot contain duplicate keys

# Dictionary methods
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

print(len(marks))       # 4
print(marks.items())    # Returns a list of (key,value) in form of tuples
print(marks.keys())     # Returns a list containing dictionary's keys
print(marks.values())       # Returns a list containing dictionary's vales
marks.update({"Harry": 99, "Renuka": 100})
# a new dict is passed,
# the values that are present beforehand are updated
# and new key-value pairs are added
print(marks)

print(marks.get("Shivika"))     # None
print(marks.get("Harry"))       # 100

# Interview question
# diff between
print(marks["Harry"])
# vs
print(marks.get("Harry"))
# in both of the above cases the output will be same
# but if there is a key which does not exist
print(marks["Harry2"])      # will give an error
# while
print(marks.get("Harry"))     # will print None as the output

# TODO: SEARCH FOR MORE PYTHON DICTIONARY METHODS
# pop, popitem

# Sets
# Set is a collection of non-repetitive elements
# when there is a use case where elements cannot be repeated we use sets

e = set()       # empty set
s = {}    # will create an empty dictionary and not an empty set

s = {1, 5, 32, 54}
print(s)    # {32, 1, 5, 54}
f = {1, 2, 3, 5, 4, 5, 5}
print(f)        # {1, 2, 3, 4, 5}

# PROPERTIES OF SETS
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.


# Set methods
a = {1, 2, 5, 32, 45, 45, 5, 5, 5, 5, "Ananya"}
print(a, type(a))           # {32, 1, 2, 5, 45, 'Ananya'} <class 'set'>

a.add(22)       # adds a new element to the set
print(a, type(a))       # {32, 1, 2, 'Ananya', 5, 22, 45} <class 'set'>

print(len(a))       # 7       # prints the length of the set

a.remove(2)         # removes the specific element from the set
print(a, type(a))       # {32, 1, 5, 'Ananya', 22, 45} <class 'set'>


# Set union and intersection
s1 = {1, 45, 76}
s2 = {7, 8, 1, 54}
print(s1.union(s2))         # {1, 54, 7, 8, 76, 45}
print(s1.intersection(s2))      # {1}

# TODO: SEARCH FOR MORE PYTHON SET METHODS


# Practice Set

# 1.
# creating a dict
words = {
      "madad": "Help",
      "phool": "Flower",
      "titli": "Butterfly",
      "manjil": "Destination",
      "safar": "Journey"
}

# creating a variable using input function
word = input("Enter the word you want meaning of:")

# prints the english meaning of the hindi word the user inputs
print(words[word])

# 2.
numbers = set()

number_1 = int(input("Enter 1st number:"))
numbers.add(number_1)
number_2 = int(input("Enter 2nd number:"))
numbers.add(number_2)
number_3 = int(input("Enter 3rd number:"))
numbers.add(number_3)
number_4 = int(input("Enter 4th number:"))
numbers.add(number_4)
number_5 = int(input("Enter 5th number:"))
numbers.add(number_5)
number_6 = int(input("Enter 6th number:"))
numbers.add(number_6)
number_7 = int(input("Enter 7th number:"))
numbers.add(number_7)
number_8 = int(input("Enter 8th number:"))
numbers.add(number_8)

print(numbers)

# 3. yes we can have it
b = set()
b.add(18)
b.add("18")
print(b)

# 4.
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)        # {20, '20'}
print(len(s))       # 2

# python compares their value,
# if the values are same, python accepts it,
# python focuses on the numerical value and not on the data type

# 5.
s = {}
print(type(s))      # <class 'dict'>

# 6.
d = {}

name = input("Enter friends name:")
lang = input("Enter Language name:")
d.update({name: lang})

name = input("Enter friends name:")
lang = input("Enter Language name:")
d.update({name: lang})

name = input("Enter friends name:")
lang = input("Enter Language name:")
d.update({name: lang})

name = input("Enter friends name:")
lang = input("Enter Language name:")
d.update({name: lang})

print(d)

# 7.
# If the names of 2 friends are same, the values entered late will be updated for the key

# 8.
# If languages of two friends are same, it will remain as it is, as the value can be duplicate but not the keys
# and the key is the identifier

# 9.
s = {8, 7, 12, "Harry", [1,2]}
# no it cannot happen
# i. list cannot be included inside a set
# ii. we cannot change the value by indexing because set is unindexed
