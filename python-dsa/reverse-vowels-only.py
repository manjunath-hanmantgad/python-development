#### 2 POINTERS

def reverse_vowels(s):
    #create a set vowels that contains all the vowel characters, both lowercase and uppercase.
    vowels = set('aeiouAEIOU')
    s = list(s) #to modify the characters in-place since strings are immutable in Python.
    #initialize two pointers, i and j, pointing to the start and end of the string respectively.
    i,j = 0, len(s)-1
    # while loop that continues until i is less than j.
    while i < j:
        #check if the character at s[i] is a vowel and the character at s[j] is also a vowel
        if s[i] in vowels and s[j] in vowels:
            # If both characters are vowels, we swap them using a simultaneous assignment.
            s[i],s[j] = s[j],s[i]
            #increment i and decrement j to continue searching for other pairs of vowels.
            i += 1
            j -= 1
            #If the character at s[i] is a vowel but the character at s[j] is not, we only decrement j to skip the non-vowel character.
        elif s[i] in vowels:
            j -= 1
        else:
            i += 1
    return ''.join(s)

s = 'Hello'
s1 = 'HelloUaA'
output = reverse_vowels(s1)
print(output)

'''
Manjunath@LAPTOP-6OTHQMEE MINGW64 /d/development/python-development/python-dsa (master)
$ python reverse-vowels-only.py 
HolleW

Manjunath@LAPTOP-6OTHQMEE MINGW64 /d/development/python-development/python-dsa (master)
$ python reverse-vowels-only.py 
HUlloe

Manjunath@LAPTOP-6OTHQMEE MINGW64 /d/development/python-development/python-dsa (master)
$ python reverse-vowels-only.py 
HAllaUoe

'''
'''
The function reverse_vowels takes a string s as input and returns the string with reversed vowels.

We create a set vowels that contains all the vowel characters, both lowercase and uppercase.

We convert the string s into a list of characters using list(s). This allows us to modify the characters in-place since strings are immutable in Python.

We initialize two pointers, i and j, pointing to the start and end of the string respectively.

We enter a while loop that continues until i is less than j.

Inside the loop, we check if the character at s[i] is a vowel and the character at s[j] is also a vowel. If both characters are vowels, we swap them using a simultaneous assignment. Then, we increment i and decrement j to continue searching for other pairs of vowels.

If the character at s[i] is a vowel but the character at s[j] is not, we only decrement j to skip the non-vowel character.

If the character at s[i] is not a vowel, we only increment i to skip the non-vowel character.

Finally, we join the modified list of characters back into a string using ''.join(s) and return the result.
'''

'''
The time complexity of this solution is O(N), where N is the length of the input string s. We iterate through the string from both ends simultaneously until the pointers meet in the middle.

The space complexity is O(N) as well since we convert the string s into a list of characters, which requires additional space proportional to the length of the string.
'''
################### 
## EDGE case

#####################

'''
If the input string s is empty, the function will return an empty string since there are no characters to reverse.
If there are no vowel characters in the string s, the function will return the original string as there are no vowels to reverse.
If the string s consists of only vowel characters, the function will return the string with the vowels reversed.
'''
