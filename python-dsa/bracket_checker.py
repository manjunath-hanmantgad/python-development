'''
Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.
'''

def bracket_balanced(s):
    stack = []
    for char in s:
        if char in ('(','{','['):
            stack.append(char)
        else:
            if stack and ((stack[-1]=='(' and char == ')') or
                          (stack[-1]=='{' and char == '}') or
                          (stack[-1]=='[' and char == ']')):
                stack.pop()
            else:
                return False
    return not stack

#expression = "{[{{))"
#expression = "({})[]"
expression = "{}()[(){}]"

# call function

if bracket_balanced(expression):
    print('balanced')
else:
    print("Not balanced")
