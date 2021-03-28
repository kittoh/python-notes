#---------------------------------------------------------------------------#
# DAY 5
#---------------------------------------------------------------------------#
# FUNCTION RETURNING SOMETHING

# defines a function that accepts arguments
# the output of this function will be returned as a value
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

# calling the function as a value for a variable
age = add(5, 15)
height = subtract(80, 10)
weight = multiply(55, 2)
iq = divide(250, 2)

# printing the output thru f strings
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# functions are called as an argument for another function
print("Puzzle!")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("Answer is ", what)

#---------------------------------------------------------------------------#