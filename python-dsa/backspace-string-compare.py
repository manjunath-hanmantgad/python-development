def backspace(s,t):
    def process_strings(string):
        processed = []
        for char in string:
            if char != '#':
                processed.append(char)
            elif processed:
                processed.pop()
        return ''.join(processed)
    return process_strings(s) == process_strings(t)

s = 'ab##'
t = 'cd##'
output = backspace(s,t)
print(output)


'''
The backspaceCompare function is defined with two parameters, s and t, which are the input strings.

The process_string function is defined to process a given string by handling the backspace characters.

The processed list is initialized to store the characters after processing.

We iterate through each character char in the input string.

If the current character char is not a backspace character (#), we append it to the processed list.

If the current character char is a backspace character and the processed list is not empty, we remove the last character from the processed list using pop().

After processing all characters in the string, we join the characters in the processed list to form a new string, representing the text after applying the backspaces.

Finally, we compare the processed strings of s and t by calling the process_string function on both and check if they are equal. If they are equal, we return True; otherwise, we return False.
'''

'''
The code efficiently handles the backspace characters by iterating through the input strings once and processing them character by character. It avoids creating intermediate strings by directly manipulating the processed list, resulting in a more efficient solution.

The time complexity of the algorithm is O(n + m), where n and m are the lengths of strings s and t, respectively. This is because we process each string separately by iterating through their characters.

The space complexity is O(n + m), as we create the processed list to store the processed characters of both strings.
'''

