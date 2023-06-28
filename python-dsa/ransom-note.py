## HASH MAP problem

'''
To check if a ransom note can be constructed using the letters from a magazine, we need to compare the frequencies of each character in the ransom note with the frequencies of the same characters in the magazine. If the magazine has enough occurrences of each character to satisfy the ransom note, the function will return True. Otherwise, it will return False.
'''

#import the Counter class from the collections module. The Counter class is used to count the occurrences of elements in a list or a string.
from collections import Counter

#can_construct function takes two strings, ransomNote and magazine

def can_construct(ransomNote,magazine):
    #create a Counter object called ransom_counts for the ransomNote string. 
    ransom_counts = Counter(ransomNote)
    #create another Counter object called magazine_counts for the magazine string.
    magazine_counts = Counter(magazine)
    # iterate through the characters and their counts in ransom_counts using the items() method.
    for char,count in ransom_counts.items():
        #check if the count of the current character in magazine_counts is less 
        # than the count of the same character in ransom_counts
        if magazine_counts[char] < count:
            # If it is, it means the magazine does not have enough occurrences 
            # of that character to satisfy the ransom note, 
            # so we return False.
            return False
    #If we reach the end of the loop without returning False, 
    # it means the magazine has enough occurrences of each character 
    # to satisfy the ransom note, so we return True.
    return True


'''
We import the Counter class from the collections module. The Counter class is used to count the occurrences of elements in a list or a string.

The can_construct function takes two strings, ransomNote and magazine, as input and returns True if the ransom note can be constructed using the letters from the magazine, or False otherwise.

We create a Counter object called ransom_counts for the ransomNote string. This object counts the occurrences of each character in the ransom note.

We create another Counter object called magazine_counts for the magazine string. This object counts the occurrences of each character in the magazine.

We iterate through the characters and their counts in ransom_counts using the items() method.

Inside the loop, we check if the count of the current character in magazine_counts is less than the count of the same character in ransom_counts. If it is, it means the magazine does not have enough occurrences of that character to satisfy the ransom note, so we return False.

If we reach the end of the loop without returning False, it means the magazine has enough occurrences of each character to satisfy the ransom note, so we return True.
'''

'''
The time complexity of this solution is O(n + m), where n and m are the lengths of the ransom note and the magazine, respectively. This is because we iterate through both strings once to create the Counter objects.
'''

##### EDGE cases

'''
Edge cases to consider:

If either the ransom note or the magazine is an empty string, the function will return True. This is because an empty ransom note can always be constructed since it contains no characters.
If the ransom note contains a character that is not present in the magazine, the function will return False. This is because we cannot construct the ransom note using characters that are not available in the magazine.
'''

ransomNote = "aabb"
magazine = "aabbcdef"
output = can_construct(ransomNote, magazine)
print(output)