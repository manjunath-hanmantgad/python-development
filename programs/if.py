cars = ['audi', 'bmw', 'subaru', 'toyota']

for c in cars:
    if c == 'bmw':
        print(c.upper())
    else:
        print(c.title())
        
# checking whether value is present in list or not 

banned = ['andy','elon','jeffy','billy']
user = 'zoey'

if user not in banned:
    print(f"User {user.title()}, is good player!")
    
# using if with lists 

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for r in requested_toppings:
    print(f"Adding {r.title()} in your pizza now!!")
    
# what if one element is not present 

for r in requested_toppings:
    if r == 'extra cheese':
        print("You have to pay extra if you want.")
    else:
        print(f"Adding the {r.title}")
        
# checking list is not empty.

r = []
if r:
    for r in requested_toppings:
        print(f"Adding {r.title()}")
else:
    print("Are you sure you want this?")
    
# check first and then second list 

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for r in requested_toppings:
    if r in available_toppings:
        print(f"Adding {r.title()} to your pizza!")
    else:
        print(f"Sorry we are out of {r}")

print("\nYour pizza is ready!")