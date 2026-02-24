# Strings - data type in python, sequence of characters enclosed in quotes

# strings are immutable and that's the reason they are case sensitive


# name1 = 'Ananya' # single qoted string

# name = "Ananya" # double quoted string

# name2 = '''Ananya
# Pradhan''' # triple quoted string for multi line strings

# string slicing - string in python can be sliced for getting a part of the strings
# indexing - if going from left to right it starts with 0 and if from right to left it starts with -1
# string is immutable - we cannot change an existing string

# nameshort = name[0:3]   # start from index 0 all the way till 3 (excluding 3)
# print(nameshort)

# character1 = name[4]    # exact character of the string
# print(character1)

# print(name[0:3])

# print(name[-4: -1])
# converting negative indices to positive
# print(name[2:5])

# if the starting index is blank it is considered 0
# print(name[:3])     # is same as print(name[0:3])
# if the ending index is blank it is considered length - 1 because the length is 6 in this case
# if the ending index is empty just put the length of the string
# print(name[0:])     # is same as print(name[0:5])
# if both the starting and ending index is blank the complete string would be printed
# print(name[:])      # is same as print(name[0:6])

# slicing with skip value
# a = "0123456789"
# print(a[1:7:3])
# print(a[1:7]) # at first this part would run to give 123456

# b = "abcdefghijklmnopqrstuvwxyz"
# print(b[1:9]) # resolve this first
# print(b[1:9:4])


# string functions

# print(len(name))    # prints length of the string

# print(name.endswith("nya"))     # prints True/False if/if not the string ends with certain characters

# print(name.startswith("Ana"))   # prints True/False if/if not the string starts with certain characters

# print(name.capitalize())    # capitalizes only the first character of a string


# escape sequence characters

# a = "Hello\nI'm Ananya"     # \n represents new line
# print(a)

# b = "Hi\tI'm learning python"       # \t represents tab space
# print(b)

# c = "Hello \"World\""       # \" considers it as a double quote inside the string
# print(c)


# Practice set

# 1.
# name_1 = input("Enter your name:")
# print("Good Afternoon", name_1)
# alternative
# print(f"Good Afternoon {name_1}")   # f-string can be used to insert a variable inside a string

# 2.
letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "Ananya").replace("<|Date|>", "22 October 2026"))