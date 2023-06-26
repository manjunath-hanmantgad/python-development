def longest_palindrome(s):
    char_count = {}
    length = 0
    odd_count = 0
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for count in char_count.values():
        if count % 2 ==0:
            length += count
        else:
            length += count - 1
            odd_count = 1
    return length + odd_count 


input = 'abbcbbaacdd'
ip_2 = 'abccccdd'
ip_3 = 'aabb'
output = longest_palindrome(ip_3)
print(output)


'''
The function longest_palindrome takes a string s as input and returns the length of the longest palindrome that can be formed using the characters in the string.

We initialize an empty dictionary char_count to store the count of each character in the string.

We initialize the variables length and odd_count to 0. length will store the length of the longest palindrome, and odd_count will keep track of whether there is an odd count of characters.

We iterate through each character char in the string s using a for loop.

Inside the loop, we check if the character char is already present in the char_count dictionary. If it is, we increment its count by 1. If it is not present, we add it to the dictionary with an initial count of 1.

After counting the occurrences of each character in the string, we iterate through the values of the char_count dictionary using another for loop.

For each count, we check if it is an even number by using the modulo operator %. If the count is even, we add it to the length variable.

If the count is odd, we subtract 1 from it and add it to the length variable. Additionally, we set odd_count to 1 to indicate that there is at least one character with an odd count.

Finally, we return the sum of length and odd_count, which represents the length of the longest palindrome that can be built using the characters in the string.

'''



'''
The time complexity of this solution is O(N), where N is the length of the string s. We iterate through the string twice: once to count the occurrences of each character and then to calculate the length of the longest palindrome.

The space complexity is O(K), where K is the number of unique characters in the string s. We store the counts of each character in the char_count dictionary. In the worst case, where all characters are unique, K will be equal to N. However, if the string contains a limited set of characters, the space complexity can be considered O(1).

'''


################################################

## EDGE CASES ####

###########################################

'''


If the input string is empty, the function will return 0 since there are no characters to form a palindrome.
If the input string contains only a single character, the function will return 1 since that character can form a palindrome of length 1.
If the input string contains all the same characters (e.g., "aaa" or "BBBB"), the function will return the length of the string since all characters can be used to form a palindrome.
If the input string contains a mix of uppercase and lowercase characters, the function treats them as distinct characters. If case-insensitive comparison is required, you can convert the string to lowercase or uppercase before processing it.
'''