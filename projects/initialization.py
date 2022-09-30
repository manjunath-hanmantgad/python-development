import numpy as np
import time
tic = time.perf_counter()
print(tic)
n = 10000
# r = np.zeros(n)
# for i in range(n):
#     r[i] = i ** 2
# #print(r)
# print((time.perf_counter() - tic) * 1000)


r = []
for i in range(n):
    r.append(i**2)
#print(r)
print((time.perf_counter() - tic) * 1000)



'''
r = np.zeros((4, 5)) # 4x5 matrix
# print(r)
r[1,2] = 7 # make 1st row , 2nd column value = 7 
print(r)
'''
