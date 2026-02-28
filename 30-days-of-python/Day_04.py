# Strings

# string creation
# Any data type written as text is a string. 
# Any data under single, double or triple quote are strings
# String could be made using a single or double quote
# Multiline string is created by using triple single (''') or triple double quotes (""")

# String Concatenation - merging or connecting strings

# first_name = "Ananya"
# last_name = "Pradhan"
# space = " "
# full_name = first_name + space + last_name
# print(full_name)

# Escape sequences in strings
# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")

# print("I think I can finish the \"Python challenge\".\n\tWhat do you think?")

# String formatting

# In old style string formatting % operator was used.
# New style string formatting (str.format) was introduced in Python version 3

# string interpolation / f-strings (3.6+)
# in string interpolation the only rule is to start the string with a f while using print function

# name = input("Enter your name:")
# print(f"Good Morning, {name}")

# python strings as sequences of characters

# simplest way of extracting single characters from strings is to unpack them into corresponding variables.
# unpacking characters
# name_1 = "Ananya"
# a,b,c,d,e,f = name_1 # unpacking sequence characters into variables
# print(a) # A
# print(b) # n
# print(c) # a
# print(d) # n
# print(e) # y
# print(f) # a

# Accessing Characters in Strings by Index
# In programming counting starts from zero. 
# Therefore the first letter of a string is at zero index and the last letter of a string is the length of a string minus one.
# word = "String"
# first_letter = word[0]
# print(first_letter) # S
# second_letter = word[1]
# print(second_letter) # t
# last_index = len(word) - 1
# last_letter = word[last_index]
# print(last_letter) # g

# If we want to start from right end we can use negative indexing. -1 is the last index.
# language = "Python"
# last_letter = language[-1]
# print(last_letter) # n
# second_last = language[-2]
# print(second_last) # o

# slicing python strings
# language = "Python"
# first_three = language[0:3] # starts at zero index and up to 3 but 3 not included
# print(first_three) #Pyt
# last_three = language[3:6]
# print(last_three) # hon
# # Another way
# last_three = language[-3:]
# print(last_three)   # hon
# it's better to convert negative indexing into positive and then print the result
# last_three = language[3:]
# print(last_three)   # hon

# Reversing string
# greeting = "Hello, World!"
# print(greeting[::-1]) # !dlroW ,olleH

# Skipping Characters While Slicing
# language = "Python"
# skip_slice = language[1:4:3]
# print(skip_slice) # y

# String Methods

# challenge = "thirty days of python"

# capitalize()
# print(challenge.capitalize()) # converts the first character of the string to capital letter
# converts all other uppercase characters to lower case other than the first character 

# count()
# print(challenge.count("t")) # calculates number of occurences of a substring in a string
# print(challenge.count("t", 12, 21)) # 1

# endswith() -- checks if a string ends with a specified ending
# print(challenge.endswith("on"))     # True
# print(challenge.endswith("th"))     # False

# find() -- Returns the index of the first occurrence of a substring, if not found returns -1
# print(challenge.find("t"))  # 0
# print(challenge.find("th")) # 0
# print(challenge.find("z")) # -1 -- substring not found

# rfind() -- Returns the index of the last occurrence of a substring, if not found returns -1
# print(challenge.rfind("t")) # 17
# print(challenge.rfind("th")) # 17
# print(challenge.rfind("z")) # -1 -- substring not found

# index() -- similar to find(), the difference is it raises a ValueError if the substring is not found
# print(challenge.index("t")) # 0
# print(challenge.index("z")) # ValueError -- substring not found

# rindex() -- similar to rfind(), the difference is it raises a ValueError if the substring is not found
# print(challenge.rindex("t")) # 17
# print(challenge.rindex("z")) # ValueError -- substring not found

# isalnum(): Checks alphanumeric character
# challenge = 'ThirtyDaysPython'
# print(challenge.isalnum()) # True

# challenge = '30DaysPython'
# print(challenge.isalnum()) # True

# challenge = 'thirty days of python'
# print(challenge.isalnum()) # False, space is not an alphanumeric character

# challenge = 'thirty days of python 2026'
# print(challenge.isalnum()) # False

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
# challenge = 'thirty days of python'
# print(challenge.isalpha()) # False, space is once again excluded
# challenge = 'ThirtyDaysPython'
# print(challenge.isalpha()) # True
# num = '123'
# print(num.isalpha())      # False

# isdecimal(): Checks if all characters in a string are decimal (0-9)
# print(challenge.isdecimal())  # False

# challenge = '123'
# print(challenge.isdecimal())  # True

# challenge = '12 3'
# print(challenge.isdecimal())  # False, space not allowed

# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
# challenge = 'Thirty'
# print(challenge.isdigit()) # False
# challenge = '30'
# print(challenge.isdigit())   # True
# challenge = '\u00B2'
# print(challenge.isdigit())   # True
# TODO: check about unicode characters and isdigit()

# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
# num = '10'
# print(num.isnumeric()) # True
# num = '\u00BD' # ½
# print(num.isnumeric()) # True
# num = '10.5'
# print(num.isnumeric()) # False

# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
# challenge = '30DaysOfPython'
# print(challenge.isidentifier()) # False, because it starts with a number
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier()) # True

# islower(): Checks if all alphabet characters in the string are lowercase
# challenge = 'thirty days of python'
# print(challenge.islower()) # True
# challenge = 'Thirty days of python'
# print(challenge.islower()) # False

# isupper(): Checks if all alphabet characters in the string are uppercase
# challenge = 'thirty days of python'
# print(challenge.isupper()) #  False
# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper()) # True

# challenge = "thirty dAys of python"
# print(challenge.isupper()) #  False
# challenge = "THIRTY DaYS OF PYTHON"
# print(challenge.isupper()) # False

# TODO: learn about join(), strip(), split()

# replace(): Replaces substring with a given string
# challenge = "hundred days of python"
# print(challenge.replace("python", "coding")) # hundred days of coding

# title(): converts the first character of each word in string
# name = "ananya pradhan"
# print(name.title()) # Ananya Pradhan

# greeting = "it's my 22nd birthday"
# print(greeting.title()) #It'S My 22Nd Birthday

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
# challenge = 'thirty days of python'
# print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
# challenge = 'Thirty Days Of Python'
# print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String
# challenge = 'thirty days of python'
# print(challenge.startswith('thirty')) # True
# print(challenge.startswith("da")) # False


# Exercises - Day 4

# 1.
# string_1 = "Thirty"
# string_2 = " "
# string_3 = "Days"
# string_4 = "Of"
# string_5 = "Python"
# print(string_1 + string_2 + string_3 + string_2 + string_4 + string_2 + string_5)

# 2.
string_6 = "Coding"
string_7 = " "
string_8 = "For"
string_9 = "All"
# print(string_6 + string_7 + string_8 + string_7 + string_9)

# 3.
company = string_6 + string_7 + string_8 + string_7 + string_9

# 4.
# print(company)

# 5.
# print(len(company))

# 6.
# print(company.upper())

# 7.
# print(company.lower())

# 8.
# print(company.capitalize())
# print(company.title())
# print(company.swapcase())

# 9. slicing first word
# first_word = company[0:6]
# print(first_word)

# 10.
# print(company.find("Coding"))
# print(company.rfind("Coding"))
# print(company.index("Coding"))
# print(company.rindex("Coding"))

# 11.
# print(company.replace("Coding", "Python"))

# 12.
script = "Python for Everyone"
print(script.replace("Everyone", "All"))

# TODO: 13.

# TODO: 14.

# 15.