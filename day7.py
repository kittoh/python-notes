#---------------------------------------------------------------------------#
# DAY 7
#---------------------------------------------------------------------------#
# PRACTICE 1

# printing escape characters, new line, tabbing
print("PRACTICE!")
print('Let\'s escape! this slashes \\ \\ yes!')
print("\nNEW Line! Tabbing \t tabs.")

# multi-line printing
print("""
This
is a
multi-line
printing...
""")

# numbers and operations
# f printing
eight = 10 - 5 + 4 -1
print(f"This should be eight {eight}!")

# defining a function
def secret_formula(started):
    jelly_beans = started * 500 
    jars = jelly_beans / 1000 
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 1000
# multi-variable designation
beans, jars, crates = secret_formula(start_point)

# print formatting
print("With a starting point of {}".format(start_point))

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("or this way.")

# function as an argument
formula = secret_formula(start_point)

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

#---------------------------------------------------------------------------#
# PRACTICE 2

# a function that returns splitted words
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# a function that returns words that are arranged alphabetically
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# a function that returns the first word from the list
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) 
    print(word)

# a function that returns the last word from the list
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) 
    print(word)

# a function that returns alpabetically arranged words from a sentence
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) 
    return sort_words(words)

# a function that returns the first and last words from a sentence
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence) 
    print_first_word(words) 
    print_last_word(words)

# a function that returns the first and last words from a sorted sentence
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# """documentation comments""", these are comments that serves as help guidelines
# help(script), this will run the help guidelines

#---------------------------------------------------------------------------#


#---------------------------------------------------------------------------#