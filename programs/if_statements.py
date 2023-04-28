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

    