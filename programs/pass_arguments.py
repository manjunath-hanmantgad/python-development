'''
consider a function that builds a pizza. It needs to accept a number of toppings, but you can’t know ahead of time how many toppings a person will want. The function in the following example has one parameter, *toppings, but this parameter collects as many arguments as the calling line provides:
'''

def make_pizza(*toppings):
    """print list of toppings"""
    print(toppings)
    
make_pizza('pepper')
make_pizza('olives','jalapeno','cheese')


# Storing Your Functions in Modules

# Importing an Entire Module

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
