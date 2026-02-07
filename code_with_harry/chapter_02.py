# variables

a = 1
b = 2
c = 7
name = "Ananya"

print(name)

# variables = container to store a value.
# keywords = reserved words in python 
# identifiers = class/function/variable name


# data types

a = 22 # a is an integer
b = 21.22 # b is a floating point number
c = "ananya" # c is a string
d = False # d is a boolean variable
e = None # e is a none type variable


# rules of choosing variables

a = 22
aaa = 1234
ananya = 2134
shan = 2608
_shan = 2010
ananya_2112 = ananya

# @sameer = 56 # Invalid due to @ symbol
# s@meer # Invalid due to @ symbol


# operators in python

# 1. Arithmetic operators: +, -, *, /, //, %, **
# 2. Assignment operators: =, +=, -=, *=, /=
# 3. Comparison operators: ==, >, >=, <, <=, !=
# 4. Logical operators: and, or, not.

# Arithmetic Operators

# 7 + 4 = 11
# 7 & 4 are operands
# + is the operator
# 11 is the result

a = 21
b = 22
c = a + b

print(c)

# Assignment operators

a = 4 - 2 # Assign 4 - 2 in a

print(a)

b = 6

b += 3 # Increment the value of b by 3 and then assign it to b
b -= 3 # Decrement the value of b by 3 and then assign it to b
b *= 3 # Multiply the value of b with 3 and then assign it to b
b /= 3 # Divide the value of b by 3 and then assign it to b

print(b)

# Comparison operators

d = 5 < 4 # Is 5 less than 4
d = 5 > 4 # Is 5 more than 4
d = 5 >= 5 # Is 5 more than equal to 5
d = 5 <= 5 # Is 5 less than equal to 5
d = 5 != 7 # Is 5 not equal to 7
d = 5 == 5 # Is 5 equal to 5

print(d)


# Logical operators

e = True or False

# Truth table of 'or'
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and'
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

# multi cursor functionality
# press alt and where ever you click cursor will apply and we can do that multiple times


print(not(False))

print(not(True))


# type function - function to find data type of any variable

a = 31
t = type(a) # class <int>

a = 31.2
t = type(a) # class <float>

a = "ananya"
t = type(a) # class <str>

a = "22.10"
t = type(a) # class <str>

a = "22.10"
b = float(a) # a but the type should be float
t = type(b) # class <float>

print(t)

# str(31) =>"31" # integer to string conversion
# int("32") => 32 # string to integer conversion
# float(32) => 32.0 # integer to float conversion


# input function - funtion that prompts user to enter data

# data type of input function is always str

a = int(input("Enter number 1: ")) # this will be shown in the terminal to enter data
b = int(input("Enter number 2: ")) # this will be shown in the terminal to enter data

print("Number a is:", a) # aftering entering data this will shown as the result along with the data
print("Number b is:", b) # aftering entering data this will shown as the result along with the data
print("Sum is:", a + b) # adding a with b

# alt + shift + down arrow key - to replicate a line


# Practice set

# 1 program to add two numbers

a = 1
b = 5

print(a + b)


# 2 program to find remainder

a = 37
b = 5

print("Remainder when a is divided by b is", a % b)


# 3 Check the type of variable assigned using input () function

a = input("Enter the value of a: ")
print(type(a))


# 4 check whether given variable a is greater than b or not

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("a is greater than b is", a > b)


# 5 program to find average of 2 numbers entered by user

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("The average of these two number is", (a + b) / 2 )


# 6 program to find power of a number entered by user

a = int(input("Enter the number: "))

print("The square of the number is", a * a)

# a ** 2 - can be used to find the power of 2
# like a ** 3 - can be used to find cube of a number