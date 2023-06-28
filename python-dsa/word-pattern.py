### HASH MAP problem 

'''
We will use two hashmaps ‘charToWord’ and ‘wordToChar’ to track which character of ‘T’ maps to which word of ‘S’ and which word of ‘S’ maps to which character of ‘T’,  respectively.

 

Here is the algorithm:

We initialise two hashmaps ‘charToWord’ and ‘wordToChar’.
We scan each character-word pair
If the character is not present in ‘charToWord’ 
If the word is already present in ‘wordToChar’ 
Return “No”. Since it has been mapped with some other character before.
Else
Map the character of ‘T’ to the word of ‘S’.
Map the word of ‘S’ to the character of ‘T’.
Else
If the current word is not equal to the word that character maps to in ‘charToWord’ 
Return “No”.
Finally, return “Yes”.

'''
def word_pattern(pattern,s):
    #splits the string s into individual words using the split() method, and stores them in the words list.
    words = s.split()
    #The function first checks if the lengths of the pattern string and the list of words are equal. If they are not equal, 
    # it immediately returns False since a full match cannot be achieved.
    if len(pattern) != len(words):
        return False 
    #mapping is a dictionary that will store the mapping of characters from pattern to words.
    #mapped_words is a set that keeps track of the words already mapped to from the pattern.
    mapping = {}
    mapped_words = set()
    for i in range(len(pattern)):
        #char stores the character at the current index i from the pattern string, 
        # and word stores the word at the corresponding index from the list of words.
        char = pattern[i]
        word = words[i]
        #If char already exists in the mapping dictionary, 
        # it means that we have seen this character before
        if char in mapping:
            #If the word in the mapping dictionary mapped to by char is not equal
            # to the current word, we return False as a full match cannot be achieved.
            if mapping[char] != word:
                return False
            #If char is not present in the mapping dictionary, 
            # it means we have encountered a new character. 
            # We need to ensure that the current word is not already mapped to another 
            # character from the pattern. If it is already mapped, 
            # we return False as a full match cannot be achieved.
        else:
            if word in mapped_words:
                return False 
            #If the conditions in lines 13 and 16 are not met, 
            # it means that we can establish a valid mapping from char to word.
            # We update the mapping dictionary and the mapped_words set accordingly.
            mapping[char] = word
            mapped_words.add(word)
    return True


pattern = 'aabb'
#s = 'cow cow dog dog'
s = 'cow dog dog cow'
output = word_pattern(pattern,s)
print(output)


'''
The is_isomorphic function is defined with two parameters, s and t.

The function first checks if the lengths of the two input strings s and t are equal. If they are not equal, it immediately returns False since the strings cannot be isomorphic.

mapping is a dictionary that will store the mapping of characters from s to t.

mapped_chars is a set that keeps track of the characters already mapped to from s to t.

The for loop iterates over the indices of the characters in the strings from 0 to the length of s (or t since their lengths are assumed to be equal).

Inside the loop, char_s and char_t store the characters at the current indices i from s and t respectively.

If char_s already exists in the mapping dictionary, it means that we have seen this character before. We need to check if the mapping is consistent. If the mapping is not consistent (i.e., the character in t mapped to by char_s is not equal to char_t), we return False as the strings cannot be isomorphic.

If char_s is not present in the mapping dictionary, it means we have encountered a new character. We need to ensure that the character in t mapped to by char_s is not already mapped to another character from s. If it is already mapped, we return False as the strings cannot be isomorphic.

If the conditions in lines 11 and 14 are not met, it means that we can establish a valid mapping from char_s to char_t. We update the mapping dictionary and mapped_chars set accordingly.

After the loop completes, we have checked all characters in both strings, and there are no inconsistencies in the mapping. Hence, we can conclude that the strings are isomorphic, and we return True.
''' 

'''
The code has a linear time complexity of O(n), where n is the length of the input strings. This is because we iterate through each character in the strings once.

The code also has a constant space complexity of O(1) for the mapping and the set, as their sizes depend on the number of unique characters encountered in the strings. Since there are a finite number of characters in any practical scenario, the space complexity can be considered constant.
'''

################## EDGE case

'''

Edge cases to consider include empty strings, strings with different lengths,
and strings with duplicate characters. The code already handles the case of different lengths
by returning False. For empty strings, since they have no characters, 
they are considered isomorphic to each other. 
Duplicate characters in the same string do not affect 
the isomorphism check since we are mapping characters from one string to another.
'''