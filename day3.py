# DAY 3
#---------------------------------------------------------------------------#
# FILE HANDLING - READING FILES AND WRITING FILES

from sys import argv

script, filename = argv

print(f"We're going to delete {filename}.")
print("To cancel, hit CTRL-C (^C).")
print("To proceed, hit RETURN.")

input('?')

print("Opening {filename}...")
target = open(filename, 'w')


#---------------------------------------------------------------------------#
