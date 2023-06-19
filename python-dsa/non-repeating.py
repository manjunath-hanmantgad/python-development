def non_repeating(s):
    count = {}
    
    for char in s:
        if char in count:
            count[char] +=1
        else:
            count[char] = 1
    for char in s:
        if count[char] == 1:
            return 
    return '$'

s = 'abcdefgh'
print(non_repeating(s))