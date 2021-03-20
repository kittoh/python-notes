# DAY 2
#---------------------------------------------------------------------------#
# PARAMETERS, IMPORTING, UNPACKING, VARIABLES

# import, this adds a set of functions/methods from a module(built-in or installed) 
# that can then be used within the script

from sys import argv

# argv is assigned to 3 variables, all of them holds the power of argv
# the first item in argv is always your script itself
# you can check the online documentation for a more clarified explanation
script, first, second = argv
third = input("Third input: ")

print("The Script", script)
print("The First", first)
print("The Second", second)
print("The Third", third)

# python your_script.py First 2nd <-- run this in the terminal
# then input a third value

# PROMPTING AND PASSING
from sys import argv

# username is defined as a command line argument
# prompt is defined as a string
script, username = argv
prompt = '--> '

# python your_script.py your_name <-- run this in the terminal
print(f"Hi {username}!, I'm the {script} script guy.")
print(f"You good there {username}?")
answer_if_good = input(prompt)

print(f"Where do you want to go {username}?")
place_to_go = input(prompt)

print(f"Okay {username}, we're going to the {place_to_go}.")

#---------------------------------------------------------------------------#
# FILE HANDLING - READING FILES

from sys import argv

# defined the argument for the file name to be opened
script, filename = argv

# opens the file name, make sure it's in the same directory as the script
text = open(filename)

# read, a function that reads the content of the file
print(f"Here's the file {filename}")
print(text.read())

# same thing but with input
print("Enter file name again.")
file = input("--> ")

text_2 = open(file)

print(text_2.read())
# close, closes the opened file
text_2.close()

#---------------------------------------------------------------------------#
