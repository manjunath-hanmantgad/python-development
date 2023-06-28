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