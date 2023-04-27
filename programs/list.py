# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:37:06 2023

@author: Manjunath
"""

bicycles = ['trek','cannon','redline','special']

#Accessing Elements in a List
bicycles[0]
bicycles[0].title()
bicycles[-1]

#Using Individual Values from a List
# use f strings for this 

message = f"My first bicycle is {bicycles[0].title()}"
print(message)


names = ['a','b','c','d']
names[0]
names[1]
names[2]
names[3]

message = f"Hello there {names[0].title()}" #names[1,2,3]

bikes = ['honda','crv']
message = f"I would like to ride {bikes[0]}"
print(message)
message_1 = f"I would like to drive {bikes[1]}"
print(message_1)


# Modifying, Adding, and Removing Elements

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
motorcycles.append('crv')

motorcycles = []
motorcycles.append('aa')
motorcycles.append('bb')

# Inserting Elements into a List

motorcycles.insert(0, 'zz') # zz,aa,bb

# Removing Elements from a List
del motorcycles[0] ## aa,bb

# Removing an Item Using the pop() Method
popped_motorcycle = motorcycles.pop() #bb

# Sorting a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
c = cars.sort(reverse=True) #Nonetype
cars.sort(reverse=True) #'bmw', 'audi', 'toyota', 'subaru'


# sorted function

'''
To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. The sorted() function lets you display your list in a particular order, but doesn’t affect the actual order of the list.
'''
sorted(cars)


# rreverse order
cars.reverse()
cars=cars[::-1] #subaru toyota audi bmw 

places = ['ab','bc','cd','de','ef']
sorted(places)
places.reverse()
places.sort(reverse=True)
len(places)






























