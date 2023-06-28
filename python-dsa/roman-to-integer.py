def roman_to_integer(roman):
    #create a dictionary, roman_values, to map each Roman numeral symbol to its corresponding integer value.
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total= 0
    #initialize a variable prev_value to keep track of the value of the previous Roman numeral character. It is initially set to 0.
    prev_value = 0
    
    #terate through the characters of the Roman numeral string s in reverse order
    # using a for loop.
    for i in range(len(roman) - 1, -1, -1):
        #retrieve the integer value of the current Roman numeral character 
        # using the roman_values dictionary.
        curr_value = roman_values[roman[i]]
        #compare the current value with the previous value. 
        # If the current value is less than the previous value, 
        # it means we need to subtract the current value from the total. 
        # This indicates a case like "IV" where "I" (1) is subtracted from "V" (5).
        if curr_value < prev_value:
            total -= curr_value
        #If the current value is greater than or equal to the previous value, 
        # we add the current value to the total.
        # This covers cases like "VI" where "V" (5) is added to "I" (1).
        else:
            total += curr_value
        # update the prev_value to the current value for the next iteration.
        prev_value = curr_value
    return total

roman = 'XIVI'
ro = 'XLIX'
output = roman_to_integer(ro)
print(output)
        
        
'''
The function roman_to_integer takes a Roman numeral string, s, as input and returns its corresponding integer value.

We create a dictionary roman_values that maps each Roman numeral character to its corresponding integer value.

We initialize a variable total to keep track of the running sum of integer values.

We also initialize a variable prev_value to keep track of the value of the previous Roman numeral character. It is initially set to 0.

We iterate through the characters of the Roman numeral string s in reverse order using a for loop.

Inside the loop, we retrieve the integer value of the current Roman numeral character using the roman_values dictionary.

We compare the current value with the previous value. If the current value is less than the previous value, it means we need to subtract the current value from the total. This indicates a case like "IV" where "I" (1) is subtracted from "V" (5).

If the current value is greater than or equal to the previous value, we add the current value to the total. This covers cases like "VI" where "V" (5) is added to "I" (1).

We update the prev_value to the current value for the next iteration.

After iterating through all the characters, we return the final total as the integer representation of the Roman numeral.

'''

'''
The time complexity of this solution is O(n), where n is the length of the Roman numeral string s. We iterate through each character once.

The space complexity is O(1) because we are using a fixed-size dictionary to store the Roman numeral values and a constant amount of additional variables
'''

################ EDGE Cases

'''
If the input Roman numeral is an empty string, the function will return 0 as the corresponding integer value.
If the input Roman numeral contains invalid characters, the function may produce incorrect results. However, in this implementation, we assume the input Roman numeral is valid and consists only of the characters 'I', 'V', 'X', 'L', 'C', 'D', and 'M'.
The function handles cases where a smaller value appears before a larger value to indicate subtraction. For example, "IV" is correctly interpreted as 4, "IX" as 9, "XL" as 40, and so on.
'''