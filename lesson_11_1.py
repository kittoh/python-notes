#---------------------------------------------------------------------------#
# DAY 11 - 1
#---------------------------------------------------------------------------#
# DOING THINGS TO LIST

# Manipulating Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar" 

print("Wait there are not 10 things in that list. Let's fix that.")

# split, splits a string into a list
# the whitespace is the separator
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # pop, removes an element from a list at a specified index
    # default value removes the last element
    # then it is stored in a variable
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff) 
print("Let's do some things with stuff.")

# prints the second item
print(stuff[1])
# prints the last item
print(stuff[-1]) # whoa! fancy 

print(stuff.pop())

# join, takes all the items from an iterable and attaches them in a string
print(' '.join(stuff))

# the hash(#) is the separator 
# [3:5] is a slice that calls out the item 3 and item 4, not including 5
# just like saying range(3, 5) 
print('#'.join(stuff[3:5]))

#---------------------------------------------------------------------------#
# DICTIONARIES

# dictionaries store data using key: value pairs
# dict is a form of a data structure
# dict have this format --> {'key1': 'value1', 'key2': 'value2'}
info = {
    'name': 'Kitto',
    'age': 18,
    'traits': [
        'Good guy!',
        'Not evil!',
        'Not bad!'
    ]
}

# adds items in the info dict
info['city'] = 'Japan'
info[1] = 'Coz why not?'

# this is how to access stuffs in a dict
print(info['name'])
print(info['age'])
print(info['traits'][0])
print(info['city'])
print(info[1])

#---------------------------------------------------------------------------#

# creates a mapping of state to their abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI' 
}

# this pairs to the previous states dict
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

print('-' * 10) # this is just a line separator
# adds some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
# prints cities from their states
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
# prints the abbreviation of the states
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print('-' * 10)
# this prints every state with their abbreviation
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}.")

print('-' * 10)
# prints every city in state
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city of {city}.")

print('-' * 10)
# prints the state with its abbreviation
# and its city
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}.")
    print(f"and has city {cities[abbrev]}.")

print('-' * 10)
# if there the state is not included
state = states.get('Texas')

if not state:
    print("Sorry not available.")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")


#---------------------------------------------------------------------------#
