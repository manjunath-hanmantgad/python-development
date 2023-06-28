def is_subsequence(s,t):
    i,j =0,0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
        
s = 'abcd'
t = 'axbucd'
output = is_subsequence(s,t)
print(output)

'''
The function is_subsequence takes two strings, s and t, as input and returns True if s is a subsequence of t, or False otherwise.

We initialize two variables, i and j, to keep track of the current indices in s and t respectively.

We enter a while loop that continues until we reach the end of either s or t.

Inside the loop, we check if the current characters at indices i and j in s and t respectively are the same. If they are, it means we have found a match, so we increment i to move to the next character in s.

We always increment j to move to the next character in t, regardless of whether there is a match or not.

After the loop ends, we check if we have reached the end of s (i.e., i is equal to the length of s). If we have, it means all characters in s have been found in t, and we return True. Otherwise, we return False.
'''

'''
The time complexity of this solution is O(len(s) + len(t)), where len(s) and len(t) are the lengths of strings s and t respectively. We iterate through both strings once.

The space complexity is O(1) because we are not using any additional data structures.
'''

#########################

## EDGE Cases

#######################

'''
If string s is an empty string, the function will always return True since an empty string is a subsequence of any string (including an empty string).
If string t is an empty string and s is not empty, the function will always return False since s cannot be a subsequence of an empty string.
If string s and string t are both empty strings, the function will return True since an empty string is a subsequence of another empty string.
'''