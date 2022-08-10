#---------------------------------------------------------------------------#
# DAY 12
#---------------------------------------------------------------------------#
# LEARNING TO SPEAK OBJECT-ORIENTED

# A Reading Test

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt" 
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** params.", 
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.", 
    "*** = %%%()":
        "Set *** to an instance of class %%%.", 
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.", 
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}


if len(sys.argv) == 2 and sys.argv[1] == "english": 
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines(): 
    WORDS.append(str(word.strip(), encoding="utf-8"))
    # print(word)

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))] 

    other_names = random.sample(WORDS, snippet.count("***"))
    results = [] 
    param_names = []

    for i in range(0, snippet.count("@@@")): 
        param_count = random.randint(1,3) 
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        # this is how you duplicate a list or string
        result = sentence[:]
        
        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
            
        results.append(result) 
            
    return results


try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
    
    for snippet in snippets:
        phrase = PHRASES[snippet]
        question, answer = convert(snippet, phrase) 
        
        if PHRASE_FIRST:
            question, answer = answer, question
        print(question)

        input('-->')
        print(f"ANSWER:  {answer}\n\n")

except EOFError:
    print("\nBye")

#---------------------------------------------------------------------------#
# IS-A, HAS-A, OBJECTS AND CLASSES

# Animal is-a object
class Animal(object):
    pass

# Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        # a Dog has-a name
        self.name = name

    def bark(self):
        print("Arf! Arf! I'm wagging my tail, hey!")

# Cat is-a animal
class Cat(Animal):
    
    def __init__(self, name):
        # Cat also has-a name
        self.name = name

# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # super, gives access to all methods and properties from another class
        super(Employee, self).__init__(name)
        # Employee, which is a person, has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    def swim(self):
        print("I'm swimming!")

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog('Rover')

# satan is-a Cat
satan = Cat('Satan')

# mary is-a Person
mary = Person('Mary')

# mary has-a pet, Satan
mary.pet = satan

# Frank is-a Employee, which has-a 10000 as salary
frank = Employee('Frank', 10000)

# Frank has-a pet, Rover
frank.pet = rover
rover.bark()

# flipper is-a Fish
flipper = Fish()
flipper.swim()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()

#---------------------------------------------------------------------------#


