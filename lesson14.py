#---------------------------------------------------------------------------#
# DAY 13
#---------------------------------------------------------------------------#
# INHERITANCE VS COMPOSITION

#-------------------------------------------------------------#
# Implicit Inheritance

class Parent:

    def implicit(self):
        print("PARENT implicit()")

# class Child inherits the traits of Parent
class Child(Parent):
    # pass, indicates an empty block
    pass

# instantiates dad object using Parent class
dad = Parent()
# instantiates son object using Child class which inherits from Parent class
son = Child()

# dad object calls out implicit action
dad.implicit()
# son object can also call implicit action since it inherits that
# from the Parent class
son.implicit()

#-------------------------------------------------------------#
# Override Explicitly

class Parent:

    def override(self):
        print("PARENT override()")

# class Child inherits the traits of Parent
class Child(Parent):
    
    def override(self):
        print("CHILD override()")


dad = Parent()
son = Child()

# dad object calls out override action
dad.override()
# son object can also call override action since it inherits that
# from the Parent class
son.override()

#-------------------------------------------------------------#
# Alter Before or After

class Parent:

    def altered(self):
        print("PARENT altered()")

# class Child inherits the traits of Parent
class Child(Parent):
    
    def altered(self):
        # this alters the Parent.altered
        print("CHILD BEFORE PARENT altered()")
        # super, calls the function of the parent
        super(Child, self).altered()
        # this alters after Child.altered
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

# dad object calls out alteredv action
dad.altered()
# son object can also call altered action since it inherits that
# from the Parent class
son.altered()

#-------------------------------------------------------------#
# Composition

class Other:

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child:

    # this functions takes the methods of class Other
    # then gives it to the Child
    # now Child has-a Other traits
    def __init__(self): 
        self.other = Other()

    def implicit(self): 
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()
son.implicit()
son.override()
son.altered()


#---------------------------------------------------------------------------#


