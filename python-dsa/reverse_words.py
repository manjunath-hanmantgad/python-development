'''
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
'''


s = 'i.like.this.program.very.much'

words = s.split('.')
string = []
for word in words:
    string.insert(0, word)
    
    
print(" ".join(string))