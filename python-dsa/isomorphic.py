def is_isomorphic(s,t):
    #checks if the lengths of the two input strings s and t are equal. If they are not equal, 
    # it immediately returns False since the strings cannot be isomorphic.
    if len(s) != len(t):
        return False 
    # dictionary that will store the mapping of characters from s to t.
    mapping = {} 
    #mapped_chars is a set that keeps track of the characters already mapped to from s to t.
    mapped_chars = ()
    for i in range(len(s)):
        #char_s and char_t store the characters at the current indices i from s and t 
        # respectively.
        char_s = s[i]
        char_t = t[i]
        
        #If char_s already exists in the mapping dictionary, 
        # it means that we have seen this character before. 
        # We need to check if the mapping is consistent. 
        # If the mapping is not consistent (i.e., the character in t mapped to by char_s 
        # is not equal to char_t), we return False as the strings cannot be isomorphic.
        if char_s in mapping:
            if mapping[char_s] != char_t:
                return False
        #If char_s is not present in the mapping dictionary, 
        # it means we have encountered a new character.
        # We need to ensure that the character in t mapped to by char_s 
        # is not already mapped to another character from s. If it is already mapped,
        # we return False as the strings cannot be isomorphic.
        else:
            if char_t in mapped_chars:
                return False
            #it means that we can establish a valid mapping from char_s to char_t. 
            # We update the mapping dictionary and mapped_chars set accordingly.
            mapping[char_s] = char_t
            mapped_chars.add(char_t)
    #We reached here only when all elements were successfully added into both dictionaries.
    return True

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

########### EDGE case
'''
Edge cases to consider include empty strings, strings with different lengths,
and strings with duplicate characters. The code already handles the case of different lengths
by returning False. For empty strings, since they have no characters, 
they are considered isomorphic to each other. 
Duplicate characters in the same string do not affect the isomorphism check
since we are mapping characters from one string to another.
'''