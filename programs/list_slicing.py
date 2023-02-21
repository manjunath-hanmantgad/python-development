# specify first and last elements

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:3])

# want 2,3,4

print(players[1:4])

# want to start from 2nd index

print(players[2:])

# last 3 players
print(players[-3:])
print(players[:-1])
print(players[-1:])

# looping through slice 

for p in players[:3]:
    print(p.title())