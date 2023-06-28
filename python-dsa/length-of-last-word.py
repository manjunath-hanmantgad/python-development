def length_of_last_word(s):
    #use the rstrip() function to remove any trailing spaces from the string s. 
    # This step ensures that we don't count any spaces after the last word.
    s=s.rstrip()    
    #initialize a variable length to keep track of the length of the last word. 
    # Initially, it is set to 0.
    length = 0
    i = len(s) - 1
    # enter a while loop that continues until we reach the beginning of the string (i >= 0)
    # or we encounter a space character (s[i] != ' ').
    while i >= 0 and s[i] != ' ': # remmeber its ' ' and not '' 
        #increment length by 1 for each non-space character encountered.
        length += 1
        # decrement i by 1 to move to the previous character in the string.
        i -= 1
    return length

s = 'Hello there Mr!'
s1 = "Hello there Mr!"
s2 = "Hello World"
output = length_of_last_word(s1)
print(output)

'''
The function length_of_last_word takes a string s as input and returns the length of the last word in the string.

We use the rstrip() function to remove any trailing spaces from the string s. This step ensures that we don't count any spaces after the last word.

We initialize a variable length to keep track of the length of the last word. Initially, it is set to 0.

We initialize a variable i to the index of the last character in the string (len(s) - 1).

We enter a while loop that continues until we reach the beginning of the string (i >= 0) or we encounter a space character (s[i] != ' ').

Inside the loop, we increment length by 1 for each non-space character encountered.

We decrement i by 1 to move to the previous character in the string.

After the loop ends, we return the value of length, which represents the length of the last word in the string.
'''

'''
The time complexity of this solution is O(n), where n is the length of the string s. We iterate through the string once, either from the end until we find a non-space character or until we reach the beginning of the string.

The space complexity is O(1) because we are not using any additional data structures.
'''

########## EDGE cases

'''
Edge cases to consider:

If the string s is empty, the function will return 0 as there are no words to count.
If the string s consists of only spaces, the function will return 0 as there are no words to count.
If the string s ends with spaces, the function will ignore those spaces and return the length of the last word.
If the string s contains only one word without any spaces, the function will return the length of that word.
'''