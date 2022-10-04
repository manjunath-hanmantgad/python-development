# -*- coding: utf-8 -*-
"""
@title: basics

@author: Manjunath
"""

# variables 

message = "Hello world!" # message is a variable
print(" ")
print(message)

message = "Hello again!"
print(message)

# strings 

# changing cases 

name = "some random"
name = "FOO BAR"
name = "Foo Bar"
print(name.title()) # title is a method , . after name tells name to execute title method on name(itself).
print(name.lower())
print(name.upper())

# variables in strings

first_name = "x"
last_name = "y"
full_name = f"{first_name} is first name and {last_name} is last name."
long_name = f"{first_name} {last_name}"
print(full_name)
print(long_name)
print(f"long_name is {long_name.upper()}")

message = f"Hello there {full_name.title()}"
print(message)

''' adding whitespaces in strings '''
print("\t Hello")
print("\n Hello_1, \n Hello_2, \n Hello_3")


''' removing prefixes '''
url_1 = "https://nohello.com"
url_1.removeprefix("https://")
print(url_1)


name = "foo"
message = f"{name} would you like a piiza ?"
print(message)
print(f"{name.title()}")
print(f"{name.upper()}")
print(f"{name.lower()}")

print('Mr.X once said, "You are what you are!"')
famous_person = "Mr.X"
message = "You are what you are!"
print(f"{famous_person} once said {message}")


print('a**b') # hackerrank problem


''' multiple values assignment '''

x,y,z = 1,2,3
print(x,y,z)

'''CONSTANTS are represented with capital letters , we are not supposed to change CONSTANTS '''


fav_nr = 7
print(f"my favorite number is {fav_nr}")


# lists 

numbers = [1,2,3,4]
print(numbers)
print(type(numbers))

''' accessing items in list '''
print(numbers[0])
print(numbers[-1])
message = f"My favorite number amongst given number is {numbers[0]}"
print(message)

names = ['foo', 'fii','bar']
print('My fellow members of board are :', f"{names[0], names[1], names[2]}")

message = "Hello there"
print(f"{message} {names[0]}")

names = ['foo', 'fii','bar'] # changing elements in list 
names[0] = 'fufu'
print(names)

names.append('7') # adding nw element , notice that it supports string and int.
print(names)

names.insert(4, '8') # adding 8 at fourth index position
print(names)
names.insert(0,'hoohaa')
print(names)



''' organizing a list '''

# sorting permanently 

names = ['aa','bb','zz','yy']
names.sort()
print(names)
#print(names.sort(reverse=True))
names.reverse() # reverse order
print(names)
len(names) # gives number of elements in list


places = ['aa','cc','dd','bb','ee'] # 5 elemnts
len(places) # 5
print(f"'Original order of list is:' {places}")
print("\nHere is sorted list:")
print(sorted(places))
print("\nHere is places in reverse alpha order:")
places .reverse()
print(places)
print("\nOriginal list is still intact:") # after reverse doesnt work
print(places)
print("\nNow sorted list is:")
places.sort()
print(places)
print("\nNow reverseing the sorted list:")
places.reverse()
print(places)


''' looping through the lists '''

# using for loops 

names = ['foo','bar','random']
for name in names:
    #name.upper()
    #print(name)
    print(f"{name.upper()}, are names in capital letters.")
    print(f"See you soon guys! , {name.lower()}.\n") # each line will be executed once as its a for loop.
print(f"{name} thank you guys!")


pizza = ['aa','bb','cc']
for i in pizza:
    #print(i)
    #print(f"I like pizza {i}\n")
    print(f"I like pizza {i}")
print("I like the mentioned pizza.")


''' numerical lists '''

# using range function

for value in range(1,100):
    print(value) #prints till 99 , not 100

numbers = list(range(100)) # converting range into list
print(numbers)
print(type(numbers)) # list 

sqaures = []
for value in range(50):
    square = value ** 2
    sqaures.append(square)
print(sqaures)


# better code 

sqaures = []
for value in range(50):
    sqaures.append(value ** 2)
print(sqaures)

numbers = list(range(3,30,3))
print(numbers)


''' slice in python '''

numbers = list(range(10))
print(numbers)
print(numbers[0:3]) # prints numbers at index 0,1,2 

print(numbers[2:]) # start from index 2 and get all rest

print(numbers[-3:]) # gives last 3 numbers 

print("Here are first 3 numbers:")
for number in numbers[:3]:
    print(number)
 