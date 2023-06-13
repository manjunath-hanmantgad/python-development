def palindrome(s):
    s = s.replace(" ", "").lower()
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

s = input("enter : ")
result = palindrome(s)
print(result)

'''
Let's go through the code line by line:

    The is_palindrome function takes a string s as input.

    The line s = s.replace(" ", "").lower() removes any whitespace from the string using the replace() method and converts it to lowercase using the lower() method. This step ensures that the comparison is case-insensitive and ignores any spaces within the string.

    Two pointers, left and right, are initialized. left points to the first character of the string, and right points to the last character.

    Using a while loop, the code compares the characters at the corresponding positions from both ends of the string. If the characters are not equal, it means the string is not a palindrome, and the function returns False.

    The pointers left and right are incremented and decremented, respectively, to move towards the center of the string.

    If the while loop completes without finding any unequal characters, it means the string is a palindrome, and the function returns True.

Efficiency and Edge Cases:

    The code has a time complexity of O(n), where n is the length of the string. It only requires a single pass through half of the string to check for palindromic properties.
    The code removes whitespace and converts the string to lowercase before comparison, making it case-insensitive and ignoring any spaces within the string.
    Edge cases to consider:
        The code handles both even and odd-length palindromes.
        It ignores whitespace and treats the input as a single string.
        If the input is an empty string, it will be considered a palindrome.
        Non-alphabetic characters are also considered in the palindrome check.
'''