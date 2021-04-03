#---------------------------------------------------------------------------#
# DAY 11 - 2
#---------------------------------------------------------------------------#
# MODULES, CLASSES AND OBJECTS

#-------------------------------------------------------------#
# this script can be imported by another script as a module
def apple():
    print("I am an apple!")

# add variable
tangerine = "I dream as I walk in paradise"

#-------------------------------------------------------------#
# from a separate script
import yourscript
# this runs the module then calls the apple function
yourscript.apple()
# this prints the variable
print(yourscript.tangerine)

#-------------------------------------------------------------#
# class, instantiates a class 
# this is followed by a class name, MyClass()
# then ends with a colon :
# yes, the next codes enters a block and are to be indented

class MyStuff(object):
    # this is initialized when an object is created
    def __init__(self):
        self.tangerine = "And so I travelled time, million years of journey."

    # just another function within a class
    def apple(self):
        print("I'm super Apple!")

# this instantiates a class
stuff = MyStuff()
stuff.apple()
print(stuff.tangerine)

#-------------------------------------------------------------#
# 3 Ways to Get Things from Things

# dict style
mystuff['apples']

# module style
mystuff.apples()

# class style
stuff = MyStuff()
stuff.apples()
print(stuff.tangerine)

#-------------------------------------------------------------#

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    # function that iterates over every line
    def sing_me_a_song(self): 
        for line in self.lyrics:
            print(line)

# this will supplied as a parameter upon instantiation
hbd_lyrics = [
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"
    ]

bulls_lyrics = [
    "They rally around tha family",
    "With pockets full of shells"
    ]

# this instantiates an object
happy_bday = Song(hbd_lyrics) 
bulls_on_parade = Song(bulls_lyrics) 

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

#---------------------------------------------------------------------------#


