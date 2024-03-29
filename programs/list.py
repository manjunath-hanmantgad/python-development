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


# looping through list 

'''
s = 'hi there my name is anthony gonsalves'
s[::-1]
'''


magicians = ['alice', 'david', 'carolina']
for m in magicians:
    #print (m) # alice, david, carolina
    #print(f"That was a great trick, MR. {m.title()}") #That was a great trick, MR. Alice
    print(f"We are looking forward to your tricks , Mr.{m}!!") #We are looking forward to your tricks , Mr.alice!!
    
    
# Doing Something After a for Loop

magicians = ['alice', 'david', 'carolina']
for m in magicians:
    #print (m) # alice, david, carolina
    print(f"That was a great trick, MR. {m.title()}") #That was a great trick, MR. Alice
    print(f"We are looking forward to your tricks , Mr.{m}!!\n") #We are looking forward to your tricks , Mr.alice!!
print("Thank you for your tricks!!")


pizzas = ['tomato','cheese','sqaure']
for p in pizzas:
    #print(p)
    print(f"I like {p.title()} pizza!")
print("I love pizza!!")


animals = ["cat","dog","horse"]
for a in animals:
    #print(a)
    print(f"{a.title()} would make a great pet!")
print("Any animal will make a grate pet!!")


# making use of range function

for number in range(1,10):
    print (number)

# convert range to list

numbers = list(range(1,10))

# even numbers

even_number = list(range(2,11,2))
type(even_number) # range ; # list

sqaures = []
for v in range(1,11):
    square = v ** 2
    sqaures.append(square) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(sqaures)

# list comprehensions

squares = [v ** 2 for v in range(1,11)]
print(squares)

numbers = [n for n in range(1,21)]
print(numbers) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

odd_numbers = list(range(1,21))
odd = [n for n in odd_numbers if n%2 == 1]

# using enumerate

list1 = range(1,21)
for k,v in enumerate(list1):
    if v%2 !=0:
        print(v, end=" ")
# Time Complexity: O(N)

threes = [t*3 for t in range(3,31)]
print(threes)

cubes = [c**3 for c in range(1,11)]
print(cubes)


# slicing


players = ['charles', 'martina', 'michael', 'florence', 'eli']
players[0:3]
players[:4]

# slice which includes end of list
players[2:]
players[-3:] # ['michael', 'florence', 'eli']
players[:-3] #['charles', 'martina']
players[::1] #Out[84]: ['charles', 'martina', 'michael', 'florence', 'eli']

players[::-1] #['eli', 'florence', 'michael', 'martina', 'charles']

# Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are first three players in my team:\n")
#print("Here are last three players of my team:\n")
for p in players[:3]:
    print(p) 
'''
charles
martina
michael
'''
print("Here are last three players of my team:\n")
for j in players[2:]:
    print(j)
    '''
    michael
    florence
    eli
    '''

# copying a list

'''
To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
'''
my_foods = ['pizza', 'falafel', 'carrot cake','blueberry','strawberry']
friend_foods = my_foods[:] # copying the entire my_foods list

my_foods == friend_foods # True



print("first three items in my_foods are:")
for f in my_foods[:3]:
    print(f)

print("three items from middle of the list are:")
for i in my_foods[1:4]: 
    print(i) #'falafel', 'carrot cake','blueberry',
print("last three items in list are:")
for k in my_foods[2:]:
    print(k) #carrot cake','blueberry','strawberry'



pizza = ['tomato','cheese','corn','apple']
friend_pizza = pizza[:] # copied pizza to friend_pizza
#pizza == friend_pizza # True
pizza.append('mushroom')
print(pizza) #['tomato', 'cheese', 'corn', 'apple', 'mushroom']
friend_pizza.append('macaroni')
print(friend_pizza) #['tomato', 'cheese', 'corn', 'apple', 'macaroni']

print("My favorite pizza are:\n")
for i in pizza:
    print(i)
print("My friends favorite pizza are:\n")
for j in friend_pizza:
    print(j)


# tuples

'''
sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that. Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
'''

tuple_1 = (1,2) # notice the brackets
type(tuple_1)
tuple_1[0] = 10 #TypeError: 'tuple' object does not support item assignment

tuple_single_element = (1,) # 1


# looping through tuple

tuple_loop = (range(1,11))
for t in tuple_loop:
    print(t)
    
# tuples work ok when reassigning them

tuple_loop = range(1,5)
for i in tuple_loop:
    print(i)

















