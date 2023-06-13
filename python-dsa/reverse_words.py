'''
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
'''


s = 'i.like.this.program.very.much'

words = s.split('.')
string = []
for word in words:
    string.insert(0, word)
    
    
print(" ".join(string))


# ----------

def reverse(string):
    words = string.split('.')
    left = 0
    right = len(words) - 1
    
    while left < right:
        words[left], words[right] = words[right], words[left]
        left =+1
        right -=1
    return '.'.join(words)

#string = 'i.am.very.ok.with.this.learning'

words = 'i.am.very.ok.with.this.learning'
reverse = reverse(words)
print(reverse)


'''
    Time Complexity:
        Splitting the string into words using the split function has a time complexity of O(n), where n is the length of the input string.
        Reversing the list of words using [::-1] has a time complexity of O(n).
        Joining the reversed words back into a string using join has a time complexity of O(n).
        Overall, the time complexity of the solution is O(n).

    Space Complexity:
        The solution utilizes additional space to store the list of words and the reversed words, both of which have a space complexity of O(n), where n is the number of words in the sentence.
        The reversed sentence also requires O(n) space.
        Therefore, the space complexity of the solution is O(n).

Considering the simplicity of the algorithm and the linear time and space complexity, this solution is considered efficient for reversing a string without reversing its individual words.
'''

def reverse_string(sentence):
    words = sentence.split('.')
    reversed_words = words[::-1]
    reversed_sentence = '.'.join(reversed_words)
    return reversed_sentence

sentence = "Hello.world.This.is.a.test"
reversed_sentence = reverse_string(sentence)
print(reversed_sentence)
