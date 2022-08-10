#---------------------------------------------------------------------------#
# DAY 10 - 1
#---------------------------------------------------------------------------#
# LOOPS AND LISTS

# Lists, lists are a container of things that are organized from first to last
# these things are enclose by square brackets ['thing 1', 'thing 2', 'thing 3']
# things inside a list are separated by , comma
# the list are then assigned to a variable

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for, indicates a for loop then followed by a variable
# then the list to be iterated then ends with a colon
# yes, the succeeding code will be inside a for loop block
# it will be indented

# number is the variable that will be the placeholder for the items
# of the iteration from the_count
# then prints every iteration
for number in the_count:
    print(f"This is the count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# change is a mix of strings and integers, its fine
for i in change:
    print(f"I got {i}")

# building from an empty list is also possible
elements = []

# this loops from 0 to 11 but not including 11
for i in range(0, 11):
    print(f"Adding {i} to the list.")
    # then appends the items to the end of the list
    # append, a function that appends elements to a list
    elements.append(i)

# then we print
for i in elements:
    print(f"Element is: {i}")

#---------------------------------------------------------------------------#
# WHILE LOOPS
# while, indicates a while loop, followed by a statement then ends with a colon :
# if the statement is True, the next block of code will run
# the loop will continue to run until the statement will be false

i = 0
numbers = []

def looper(i, inc):
    # while i is <= to 8, the succeeding block of codes will ran in a loop
    while i <= 8:
        print(f"At the top is {i}")
        numbers.append(i)

        # this is the incrementor
        i += inc

        # this displays the current list per iteration
        print("Numbers now: ", numbers)
        print("At the bottom i is {}".format(i))


call_looper = looper(i, 2)
print(call_looper)

print("The numbers: ")

# loops through the final list
for num in numbers:
    print(num)

#---------------------------------------------------------------------------#