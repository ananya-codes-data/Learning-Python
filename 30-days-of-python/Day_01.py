# The process of identifying and removing errors from a program is called debugging

# Some of the Python errors types we may encounter are:
# SyntaxError
# IndexError
# NameError
# ModuleNotFoundError
# KeyError
# ImportError
# AttributeError
# TypeError
# ValueError
# ZeroDivisionError etc

a = 45
b = 6

print(a / b) # division (returns a float)
print(a // b) # floor division (returns quotient as int)
print(a % b) # modulus (returns the remainder as int)

# Data types

# string - characters within quotes
a = "Ananya"


# Booleans - either the value is True or False
a = 4 > 5
print(a)


# List - ordered collection which allows to store different data type items
# mutable and allows duplicates

a = [0, 1, 2, 3, 4]
a = [True, 1.25, 2, "Ananya", 4]

print(a)

nums = [1, 2, 3, 3]

print(nums)


# Dictionary - dictionary object is an unordered collection of data in a key value pair format
# mutable

a = {
"role":"data scientist",
"skills":["Python", "SQL", "ML", "AI"]
}

print(a)

student = {
    "name": "Ananya",
    "age": 22,
    "course": "Data Science"
}

print(student)

print(student["course"])


# Tuple - ordered collection of different data types like list but tuples can not be modified once they are created
# They are immutable but allows duplicates

planets = ("Earth", "Jupiter", "Neptune", "Mars", "Venus", "Saturn", "Uranus", "Mercury")

print(planets)

a = (1, 2, 4, 4)

print(a)


# set - unordered, mutable collection of unique values

a = {1, 2, 3, 3}
b = {"Ananya", 21.22, 10, True, 10, 30.0, 18, 20, 19, 18}

print(b)



# Exercises - Day 1

# Exercise: Level 1

# 1. checked in the terminal - Python 3.12.10

# 2. done in terminal

# 3. done in terminal

# 4.

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Ananya"))
print(type("Pradhan"))
print(type("India"))


# Exercise: Level 2
# Completed


# Exercise: Level 3

# 1.
i = 22

print(a)
print(type(a))

f = 22.10

print(b)
print(type(b))

c = (21 + 2j)

print(c)
print(type(c))

s = "Ananya"

print(s)
print(type(s))

b = 22 > 21

print(b)
print(type(b))

l = [1, 2, 3, 3]

print(l)
print(type(l))

t = (1, 2, 3, 4, 4)

print(t)
print(type(t))

s = {1, 2, 3, 4, 4, 14, 18, 87, 43, 14}

print(s)
print(type(s))

d = {
    "role":"data scientist",
    "programming languages":["Python, SQL"]
}

print(d)
print(type(d))

# 2.
x1, y1 = 2, 3
x2, y2 = 10, 8

dx = x2 - x1
dy = y2 - y1

distance = (dx*dx + dy*dy) ** 0.5

print(distance)
