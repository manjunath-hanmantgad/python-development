# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:42:27 2023

@author: Manjunath
"""

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        

# Conditional Tests
 #At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test.

#Checking Whether a Value Is in a List

requested_toppings = ['mushrooms', 'onions', 'pineapple']
plant = 'potato'
#'mushrooms' in requested_toppings

if plant not in requested_toppings:
    print(f"{plant} not found here!")
    
# if;else chain

age = 12
if age < 4:
    print("Enter for free")
elif age <18:
    print("You need to pay 20 rs")
else:
    print("You need to pay 40rs")
    
# another way to write it:
    
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 20
else:
    price = 40
print(f"You need to pay Rs {price}!!")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'macroni' in requested_toppings:
    print("Adding macroni")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese")
print("Preparing your pizza now!")


alien_color = ['green','yellow','red']
#alien_color = yellow
if 'green' in alien_color:
    print("You earned 5 points!!")
if alien_color != 'green':
    print("You earned 10 points!")

if 'green' in alien_color:
    print("You earned 5 points")
if 'yellow' in alien_color:
    print("You earned 10 points")
if 'red' in alien_color:
    print("You earned 15 points")
    
    
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for r in requested_toppings:
    #print(f"Adding {r} in your pizza")
    '''out of green pepper'''
    if r == 'green peppers':
        print("Sorry we are out of GP currently")
    else:
        print(f"Adding {r} to your pizza!")

requested_toppings = [] # empty list
if requested_toppings:
    for r in requested_toppings:
        print(f"Adding {r}")
    print("Finished adding all.")
else:
    print("Guess you want a plain pizza")
    

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for r in requested_toppings:
    
    if r in available_toppings:
        print(f"Adding {r} as topping!")
    else:
        print("Sorry out of the {r}")
print("Pizza is ready")



users = ['aa','bb','cc','admin','dd']
for u in users:
    print("Hello there {u.title()}")



























