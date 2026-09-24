total = 100 + 200 + \
300 + 400
print(total)

print("Hello", end=" ")
print("World")

print("Hello", end="\n") # by default
print("World")

name = "Ananya"
print(id(name))

age = 24
print(id(age))

num = 54321
total = 0
for digit in str(num):
    total += int(digit)
    print(total)
print(total)


# celsius to far
celsius = 60
fahrenheit = celsius / 5 * 9 + 32
print(f"when celcius = {celsius}, then fahrenheit = {fahrenheit}")

# far to cel
fahrenheit = 45
celcius = (fahrenheit - 32) / 9 * 5
print(f"when fahrenheit = {fahrenheit}, then celcius = {round(celcius)}")

citizenship_check = input("are you a citizen (yes/no):")

if citizenship_check.lower() == "yes":
    age_check = int(input("whats your age:"))

    if age_check >= 18:
        print("You can vote")
    else:
        print(f"You cannot vote right now, but you can after {18 - age_check} years")
else:
    print("You cannot vote because you are not a citizen")

#  Print numbers 1 to 20. For multiples of 3 print "Fizz", multiples of 5 print "Buzz", multiples of both print "FizzBuzz

for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Find all numbers between 1500 and 2700 that are divisible by both 7 and 5

count = 0

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num, end= ", ")
        count += 1
print(f"total numbers are: {count} ")

# Given number = 987654 , find: (a) how many digits it has, (b) which digits are even, (c) the largest digit

number = 987654

digit_count = len(str(number))
print(digit_count)

print("Even digits:", end=" ")
for digit in str(number):
    if int(digit) % 2 == 0:
        print(digit, end=" ")

largest = 0
for digit in str(number):
    if int(digit) > largest: # convert to int for comparison
        largest = int(digit)
print(f"Largest digit: {largest}")

# Write a program to check if a number is positive, negative, or zero

number = int(input("put the number: "))

if number < 0:
    print("negative")
elif number == 0:
    print("zero")
else:
    print("positive")


# Write a number classification program (even/odd, prime, perfect square)

# num = int(input("let's check your number: "))

# if num ** 0.5:
#     pass

# print a table

number = int(input("Enter the number: "))

i = 1

while i < 11:
    print(number * i)
    i += 1


# guessing game

#  generate a random integer between 1 to 100

import random

jackpot = random.randint(1, 100)

guess = int(input("guess the number: "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("guess higher!!")
    else:
        print("guess lower!!")
    guess = int(input("guess the number: "))
    counter += 1
else:
    print("correct guess")
    print("attempts:", counter)


for i in range(10, 0, -1):
    print(i)


# the current population of a town is 10000. the population of the town is increasing at the rate of 10% per year
# write a program to find out the population at the end of the last 10 years

current_population = 10000

for i in range (10, 0, -1):
    print(i, "year =", current_population)
    current_population = round(current_population/ 1.1, 2)


# sequence sum till nth term
# 1/1! + 2/2! + 3/3! +.....

n = int(input("enter the number n: "))

result = 0
fact = 1

for i in range(1, n+1):
    fact *= i
    result += i/ fact

print(result)


for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            print(i,j, k)


rows = int(input('enter number of rows: '))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('*', end= '')
    print()


num = int(input('enter number of rows: '))

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end= '')
    for k in range(i - 1, 0, -1):
        print(k, end= '')
    print()


# user will give a range, we have to find out all the prime numbers between the range

lower = int(input('enter lower range: '))
upper = int(input('enter upper range: '))

for i in range(lower, upper + 1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print(i)


# Find the length of a given string without using the len() function

s = input('enter the string: ')

counter = 0

for i in s:
    counter += 1
print(counter)


# Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com 
# then the username should be nitish24singh

email_id = input('enter your email: ')

# method 1
for i in email_id:
    if i == '@':
        break
    print(i, end= '')

# method 2
pos = email_id.index('@')
print(email_id[0:pos])

# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.

test = input('enter the string: ')

test_case = input('enter the character for which you want the frequency: ')

counter = 0

for i in test:
    if i == test_case:
        counter += 1
print(counter)


# Write a program which can remove a particular character from a string.

t = input('enter the string: ')

term = input('what would you like to remove: ')

# method 1
for i in t:
    if i == term:
        continue
    print(i, end= '')

# method 2
result = ''

for i in t:
    if i != term:
        result += i
print(result)


# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

p = input('enter the word: ')

flag = True

for i in range(0, len(p)// 2):
    if p[i] != p[len(p) - i - 1]:
        flag = False
        print('Not a palindrome')
        break
if flag:
    print('Palindrome')


# Write a program to count the number of words in a string without split()

word_check = input("enter your string: ")

l = []

temp = ''

for i in word_check:
    if i != ' ':
        temp += i
    else:
        l.append(temp)
        temp = ''
l.append(temp)
print(l)


# Write a python program to convert a string to title case without using the title()

s = input('enter the string: ')

l = []

for i in s.split():
    l.append(i[0].upper() + i[1:].lower())

print(" ".join(l))


# Write a program that can convert an integer to string.

number = int(input('enter the number: '))

digits = '0123456789'

result = ''

while number != 0:
    result = digits[number % 10] + result
    number = number// 10
print(result)
print(type(result))

