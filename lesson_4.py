#---------------------------------------------------------------------------#
# DAY 4
#---------------------------------------------------------------------------#
# NAMES, VARIABLES, CODES, FUNCTIONS

# Functions, these are sets of codes that does a certain action
# sometimes it takes parameters, sometimes it don't
# def, is the keyword that defines a functions
# then followed by any name for your function you want to have
# * in *args means the function takes any number of arguments

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# 
from sys import argv

script, x, y = argv

# sets x, y as function parameters
# since these arguments are strings, it should be converted to an integer
# so that it can be used in math operations
def sum(x, y):
    return int(x) + int(y)

print(sum(x, y))

# command to run: python your_script.y {first_number} {second_number}
# the above command will print the sum of the two numbers

#---------------------------------------------------------------------------#
# FUNCTIONS AND FILES

from sys import argv

script, input_file = argv

# reads the whole file then prints it
def print_all(f):
    print(f.read())

# moves the cursor/pointer to the start of the file
def rewind(f):
    f.seek(0)

# prints the line number and everything along that line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# opens the file then prints it
current_file = open(input_file)

print("Printing the whole file: \n")
print_all(current_file)

print("Rewinding the file.")
rewind(current_file)

print("Now print more lines.")

current_line = 1
print_a_line(current_line, current_file)

# +=, increments the value of the variable by any amount placed
# same as saying x = x + y is equal to x += y
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

print(current_file.readline())

#---------------------------------------------------------------------------#
