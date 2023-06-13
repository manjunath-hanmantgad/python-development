'''
Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other.
'''

def anagrams(a,b):
    if len(a) != len(b):
        return False 

# dict to store the character counts / frequencies

    char_freq_a = {}
    char_freq_b = {}

    # count frequency in strings

    for char in a:
        char_freq_a[char] = char_freq_a.get(char, 0) + 1
    for char in b:
        char_freq_b[char] = char_freq_b.get(char, 0) + 1
        
    return char_freq_a == char_freq_b

a = input('enter : ')
b = input('enter : ')
result = anagrams(a,b)
print(f" are {a} and {b} anagrams ? {result}")


'''
Edge cases to consider:

    Strings of different lengths cannot be anagrams, so the solution handles this case by returning False early.
    The solution is case-sensitive, meaning that different cases of letters are considered different characters. For case-insensitive comparison, you can convert both strings to lowercase or uppercase before processing.
    The solution assumes that the input consists only of lowercase characters. If the input can contain uppercase characters, digits, or special characters, you may need to modify the solution accordingly.
'''