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
# :, a colon, denotes that the next codes will be included in a block
# thus the need for indentation
if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

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
# ELIF STATEMENTS

people = int(input("How many humans? "))
cars = int(input("How many cars? "))
trucks = int(input("How many trucks? "))

if cars > people:
    print("We should take the cars.")

# elif, sets an else if statement then end with a colon
# provides another condition aside from the if statement
# then followed by an indented code which will execute if the if statement is True
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
# MAKING DECISION
# if statements within if statements

print("""You enter a dark room with two doors.\
Do you go through door #1 or door #2?""")

door = input('--> ')

# if this statement is True, the next block of code will run
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input('--> ')

    if bear == "1":
        print("The bear eats your face off. Good job!")
        print("Want to fight back? Yes or No")

        fight = input('--> ')

        if fight == 'Yes':
            print("You killed the bear! Good job murderer!")
        if fight == 'No':
            print("Scared!")

    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

# if this statement is True the next block of code will runs
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input('--> ')

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.") 
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.") 
        print("Good job!")

# when if and elif statements are not True, then else statement will run       
else:
    print("You stumble around and fall on a knife and die. Good job!")


#---------------------------------------------------------------------------#