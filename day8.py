#---------------------------------------------------------------------------#
# DAY 8
#---------------------------------------------------------------------------#
# LOGIC - THE TRUTH

# and, or, not
# != (not equal)
# == (is equal?)
# >= (greater than or equal)
# <= (less than or equal)
# True, False

# not, reverses the logic
not False = True
not True = False

# or, only  needs 1 True to be True
True or False = True
True or True = True
False or True = True
False or False = False

# and, needs both to be True
# 1 False and its False
True and False = False
True and True = True
False and True = False
False and False = False

# not, reverses the logic in the parenthesis
not(True or False) = False
not(True or True) = False
not(False or True) = False
not(False or False) = True

# not, reverses the logic in the parenthesis
not(True and False) = True
not(True and True) = False
not(False and True) = True
not(False and False) = True

# !=, if not equal then True
1 != 0 # True
1 != 1 # False
0 != 1 # True
0 != 0 # False

# ==, if equal then True
1 == 0 # False
1 == 1 # True
0 == 1 # False
0 == 0 # True
 
#---------------------------------------------------------------------------#
# PRACTICE

True and True # True
False and True # False
1 == 1 and 2 == 1 # False
"test" == "test" # True
1 == 1 or 2 != 1 # True
True and 1 == 1 # True
False and 0 != 0 # False
True or 1 == 1 # True
"test" == "testing" # False
1 != 0 and 2 == 1 # False
"test" != "testing" # True
"test" == 1 # False
not (True and False) # True
not (1 == 1 and 0 != 1) # False
not (10 == 1 or 1000 == 1000) # False
not ("testing" == "testing" and "kittoh" == "Awesome Human!") # True
1 == 1 and (not("testing" == 1 or 1 == 0)) # True
"chunky" == "bacon" and (not(3 == 4 or 3 == 3)) # False
3 == 3 and (not("testing" == "testing" or "Python" == "Fun")) # False


#---------------------------------------------------------------------------#