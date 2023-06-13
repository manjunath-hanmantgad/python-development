inputstr = 'hello'

print(inputstr[-1::-1])
  
#----------
'''
Edge cases to consider:

    The code handles strings of any length, including empty strings.
    The code works for strings that contain any characters, including whitespace, digits, special characters, and non-ASCII characters.
    If the input is a Unicode string, the reversal will preserve the Unicode characters correctly.
    '''
    
def reverse(s):
    chars = list(s)
    
    left = 0
    right = len(chars) - 1
    
    # reverse chars in list 
    while left < right :
        chars[left],chars[right] = chars[right], chars[left]
        left +=1
        right -=1
    reverse = ''.join(chars)
    return reverse

s = input('enter : ')
result = reverse(s)
print(result)