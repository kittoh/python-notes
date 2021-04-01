#---------------------------------------------------------------------------#
# DAY 10 - 2
#---------------------------------------------------------------------------#
# ACCESSING ELEMENTS OF LISTS

# elements in a list have their own address called inex
# they can then be accessed by indicating their respective indices

animals = ['bear', 'python3.9', 'peacock', 'kangaroo', 'whale', 'platypus']

# these are printing the animals by pulling them using their indices
print("The animal at 1 is {}.".format(animals[1]))
print("The third(3rd) animal which is the animal at 2 is the {}.".format(animals[2]))
print("The animal", animals[0], "is at 0 and is the first animal.")
print("The animal at 3 is the fourth(4th) which is the {}.".format(animals[3]))

fifth_animal = animals[4]
print(f"The {fifth_animal} is at 4 and is the fifth animal.")

print("The animal at 2 is also the third(3rd) animal which is the {}.".format(animals[2]))
print("The sixth(6th) animal is the {} which is at 5.".format(animals[5]))
print("The animal at 4 is the fifth animal which is the {}.".format(animals[4]))

#---------------------------------------------------------------------------#
# BRANCHES AND FUNCTIONS

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    choice = input('--> ')

    # try, this is responsible when testing for error in the block of code
    try:
        how_much = int(choice)
    # except, this code block handles the error
    except ValueError:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        # exit quits the program 
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.") 
    print("How are you going to move the bear?") 
    bear_moved = False
    
    # this will always be True, thus will loop infinitely
    while True:
        choice = input('--> ')
    
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved: 
            print("The bear has moved from the door.") 
            print("You can go through it now.") 
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.") 
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.") 
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else: cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit()

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.") 
    print("Which one do you take?")

    choice = input('--> ')
    
    if choice == "left":
        bear_room()
    elif choice == "right": 
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# this executes the program
start()


#---------------------------------------------------------------------------#