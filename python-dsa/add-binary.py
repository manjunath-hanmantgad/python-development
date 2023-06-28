def add_binary(a,b):
    result = []
    carry = 0
    #i and j are initialized to the last indices of a and b respectively.
    i = len(a) - 1
    j = len(b) -1 
    #while loop continues until we process all digits in both strings a and b, 
    # and there is no remaining carry.
    while i >=0 or j >=0 or carry !=0: # its or and not 'and'
        #sum_val is initialized with the current carry value.
        sum_val = carry
        #If i is greater than or equal to 0, 
        # we add the integer value of a[i] (0 or 1) to the sum_val and decrement i by 1.
        if i >=0:
            sum_val += int(a[i])
            i -= 1
        #If j is greater than or equal to 0, we add the integer value of b[j] (0 or 1) 
        # to the sum_val and decrement j by 1.
        if j >=0:
            sum_val += int(b[j])
            j -= 1
        #We calculate the binary digit to be added to the result by taking the modulo 2 
        # of sum_val and converting it to a string. 
        # This ensures that the digit is either 0 or 1.
        result.append(str(sum_val % 2))
        #update the carry value by performing integer division of sum_val by 2, 
        # which gives either 0 or 1.
        carry = sum_val // 2
    #After the loop completes, we have processed all digits and the carry. 
    # We join the binary digits in the result list in reverse order, 
    # convert them to a string, 
    # and return the final binary sum.
    return ''.join(result[::-1])        

a = '100'
b = '001'
c = '11'
d = '1'
output = add_binary(a,b)
print(output)


'''
The addBinary function is defined with two parameters, a and b.

result is an empty list that will store the binary digits of the sum.

carry represents the carry value during addition.

i and j are initialized to the last indices of a and b respectively.

The while loop continues until we process all digits in both strings a and b, and there is no remaining carry.

sum_val is initialized with the current carry value.

If i is greater than or equal to 0, we add the integer value of a[i] (0 or 1) to the sum_val and decrement i by 1.

If j is greater than or equal to 0, we add the integer value of b[j] (0 or 1) to the sum_val and decrement j by 1.

We calculate the binary digit to be added to the result by taking the modulo 2 of sum_val and converting it to a string. This ensures that the digit is either 0 or 1.

We update the carry value by performing integer division of sum_val by 2, which gives either 0 or 1.

The binary digit is appended to the result list.

After the loop completes, we have processed all digits and the carry. We join the binary digits in the result list in reverse order, convert them to a string, and return the final binary sum.
'''

#######################

'''
The code has a linear time complexity of O(max(len(a), len(b))), where len(a) and len(b) represent the lengths of the input binary strings a and b. This is because we iterate through the digits of the longer string, performing constant-time operations.

The code has a linear space complexity of O(max(len(a), len(b))), primarily due to the result list. In the worst case, when both strings have the same length, the result list will have one extra digit than the input strings.
'''

################ EDGE cases

'''
The code can handle empty strings by returning the non-empty string as the sum. Leading zeros in the input strings will not affect the calculation, as the result will automatically have the correct number of digits. If the input strings have different lengths, the code will process the remaining digits of the longer string and include any remaining carry in the sum.
'''
