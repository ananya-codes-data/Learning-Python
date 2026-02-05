print("Hello World")
# print is a function

# pip install flask - installs flask module

# ctrl + / - for single line comment - #

"""
 so thanks
that was my program
"""

# Practice set

# 1

print(""" Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.""")

# 2

# done using REPL in terminal

# 3

import pyttsx3
engine = pyttsx3.init()
engine.say("Hey I'm good.")
engine.runAndWait()

# 4

import os

# Select the directory whose content you want to list
directory_path = "C:/"

# use the os module to list the directory content
contents = os.listdir(directory_path)

# Print the contents of the directory
print(contents)
