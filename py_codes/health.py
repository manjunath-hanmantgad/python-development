#health = 50

# generate random number to assign to health 
import random 
health = 50
#genearte varaible to assign random int value between 25 and 50
potion_health = random.randint(25, 50)

# add potion_health to health 
health = health + potion_health

#print(health) # print new_health 

difficulty = 1 # 1 = easy , 2 = medium , 3 = difficult
difficulty = random.randint(1,3)

# as difficulty increases health decreases 

health = health / difficulty 

print(health)


