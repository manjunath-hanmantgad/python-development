## TWO POINTERS

def merged_strings(word1,word2):
    merged = ''
    length1,length2 = len(word1),len(word2)
    #determine the maximum length between the two strings using the max function and store it in the variable max_length
    max_length = max(length1,length2)
    # use for loop to iterate through max_length - 1
    for i in range(max_length):
        #check if the current index i is less than the length of word1
        if i < length1:
            #If it is, we append the character at index i from word1 to the merged string.
            merged += word1[i]
        if i < length2:
            merged += word2[i]
    # the function returns the merged string, which contains the merged result.
    return merged

word1 = 'hello'       
word2 = 'HELLO'
output = merged_strings(word1,word2)
print(output)


'''
The function merge_strings takes two strings word1 and word2 as input and returns the merged string.

We initialize an empty string merged to store the merged result.

We calculate the lengths of word1 and word2 and store them in variables length1 and length2 respectively.

We determine the maximum length between the two strings using the max function and store it in the variable max_length. This will be useful for iteration.

We use a for loop to iterate from 0 to max_length - 1.

Inside the loop, we check if the current index i is less than the length of word1. If it is, we append the character at index i from word1 to the merged string.

Similarly, we check if the current index i is less than the length of word2. If it is, we append the character at index i from word2 to the merged string.

Finally, the function returns the merged string, which contains the merged result.
'''

'''
The time complexity of this solution is O(N), where N is the maximum length between word1 and word2. We iterate through the characters of both strings up to the maximum length, which ensures that we cover all characters.

The space complexity is O(N) as well. We store the merged result in the merged string, which can have a maximum length of N.
'''

##################################

## EDGE CASE

####################################

'''
Edge cases to consider:

If either word1 or word2 is an empty string, the function will return the non-empty string as the merged result.
If both word1 and word2 are empty strings, the function will return an empty string since there are no characters to merge.
If the lengths of word1 and word2 are equal, the function will merge the strings by alternating characters until all characters are exhausted from both strings.
If one string is longer than the other, the additional characters from the longer string will be appended to the end of the merged string.
'''