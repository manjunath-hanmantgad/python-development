# -*- coding: utf-8 -*-
"""

@author: Manjunath
"""
def add(x,y):
    return x+y

 
print(add(10,1))


def reverse(text):
    return text[::-1]

print(reverse("GoGoaGone"))
print(type(reverse("GoGoaGone")))


##############

# global VS local variable scope 

a = 250 # a is global variable
def f1():
    b= a + 100 
    print(b) # 350 will be printed

def f2():
    a = 50 # a here is local variable
    print(a)

print(f1())
print(f2())
print(a) # a here is global variable


#########################

print(1,2,3,4,5)
numbers = [1,2,3,4,5]
print(numbers)

print(*numbers) # unpacking 

def add (x,y):
    return x + y

print(add(10,1))


def add(*numbers):
    total =0
    for n in numbers:
        total = total + n
    return(total)

print(add(1,2,3,4,5))


def about(name,age,likes):
    sentence = "Meet {} , they are {},and they like {}".format(name,age,likes)
    return sentence

dict_1 = {'name':'N1','age':22, 'likes':'apples'}
print(about(**dict_1))






def foo(**kwargs):
    # produce a dict called kwargs 
    for key,value in kwargs.items():
        print("{},{}".format(key,value))

foo(animal="cow",likes="me")
print(foo)














