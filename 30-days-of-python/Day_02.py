# Built in functions in Python

# A
# abs()
# aiter()
# all()
# anext()
# any()
# ascii()

# B
# bin()
# bool()
# breakpoint()
# bytearray()
# bytes()

# C
# callable()
# chr()
# classmethod()
# compile()
# complex()

# D
# delattr()
# dict()
# dir()
# divmod()

# E
# enumerate()
# eval()
# exec()

# F
# filter()
# float()
# format()
# frozenset()

# G
# getattr()
# globals()

# H
# hasattr()
# hash()
# help()
# hex()

# I
# id()
# input()
# int()
# isinstance()
# issubclass()
# iter()

# L
# len()
# list()
# locals()

# M
# map()
# max()
# memoryview()
# min()

# N
# next()

# O
# object()
# oct()
# open()
# ord()

# P
# pow()
# print()
# property()

# R
# range()
# repr()
# reversed()
# round()

# S
# set()
# setattr()
# slice()
# sorted()
# staticmethod()
# str()
# sum()
# super()

# T
# tuple()
# type()

# V
# vars()

# Z
# zip()

# _
# __import__()

# Note: Some built-in functions may not be listed here.

print(len("Ananya Pradhan"))

# print() - prints the value
# len() - counts the number of characters including space

print(type(3.14))

# type() checks the data type

print(str(22.10))
print(type(str(22.10))) # to check the data type

# str() - converts decimal to string

print(int(22.10))
print(type(int(22.10))) # to check the data type

# int() converts float to integer

print(float(22))
print(type(float(22))) # to check the data type

# float() converts integer to decimal

print(input("Enter your name:"))

# input() takes user input

print(help("keywords"))

# prints all python reserved words

print(help("class"))
print(help("str"))
print(dir("str"))

print(min(20, 30, 40, 50)) # gives the minimum value
print(min([20, 30, 40, 50])) # takes list as an argument and returns min
print(max([20, 30, 40, 50])) # takes list as an argument and returns max
print(max(20, 30, 40, 50)) # gives the maximum value
print(sum([20, 30, 40, 50])) # takes list as an argument and returns sum


# Variables

# Python Variable Name Rules

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

# When we assign a certain data type to a variable, it is called variable declaration

# Assigning means storing data in the variable

print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument

# Multiple variables can also be declared in one line

first_name, last_name, country, age, is_married = "Ananya", "Pradhan", "India", 22, False

print(first_name, last_name, country, age, is_married)
print("First name:", first_name)
print("Last name:", last_name)
print("Country:", country)
print("Age:", age)
print("Married:", is_married)

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)


# Data types

# checking data types

# Casting: Converting one data type to another data type


# Exercises - Day 2

# Exercises: Level 1

# 1. Done
# 2. Done

# 3.
first_name = "Ananya"

# 4.
last_name = "Pradhan"

# 5.
full_name = "Ananya Pradhan"

# 6.
country = "India"

# 7.
city = "Mumbai"

# 8.
age = 22

# 9.
year = 2025

# 10.
is_married = False

# 11.
is_true = True

# 12.
is_light_on = False

# 13.
first_name, last_name, full_name, country, city = "Ananya", "Pradhan", "Ananya Pradhan", "India", "Mumbai"


# Exercises: Level 2

# 1.
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# 2.
print(len(first_name))

# 3.
print(len(first_name))
print(len(last_name))

# 4.
num_one = 5
num_two = 4

# 5.
total = num_one + num_two

print(total)

# 6.
diff = num_two - num_one

print(diff)

# 7.
product = num_one * num_two

print(product)

# 8.
division = num_one / num_two

print(division)

# 9.
remainder = num_two % num_one

print(remainder)

# 10.
exp = num_one ** num_two

print(exp)

# 11.
floor_division = num_one // num_two

print(floor_division)

# 12. i.
radius = 30
pi = 3.14
area_of_circle = pi * radius * radius

print(area_of_circle)

# 12. ii.
radius = 30
pi = 3.14
circum_of_circle = 2 * pi * radius

print(circum_of_circle)

# 12. iii.
pi = 3.14

radius = float(input("Enter the radius:"))
area_of_circle = pi * radius * radius

print("The area of the circle is:", area_of_circle)

# 13.
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
country = input("Entry your country name:")
age = input("Enter your age:")

print("My first name is", first_name)
print("My last name is", last_name)
print("I am from", country)
print("I am", age, "years old")

# 14.
print(help("keywords"))