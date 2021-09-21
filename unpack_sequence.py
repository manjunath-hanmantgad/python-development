# Unpacking a Sequence into Separate Variables

'''
You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.
'''

data = ['apple','banana','papaya','mango']

a,b,c,d = data

#print(a)
#print(b)
#print(c)
#print(d)

for i in data:
    print(i)


print('************************************')

# Unpacking Elements from Iterables of Arbitrary Length

'''
You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a “too many values to unpack” exception.
'''

record = ['harry','harry@example.com','200-000-555','100-200-300']
name,email,*phone_nos = record 

print(name)
print(email)
print(phone_nos) # so need to mention phone_nos twice as I am using * star expression here 
