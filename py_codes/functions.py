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