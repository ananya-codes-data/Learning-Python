# Conditional Expression

# Conditionals

a = int(input("Enter your age:"))

# if else statement

if(a >= 18):
    print("You are above the age of consent")

else:
    print("You are below the age of consent")

print("End of program")


a = int(input("Enter your age:"))

# if elif else ladder

if(a >= 18):
    print("You are above the age of consent")

elif(a < 0):
    print("You are entering an invalid negative age")

elif(a == 0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age of consent")

print("End of program")


age = int(input("Enter your age:"))

if(age >= 18):
    print("Yes")

else:
    print("No")


# multiple if statements

a = int(input("Enter your age:"))

# if statement 1
if(a%2 == 0):
    print("a is even")

# End of if statement 1

# if statement 2
if(a >= 18):
    print("You are above the age of consent")

elif(a < 0):
    print("You are entering an invalid negative age")

else:
    print("You are below the age of consent")

# End of if statement 2

print("End of program")

# IMPORTANT NOTES:
# 1. There can be any number of elif statements.
# 2. Last else is executed only if all the conditions inside elifs fail.


# Practice Set

# 1. program to find the greatest of four numbers

# take input from user and convert it to integer
# input() returns string, so conversion is required
a1 = int(input("Enter number 1:"))
a2 = int(input("Enter number 2:"))
a3 = int(input("Enter number 3:"))
a4 = int(input("Enter number 4:"))

if(a1 > a2 and a1 > a3 and a1 > a4):
    print("Greatest number is a1:", a1)

elif(a2 > a1 and a2 > a3 and a2 > a4):
    print("Greatest number is a2:", a2)

elif(a3 > a1 and a3 > a2 and a3 > a4):
    print("Greatest number is a3:", a3)

elif(a4 > a1 and a4 > a2 and a4 > a3):
    print("Greatest number is a4:", a4)

# 2. program to find out whether a student has passed or failed

marks1 = int(input("Enter marks 1:"))
marks2 = int(input("Enter marks 2:"))
marks3 = int(input("Enter marks 3:"))

# # Check for total percentage
total_percentage = (100 * (marks1 + marks2 + marks3))/300

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You have passed:", total_percentage,"%")

else:
    print(f"You failed with {total_percentage}%")

# 3. spam filter for detecting spam

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")

# 4.  find whether a given username contains less than 10 characters or not

username = input("Enter username:")

if(len(username) < 10):
    print("Your username contains less than 10 characters")

else:
    print("Your username contains more than or equal to 10 characters")

# 5. finds out whether a given name is present in a list or not

l = ["Ananya", "Rohan", "Anshul", "Rohit", "Anshika"]

name = input("Enter your name to check in list:")

if(name in l):
    print("Your name is in the list")

else:
    print("Your name is not in the list")

# 6. calculate the grade of a student from his marks

marks = int(input("Enter your marks:"))

if (marks <= 100 and marks >= 90):
    grade = "Ex"

elif(marks < 90 and marks >= 80):
    grade = "A"
elif(marks < 80 and marks >= 70):
    grade = "B"
elif(marks < 70 and marks >= 60):
    grade = "C"
elif(marks < 60 and marks >= 50):
    grade = "D"
elif(marks < 50):
    grade = "F"

print("Your grade is:", grade)

# 7. find out whether a given post is talking about “Harry” or not

post = input("Enter the post:")

if("harry" in post.lower()):
    print("This post is talking about harry")

else:
    print("This post is not talking about harry")
