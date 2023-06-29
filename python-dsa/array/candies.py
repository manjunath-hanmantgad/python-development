'''
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise
'''

def kidswithcandies(candies,extraCandies):
    max_candies = max(candies)
    result = []
    
    for c in candies:
        result.append(c + extraCandies >= max_candies)
    return result

candies = [1,2,3,4]
extraCandies = 2
output = kidswithcandies(candies,extraCandies)
print(output)


'''
The function kidsWithCandies takes two parameters: candies (an integer array representing the number of candies each kid has) and extraCandies (the number of extra candies you have).

We start by finding the maximum number of candies among all the kids using the max() function and store it in the variable max_candies.

We create an empty list called result to store the boolean values indicating whether each kid can have the greatest number of candies after receiving the extra candies.

Next, we iterate through each candy_count in the candies array.

For each candy_count, we check if adding extraCandies to it would make it greater than or equal to max_candies. If it is, we append True to the result list; otherwise, we append False.

Finally, we return the result list containing the boolean values indicating whether each kid can have the greatest number of candies after receiving the extra candies.
'''

'''
The solution has a time complexity of O(n), where n is the number of kids. This is because we need to iterate through the candies array once to compare each candy count with the maximum number of candies. Finding the maximum value takes O(n) time, and the subsequent iteration through the array also takes O(n) time. Therefore, the overall time complexity is linear.
'''

############# EDGE case

'''
Empty candies array: If the candies array is empty, the function will return an empty result list since there are no kids to consider.
Large input size: The solution can handle large input sizes efficiently due to its linear time complexity. However, very large values in the candies array or extraCandies could potentially cause overflow issues, depending on the programming language and platform used.
'''