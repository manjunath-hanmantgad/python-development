## MATH based question on STRINGS

def largest_common_dvisor(str1,str2):
    i,j = 0,0
    result = ""
    #while loop that continues until we reach the end of either str1 or str2 or until we encounter a mismatch.
    while i < len(str1) and j < len(str2):
        #compare the characters at the current indices, str1[i] and str2[j]. If they are equal, it means the characters are part of the common divisor, so we append the character to the result string.
        if str1[i] == str2[j]:
            result += str1[i]
            i += 1
            j += 1
        else:
            break
    return result


str1 = 'leetcode'
str2 = 'code'
str3 = 'leet'
str4 = 'ABC'
str5 = ''
output = largest_common_dvisor(str1,str5)
print(output)


#################################

## EDGE case

#############################

'''
Edge cases to consider:

If either str1 or str2 is an empty string, the function will return an empty string as there can be no common divisor.
If both str1 and str2 are empty strings, the function will return an empty string since there are no characters to compare.
If there is no common divisor between the strings, the function will return an empty string.
If the common divisor is the entire string, the function will return the entire string.
'''