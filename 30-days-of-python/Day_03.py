# Operators

# Note
# 1. Declaring the variable at the top first
# 2. then can go for applying functions to the assigned variable

# example
# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3') # Adding unit to the density


# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x not in y)


# Exercises - Day 3

# 1.
age = 22

# 2.
h = 5.8

# 3.
c = 22 + 1j

# 4.
base = float(input("Enter base:"))
height = float(input("Enter height:"))
area_of_traingle = 0.5 * base * height
print("The area of the triangle is", area_of_traingle)

# 5.
side_a = float(input("Enter side a:"))
side_b = float(input("Enter side b:"))
side_c = float(input("Enter side c:"))
perimeter_of_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter_of_triangle)

# 6.
length = float(input("Enter length:"))
width = float(input("Enter width:"))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print("The area of the rectangle is", area_of_rectangle, "and", "The perimeter of the rectangle is", perimeter_of_rectangle)

# 7.
radius = float(input("Enter radius:"))
pi = 3.14
area_of_circle = pi * radius * radius
circumference_of_circle = 2 * pi * radius
print("The area of the circle is", area_of_circle)
print("The circumference of the circle is", circumference_of_circle)

# 8. slope, x-intercept, y-intercept
# y = mx + c
# equation: y = 2x -2
m = 2       # slope
c = -2      # y-intercept value
print("Slope:", m)
print("Y-intercept: (0 ,", c,")")

# to find x-intercept, set y = 0
# 0 = 2x -2
# 2x = 2
# x = 1

x_intercept = 1
print("X-intercept: (", x_intercept, ", 0)")

# 9. slope, euclidean distance
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
print("Slope between points:", slope)

distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Euclidean Distance:", distance)

# 10.
# equation = y = 2x - 2

# check point (2,2)
print(2 == 2*2 - 2)

# check point (6,10)
print(10 == 2*6 - 2)

# TODO: checking using if-else

# 11.
x = float(input("Enter the value of x:"))
y = x**2 + 6*x + 9
print("The value of y is", y)
print("x=", x, "y=", y)
print("(", x, ",", y, ")")

# by factorization we get the value of x to be -3
# so for x = -3, y = 0

# 12.
# strings
word_1 = "python"
word_2 = "dragon"
# find and print lengths
print(len(word_1))
print(len(word_2))
# falsy comparison statement
comparison = len(word_1) > len(word_2)
print("Is length of python greater than dragon?", comparison)

# 13.
# Check if 'on' is present in both using AND operator
result_1 = ("on" in word_1) and ("on" in word_2)
print(result_1)

# 14.
sentence = "I hope this course is not full of jargon"
result_2 = "jargon" in sentence
print(result_2)

# 15.
print(not(result_1))

# 16.
# finding length of word - python
# converting it to float & then to string
# finally checking the if the length is string or not
print(type(str(float(len(word_1)))))

# 17. checking if a number is even or not
number = float(input("Enter a number:"))    # user input
even_number = number % 2    # using modulus operator for finding remainder
print(even_number == 0)     # if the remainder is 0 then that becomes an even number

# 18. checking if the result of both num would be equal
num_1 = 7 // 3
num_2 = 2.7

print(num_1 == int(num_2))      # converting num_2 to integer

# 19. Check if type of '10' is equal to type of 10
num_3 = "10"
num_4 = 10
print(type(num_3) == type(num_4))

# 20. Check if int('9.8') is equal to 10
num_5 = int(float("9.8"))
num_6 = 10
print(type(num_5) == num_6)

# 21.
# prompt user to enter the number of hours
hours = float(input("Enter hours:"))
# prompt user to enter the rate per hour
rate_per_hour = float(input("Enter rate per hour:"))
# calculation of weekly earning
pay_of_the_person = hours * rate_per_hour
print("Your weekly earning is", pay_of_the_person)

# 22.
# prompt user to enter number of years
years = float(input("Enter the number of years you have lived:"))
# constants
seconds_in_one_year = 365 * 24 * 60 * 60
# calculate seconds lived
seconds_lived = years * seconds_in_one_year
print("You have lived for", seconds_lived, "seconds")

# 23.
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

# TODO: rewrite it using loop