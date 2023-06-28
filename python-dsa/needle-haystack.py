def strStr(haystack,needle):
    # base condition
    if haystack is None or needle is None:
        return -1 
    # special case or when needle is empty
    if haystack == needle:
        return 0
    # length of needle 
    needlelength = len(needle)
    # loop through haystack using sliding window pattern
    for i in range(len(haystack) -needlelength +1):
        if haystack[i:i+needlelength] ==needle:
            return i
    return -1

haystack = 'leetcode'
#needle = 'leetu'
needle = 'leet'
output = strStr(haystack,needle)
print(output)


'''
The strStr function takes two parameters, haystack and needle, which represent the haystack string and the needle string, respectively. The function returns the index of the first occurrence of the needle in the haystack.

The first check is for the base condition. If either the haystack or the needle is None, it means one of the inputs is invalid, so the function returns -1.

The next check handles a special case when the haystack and the needle are equal. In this case, the needle is found at the beginning of the haystack, so the function returns 0.

The variable needlelength is assigned the length of the needle string. It will be used to control the iteration of the for loop.

The for loop iterates through the haystack using a sliding window pattern. The range is set to len(haystack) - needlelength + 1 to ensure that the sliding window stays within the bounds of the haystack.

Inside the loop, we check if the current substring of the haystack from i to i+needlelength is equal to the needle string. If it is, it means we have found a match, so the function returns the index i.

If the loop finishes without finding a match, it means the needle is not present in the haystack, so the function returns -1.
'''

'''
Time Complexity
The string is traversed once so the time complexity will be O(n).

Space Complexity
We may have to create n substrings of length 1 each, therefore, the space complexity will also be O(n).
'''