squares = [value **2 for value in range(1,10)]
print(squares)

numbers = [x for x in range(1,21)]
print(numbers)

one_million = list(range(1,1000000)) # 10 lacs = 1 mil
#print(one_million)
maxi = max(one_million)
mini = min(one_million)
addi = maxi + mini
#print(addi)
odd = [o for o in range(1,20,2)]
print(odd)

mul_3 = [m for m in range(3,30,3)]
print(mul_3)

cubes = [value **3 for value in range(1,11)]
print(cubes)