#---------------------------------------------------------------------------#
# PRACTICE 1
#---------------------------------------------------------------------------#

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