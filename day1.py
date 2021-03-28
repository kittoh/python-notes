#---------------------------------------------------------------------------#
# DAY 1
#---------------------------------------------------------------------------#
# FIRST PROGRAM, PRINTING STATEMENTS

# print, is function that displays text(string)
# anything within a set of single(' ') and double(" ") quotes are strings
print("This will be a print statement")
print('Print THIS!')
print('AGAIN!')

# This is a comment! @#$%^&*(!?!
# the hash symbol #, makes the succeeding characters a comment, 
# anything that is after the # will be ignored when the program is run

# a set of single quotes(' ') within a double quoted(" ") strings 
# or vice-versa, is considered a part of the string thus will be included in printing
print("Ain't 'easy', is it?")
print('Do "it" please?')

# \n denotes printing on a new line
# \t tabs the next character/s
print('1\n2\n3')
print('1\t2\t3')

# \ symbol, encodes some characters into strings
print("That guy is 5'8\" tall.")

# backslash \ is an escape character
# escape character escapes the functionality of the succeeding character,
# meaning it removes its functionality thus printing it as it is

# Printing of multi-line strings
print("""
First line
Second line
3rd line
4th line
"5th line!"
""")

# Printing of statements can be used for displaying descriptive results 
# or anything you want to know about anything within your program

#---------------------------------------------------------------------------#
# NUMBERS AND OPERATIONS

# This will print the strings within the double quotes
# and anything not included is considered an operation
# depends on what is written there.
print("Addition: 2 + 5 = ", 2 + 5)
print("Subtraction: 8 - 4 = ", 8 - 4)

# Other Math Symbols: * / % < > <= >=

# The modulus symbol %, is a division operand that spits out 
# the remainder of the operation
print("Remainder: 7 % 2 = ", 7 % 2)
print("Remainder: 10 % 5 = ", 10 % 5)

# the <, > symbols ask for comparison, if the values are less than or greater than 
# then returns True or False
# the == symbol, checks for equality and also returns True or Fals
print("Is 8 greater than 12?", 8 > 12)
print("Is 10 equal to 15", 10 == 15)

#---------------------------------------------------------------------------#
# VARIABLES

# Strings and numbers can be assigned to variables
# Strings are assigned within single or double quotes
# Numbers(Integers or Float) are assigned just by putting the numbers
name = 'Kitto'
age = 18
height_in_meters = 1.72

# Variables can then be inserted in print statements
print("Hi! I'm", name, "!")
print("I'm", age, "years old.")

# Converts meters to feet then prints it
height_in_feet = (height_in_meters * 100 / 2.54) / 12
print("I'm", height_in_feet, "feet tall.")

# A more efficient way of inserting variables is thru print formatting
print(f"Hi I'm {name}!")
print(f"I'm {age} years old.")

# Another kind of formatting
# name, age variables are inserted via .format
print("Hi! I'm {0}! I'm {1} years old. I'm {0} btw.".format(name, age))

#---------------------------------------------------------------------------#
# ASKING FOR USER INPUT

# end=': ' tells to end statement with : then to proceed to the next line 
# without putting it on a new line
print("Gimme your name", end=': ')
name = input()
print("Gimme your passkey", end=': ')
passkey = input()

# input a number
# int converts the input into an integer so that it can be used for math operations
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
print(f"{x} + {y} = ", x + y)

#---------------------------------------------------------------------------#
