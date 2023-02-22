'''
1. access and modify info inside a dict
2. loop through the dict
3. nest the dict inside lists
4. nest lists inside dicts 
5. nest dicts inisde dicts
'''
'''
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# A dictionary in Python is a collection of key-value pairs.

new_points = alien_0['points']
print(f"You just earned: {new_points} points!")

# Adding New Key-Value Pairs

# To add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets, along with the new value.

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Starting with an Empty Dictionary

# define a dictionary with an empty set of braces and then add each key-value pair on its own line.

alien_0 = {}
alien_0['w_position'] = 0
alien_0['z_position'] = 25

print(alien_0)

# Modifying Values in a Dictionary


#To modify a value in a dictionary, give the name of the dictionary with the key in 
#square brackets and then the new value you want associated with that key. 

alien_0['w_position'] = 100
print(alien_0)

#
'''
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# now changing default speed 
alien_0['speed'] = 'fast'
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # a fast alien 
    x_increment = 3
    
# new position = old + increment 
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# # now changing default speed 
# alien_0['speed'] = 'fast'


# A Dictionary of Similar Objects

'''
You can also use a dictionary to store one kind of information about many objects. For example, say you want to poll a number of people and ask them what their favorite programming language is. A dictionary is useful for storing the results of a simple poll.
'''

# breaking down larger dict into smaller dicts

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"sarah's fav language is: {language}")

# Looping through dictionary 

user_0 = {
    'username': 'efermi',
    'first_name': 'enrico',
    'last_name': 'fermi',
    }
for k , v in user_0.items():
    print(f"\nKey: {k}")
    print(f"\nValue: {v}")


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
    
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you like {language}.")
if 'erin' not in favorite_languages.keys():
    print("Erin please take the poll.")
    
    
# Looping Through a Dictionary’s Keys in a Particular Order

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"Thank you {name.title()} for taking our poll.")
    
    
# Looping Through All Values in a Dictionary

for l in favorite_languages.values():
    print(l.title())
    
###########################################################

# NESTING 

############################################################
# A List of Dictionaries


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# suppose there are 30 aliens 

aliens = []

for alien in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'medium'}
    aliens.append(new_alien)
    
# show first 5 aliens 
print(aliens[:5])

# total aliens created 
print(f"total aliens created: {len(aliens)}")

# now we want to change some features of aliens 

# change the first three aliens to yellow, medium-speed aliens worth 10 points each, 

for alien in aliens[:3]:
    if alien['color'] == 'green':
        #alien['color'] == 'yellow' # change green color to yellow color
        alien['color'] = 'yellow' # single = , not ==
        alien['speed'] = 'slow'
        alien['points'] = 10
# show first 5 aliens 
print(aliens[:5])


# List in a Dictionary

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")


favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name,language in favorite_languages.items():
    print(f"\n{name.title()} 's favorite languages are:")
    for l in language:
        print(f"\t{l.title()}")
        
        