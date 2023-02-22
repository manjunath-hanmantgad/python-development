""" 
Because a function definition can have multiple parameters, a function call may need multiple arguments. You can pass arguments to your functions in a number of ways. 
"""

# Positional Arguments

'''
When you call a function, Python must match each argument in the function call 
with a parameter in the function definition.
The simplest way to do this is based on the order of the arguments provided.
Values matched up this way are called positional arguments.
'''
# order is important 

def describe_pet(animal_type, pet_name):
    """display info about pet"""
    print(f"\nI have {animal_type} as pet.")
    print(f"\nMy {animal_type}'s name is {pet_name}")

describe_pet('dog','bunty')
# here I cant give as ('bunty','dog')
# bcoz this will change ordering.


# Keyword Arguments

'''
A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion
'''
def describe_pet(animal_type, pet_name):
    """display info about pet"""
    print(f"\nI have {animal_type} as pet.")
    print(f"\nMy {animal_type}'s name is {pet_name}")

describe_pet(animal_type='cat',pet_name='bubbly')
