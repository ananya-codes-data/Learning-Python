# Strings - data type in python, sequence of characters enclosed in quotes

# name1 = 'Ananya' # single qoted string

name = "Ananya" # double quoted string

# name2 = '''Ananya
# Pradhan''' # triple quoted string for multi line strings

# string slicing - string in python can be sliced for getting a part of the strings
# indexing - if going from left to right it starts with 0 and if from right to left it starts with -1
# string is immutable - we cannot change an existing string

# nameshort = name[0:3]   # start from index 0 all the way till 3 (excluding 3)
# print(nameshort)

# character1 = name[4]    # exact character of the string
# print(character1)

print(name[0:3])

print(name[-4: -1])
# converting negative indices to positive
print(name[2:5])

print(name[:3])     # if the starting index is blank it is considered 0
print(name[0:])     # if the ending index is blank it is considered the complete length
print(name[:])      # if both the starting and ending index is blank the complete string would be printed
