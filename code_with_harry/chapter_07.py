# Loops in Python

# for i in range(1, 6):
#     print(i)

# types of loops in python
# while loops
# for loops

# while loop

# i = 1

# while(i < 6):
#     print(i)
#     i += 1

# i = 1

# while(i < 51):
#     print(i)
#     i += 1

# i = 0

# while(i < 5):
#     print("Harry")
#     i += 1

# list using while loop

# l = [1, 10.22, "Harry", False, "Rohan", "This", "Shubham"]

# i = 0

# while(i < len(l)):
#     print(l[i])
#     i += 1

# for loops

# for loop is used to iterate through a sequence like list, tuple, or string [iterables]

# for i in range(0, 4):
#     print(i)

# range(start, stop, step_size)

# for i in range(20,42):
#     print(i)        # from 20 to 41 and excluding 42

# for i in range(20, 62, 4):
#     print(i)        # 20, 24, 28, 32,...,56, 60

# for loop iterate

# for loop with lists

# l = [1, 4, 6, 224, 21, 6, 764]

# for i in l:
#     print(i)

# for loop with tuples

# t = (6, 231, 75, 122)

# for i in t:
#     print(i)

# for loop with string

# s = "Ananya"

# for i in s:
#     print(i)

# for loop with else

# l = [1, 7, 8]

# for item in l:
#     print(item)

# else:
#     print("done")  # this is printed when the loop exhausts!


# break statement

# for i in range(0, 100):
#     if(i == 34):
#         break   # exit the loop right now
#     print(i)

# continue statement

# for i in range(0, 100):
#     if(i == 34):
#         continue   # skip this iteration
#     print(i)

# pass statement - null statement in python

# for i in range(0, 645):
#     pass

# i = 0

# while(i < 45):
#     print(i)
#     i += 1


# Practice Set

# 1.

# n = int(input("Enter a number:"))

# for i in range(1, 11):
#     print(f"{n} X {i} = {n * i}")

# 2.

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# 3.

# n = int(input("Enter a number:"))

# i = 1

# while(i < 11):
#     print(f"{n} X {i} = {n * i}")
#     i += 1

# 4.

n = int(input("Enter a number:"))