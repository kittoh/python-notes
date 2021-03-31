#---------------------------------------------------------------------------#
# DAY 9
#---------------------------------------------------------------------------#
# IF STATEMENTS

people = int(input("How many humans? "))
cats = int(input("How many cats? "))
dogs = int(input("How many dogs? "))

# if, sets an if statement then ends with a colon :
# then followed by an indented code which will execute if the if statement is True
# an indentation error will occur if not indented
if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

# dogs += 5 is the same as dogs = dogs + 5
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs: 
    print("People are dogs.")

#---------------------------------------------------------------------------#
# ELSE IF

people = int(input("How many humans? "))
cars = int(input("How many cars? "))
trucks = int(input("How many trucks? "))

if cars > people:
    print("We should take the cars.")

# elif, provides another condition aside from the if statement
elif cars < people:
    print("We should not take the cars.")

# else, when if and elif statements are not met, this will execute
else:
    print("Can't tell!")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks and people > cars:
    print("Alright, what to do?.")
else:
    print("Fine, let's stay home then.")


#---------------------------------------------------------------------------#