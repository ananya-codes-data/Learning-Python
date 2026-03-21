# Dictionary and Sets

# Dictionary is a collection of keys-value pairs

# d = {}      # empty dictionary

# marks = {
#     "Harry": 100,
#     "Shubham": 56,
#     "Rohan": 23
# }
# print(marks, type(marks))
# print(marks["Harry"])   # 100

# properties of python dictionaries
# 1. It is unordered
# 2. It is mutable
# 3. It is indexed
# 4. Cannot contain duplicate keys

# Dictionary methods
# marks = {
#     "Harry": 100,
#     "Shubham": 56,
#     "Rohan": 23,
#     0: "Harry"
# }

# print(marks.items())    # Returns a list of (key,value) in form of tuples
# print(marks.keys())     # Returns a list containing dictionary's keys
# print(marks.values())       # Returns a list containing dictionary's vales
# marks.update({"Harry": 99, "Renuka": 100})
# a new dict is passed,
# the values that are present beforehand are updated
# and new key-value pairs are added
# print(marks)

# print(marks.get("Shivika"))     # None
# print(marks.get("Harry"))       # 100

# Interview question
# diff between
# print(marks["Harry"])
# vs
# print(marks.get("Harry"))
# in both of the above cases the output will be same
# but if there is a key which does not exist
# print(marks["Harry2"]) -- will give an error
# while
# print(marks.get("Harry")) -- will print None as the output
# TODO: SEARCH FOR MORE PYTHON DICTIONARY METHODS
# pop, popitem

# Sets
# Set is a collection of non-repetitive elements

