""" 
A function doesn’t always have to display its output directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function.
"""

# function that takes a first and last name, and returns a neatly formatted full name:

def formatted_name(first,last):
    """return first and last name"""
    full = f"{first} {last}"
    return full.title()

# apply this function 

rapper = formatted_name('emiway','bantai')
print(f"\nMy favorite rapper is {rapper.title()}")