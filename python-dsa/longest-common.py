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
        