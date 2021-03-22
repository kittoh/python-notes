# DAY 3
#---------------------------------------------------------------------------#
# FILE HANDLING - READING FILES AND WRITING FILES

from sys import argv

script, filename = argv

print(f"We're going to delete {filename}.")
print("To cancel, hit CTRL-C (^C).")
print("To proceed, hit RETURN.")

input('?')

# prints an indication, then opens the file
# w means opens the file as a writable file
print("Opening {filename}...")
target = open(filename, 'w')

# truncate, means deleting the content of the file
print("Deleting the content of {}...".format(filename))
target.truncate()

# asking for input then writes it in the file
print("Gimme three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# or a prettier approach
target.write(f"{line1}\n{line2}\n{line3}")

# then closes the file
print(f"Closing the {filename}...")
target.close()

#---------------------------------------------------------------------------#
