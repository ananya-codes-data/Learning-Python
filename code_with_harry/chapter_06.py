# Conditional Expression

# Conditionals

# a = int(input("Enter your age:"))

# if else statement

# if(a >= 18):
#     print("You are above the age of consent")

# else:
#     print("You are below the age of consent")

# print("End of program")


# a = int(input("Enter your age:"))

# if elif else ladder

# if(a >= 18):
#     print("You are above the age of consent")

# elif(a < 0):
#     print("You are entering an invalid negative age")

# elif(a == 0):
#     print("You are entering 0 which is not a valid age")

# else:
#     print("You are below the age of consent")

# print("End of program")


# age = int(input("Enter your age:"))

# if(age >= 18):
#     print("Yes")

# else:
#     print("No")


# multiple if statements

# a = int(input("Enter your age:"))

# if statement 1
# if(a%2 == 0):
#     print("a is even")

# End of if statement 1

# if statement 2
# if(a >= 18):
#     print("You are above the age of consent")

# elif(a < 0):
#     print("You are entering an invalid negative age")

# else:
#     print("You are below the age of consent")

# End of if statement 2

# print("End of program")

# IMPORTANT NOTES:
# 1. There can be any number of elif statements.
# 2. Last else is executed only if all the conditions inside elifs fail.


# Practice Set

# 1.

# a1 = int(input("Enter number 1:"))
# a2 = int(input("Enter number 2:"))
# a3 = int(input("Enter number 3:"))
# a4 = int(input("Enter number 4:"))

# if(a1 > a2 and a1 > a3 and a1 > a4):
#     print("Greatest number is a1:", a1)

# elif(a2 > a1 and a2 > a3 and a2 > a4):
#     print("Greatest number is a2:", a2)

# elif(a3 > a1 and a3 > a2 and a3 > a4):
#     print("Greatest number is a3:", a3)

# elif(a4 > a1 and a4 > a2 and a4 > a3):
#     print("Greatest number is a4:", a4)

# 2.

marks1 = int(input("Enter marks 1:"))
marks2 = int(input("Enter marks 2:"))
marks3 = int(input("Enter marks 3:"))

# Check for total percentage
total_percentage = (marks1 + marks2 + marks3)/300
