
#######################################

### Watch this video : https://www.youtube.com/watch?v=5NdhK3tZViQ

## in hindi!

###################################

def multiply(num1,num2):
    n1 = len(num1)
    n2 = len(num2)
    #initialize the result list with zeros to hold the intermediate and final products.
    result = [0] * (n1+n2)
    #first for loop iterates through each digit of num1 from right to left, 
    # starting from the index n1 - 1 and decrementing by 1 in each iteration.
    for i in range(n1-1, -1, -1):
        #second for loop iterates through each digit of num2 from right to left, 
        # starting from the index n2 - 1 and decrementing by 1 in each iteration.
        for j in range(n2-1,-1,-1):
            #calculate the product of the corresponding digits of num1 and num2 
            # by converting them to integers using int().
            mul = int(num1[i]) * int(num2[j])
            pos1 = i + j
            pos2 = i + j + 1
            summation = mul + result[pos2]
            
            result[pos1] += summation // 10
            result[pos2] = summation % 10
        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1
        return ''.join(map(str,result[start:]))

a = '123'
b = '456'
output = multiply(a,b)
print(output)