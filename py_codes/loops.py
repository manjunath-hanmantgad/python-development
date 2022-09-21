# -*- coding: utf-8 -*-
"""
@author: Manjunath
"""

from random import choice 
questions = ["why are you here?","what are you?", "where are you?"]

question = choice(questions)
answer = input(question)

answer = input("why is this here?")
while answer != "Just because":
    answer = input("why?")
    


# for loops 


#range(1,11)
for number in range(1,11):
    print(number)


vowels = 0
consonants = 0
for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1
print("there are {} vowels in the word".format(vowels))
print("there are {} consonant in the word".format(consonants))



students = {
    "male": ["AA","BB","CC","DD"],
    "female": ["aa","bb","cc","dd"]
    }
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
    #print(key)


even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)

prime_numbers = [x for x in range(1,101) if all(x % y != 0 for y in range(2, x))]
print(prime_numbers)


words = ["beautiful","woman"]
answer = [[w.upper(), w.lower(),len(w)] for w in words]
print(answer)


###############################

# pig latin project 

# take first consonant taken out and added in last and added with 'ay' 
# if starts with vowel then take that and add 'yay' at the end


'''
get the sentence from user 
split sentence into words 
loop through words 
stick words back together 
output final string

'''
original = input("enter a sentence here:").strip().lower()

words = original.split()
#print(words)

new_words = []

# if start with vowel add 'yay'
# else move first consonant to endd and add 'ay'

for w in words:
    if w[0] in "aeiou": # check if first letter is in vowels
        new_word = w + 'yay'
        new_words.append(new_word)
    else:
        vowel_position = 0
        for letter in w:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break # our consonants end here
        consonants = w[:vowel_position]
        the_rest = w[vowel_position:]
        new_word = the_rest +consonants + 'ay'
        new_words.append(new_word)
        
#print(new_words)

output = " ".join(new_words)
print(output)























































