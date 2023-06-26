def longest_common_prefix(strings):
        if not strings:
            return ""
        prefix = strings[0]
        for s in strings[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
    
        """
  Finds the longest common prefix among all strings present in the given array.

  Args:
    strings: An array of strings.

  Returns:
    The longest common prefix of all strings present in the given array.
    """

strings = ["geeksforgeeks", "geeks", "geek", "geezer"]
print(longest_common_prefix(strings))

'''
The longest_common_prefix() function works by first checking if the array of strings is empty. If it is, then the function returns an empty string. Otherwise, the function starts by setting the prefix to the first string in the array. Then, the function iterates through the remaining strings in the array. For each string, the function checks if it starts with the current prefix. If it does not, then the function shortens the prefix by one character. The function continues this process until the prefix is no longer shorter. The function then returns the prefix.
'''

'''
The function longest_common_prefix takes an array of strings (strs) as input and returns the longest common prefix among all the strings.

The first conditional statement checks if the input array is empty. If it is, it means there are no strings, and hence, the function returns an empty string.

We initialize the variable min_length to store the length of the shortest string in the array. This will be useful for iteration and comparison purposes.

The variable prefix is initialized as an empty string to store the common prefix characters.

We use a for loop to iterate through the characters at each index from 0 to min_length - 1. This ensures that we only check up to the length of the shortest string.

Inside the loop, we get the character at the current index (i) from the first string (strs[0]) and store it in the variable char. We compare this character with the corresponding character at index i in all other strings using a nested for loop and the all function.

If all the characters at index i in all strings are equal, we append the character to the prefix string. This means the character is a common prefix character.

If any character is found to be different during the comparison, we break out of the loop because we have found the longest common prefix.

Finally, the function returns the prefix string, which represents the longest common prefix among all strings in the array.

'''



'''
The time complexity of this solution is O(N * M), where N is the number of strings in the array and M is the length of the shortest string. We iterate through each character in the shortest string and compare it with the corresponding character in all other strings.

The space complexity is O(M) because we store the common prefix characters in the prefix string. The space required is proportional to the length of the shortest string.
'''

############################

## Edge Cases 

###############################

'''
If the input array is empty, the function returns an empty string since there are no strings to compare.
If the input array contains an empty string, the function will return an empty string as the common prefix because there are no characters to compare.
If the input array contains only one string, the function will return the entire string as the common prefix since there are no other strings to compare with.
'''
