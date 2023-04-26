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
