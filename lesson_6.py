#---------------------------------------------------------------------------#
# DAY 6
#---------------------------------------------------------------------------#

# STRINGS, BYTES, AND CHARACTER ENCODINGS
# this encodes string into bytes then decodes it back to string
from sys import argv

script, input_encoding, error = argv

# defines main function that accepts 3 arguments
# then declared line variable that will read each line from the file
def main(language_file, encoding, errors):
    line = language_file.readline()

    # if statement - states conditions that when true,
    # then the succeeding codes will run
    # main is called to make a loop
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

# print_line, this encodes the string in each line from the file
# then decodes it back
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<--->", cooked_string)

# opens the file to be processed
languages = open('languages.txt', encoding="utf-8")

# calls main with the appropriate parameters
main(languages, input_encoding, error)

# command to run: python3.x yourscript.py utf-8 strict


#---------------------------------------------------------------------------#