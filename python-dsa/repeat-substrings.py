def repeat_substring(s):
    n = len(s)
    #The for loop iterates from 1 to n // 2 + 1. 
    # We start from 1 because the substring should have at least one character,
    # and we end at n // 2 + 1 because a substring longer than half of s 
    # cannot be repeated to form the original string.
    for i in range(1, n // 2 +1):
       #check if n is divisible by i without any remainder.
       if n % i == 0:
           #If n is divisible by i, 
           # we extract the substring from index 0 to i-1 
           # and store it in the substr variable.
           substr = s[:i]
           #calculate the number of times the substring 
           # needs to be repeated to form a string of length n 
           # by performing integer division of n by i, 
           # and store it in the num_repeats variable.
           num_repeats = n // i
           #construct a string by repeating the substring num_repeats times 
           # and assign it to the constructed_str variable.
           constructed_str = substr * num_repeats
           # check if the constructed_str is equal to the original string s. If they match, it means s can be formed by repeating the substring, and we return True.
           if constructed_str == s:
               return True
    return False
           
            
s = 'abab'
output = repeat_substring(s)
print(output)


'''
The repeatedSubstringPattern function is defined with one parameter, s, which is the input string.

n stores the length of the string s.

The for loop iterates from 1 to n // 2 + 1. We start from 1 because the substring should have at least one character, and we end at n // 2 + 1 because a substring longer than half of s cannot be repeated to form the original string.

Inside the loop, we check if n is divisible by i without any remainder. This condition ensures that i can be the length of the repeated substring.

If n is divisible by i, we extract the substring from index 0 to i-1 and store it in the substr variable.

We calculate the number of times the substring needs to be repeated to form a string of length n by performing integer division of n by i, and store it in the num_repeats variable.

We construct a string by repeating the substring num_repeats times and assign it to the constructed_str variable.

We check if the constructed_str is equal to the original string s. If they match, it means s can be formed by repeating the substring, and we return True.

If no match is found in the loop, it means s cannot be constructed by repeating a substring, and we return False.
'''

####################

'''
The code has a linear time complexity of O(n^2), where n is the length of the input string s. This is because we have a loop that iterates from 1 to n/2 and, within each iteration, we create a substring of length i and repeat it n/i times, resulting in a string of length n. Hence, the worst-case scenario is when we iterate up to n/2 and repeat the substring n/2 times, resulting in O((n/2)^2) = O(n^2) time complexity.

The code has a constant space complexity because we only use a few variables to store intermediate results, and their sizes do not depend on the input string size.
'''
#######################

## EDGE cases
######################

'''
Edge cases to consider include empty strings and strings with length 1. The code already handles these cases correctly. If the input string is empty or has a length of 1, it cannot be constructed by repeating a non-empty substring, and the code will return False.
'''
