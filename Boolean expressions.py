# example_statement = "My dog is the cutest dog in the world" (this is not a Boolean expression)
example_statement = "No"

# statement_one = "Dogs are mammals" (this IS a Boolean expression)
statement_one = "Yes"

# statement_two = "My dog is named Pavel" (this IS a Boolean expression)
statement_two = "Yes"

# statement_three = "Dogs make the best pets" (this is not a Boolean expression)
statement_three = "No"

# statement_four = "Cats are female dogs" (this is not a Boolean expression)
statement_four = "Yes"

# Relational Operators: equals and not equals

# Relational operators compare two items and return either True or False. 
# For this reason we sometimes call them Comparators.
# The first two relational operators we will cover are equals: == and not equals: !=

# 1 Determine if the following boolean expressions are True or False. 

# statement_one = (5*2) - 1 == 8+1 
statement_one = True

# statement_two = 13-6 != (3*2) + 1 
statement_two = False

# statement_three = 3 * (2-1) == 4-1
statement_three = True

# When True and False are their own special type, "bool" they appear in a different color.
# They are not the same color as variables or strings. 
# Any variable that is assigned one of these values is a BOOLEAN VARIABLE.

# Boolean variables can be created in several ways. The easiest way is to assign T or F to a variable

set_to_true= True
set_to_false= False

bool_one= 5!=7
bool_two= 1+1 !=2
bool_three=3*3 ==9

print (bool_one) #True
print (bool_two) #False
print (bool_three) #True

my_baby_bool= "true"
print (type(my_baby_bool)) # this is checking the type of my_baby_bool
my_baby_bool_two=True
print (type(my_baby_bool_two)) # this is checking the type of my_baby_bool_two
