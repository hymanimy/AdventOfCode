with open('AOC06.txt') as f: 
    fish = list(map(int, f.read().split(',')))

def next_day(fish):
    new_fish = []
    for i in range(len(fish)):
        fish[i] -= 1
        if fish[i] == -1:
            fish[i] = 6 
            new_fish.append(8)
    return fish + new_fish

for _ in range(80):
    fish = next_day(fish)

print(len(fish))

# it would take too much memory to have an array of all the fish 
# instead have an array of length of all possible ages 
# where we have the values at each index as the number of fish that age 
# and update it 

with open('AOC06.txt') as f: 
    fish = list(map(int, f.read().split(',')))

fish_ages = [0] * 9 # fish_ages[age] = number_of_fish_that_age
for f in fish:
    fish_ages[f] += 1

def update_ages(ages):
    new_ages = [0] * 9 
    for i in range(1, 9):
        new_ages[i-1] = ages[i]
    new_ages[8] = ages[0]
    new_ages[6] += ages[0]
    return new_ages

for _ in range(256):
    fish_ages = update_ages(fish_ages)

print(sum(fish_ages))




