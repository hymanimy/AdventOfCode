with open("AOC02.txt") as f:
    directions = list(map(lambda s : (s.split()[0], int(s.split()[1])), f.read().splitlines()))

# task 1 
horizontal = 0
depth = 0 
for direction, n in directions:
    if direction == "forward":
        horizontal += n 
    elif direction == "down":
        depth += n 
    else:
        depth -= n 
    
print(horizontal, depth, horizontal*depth)

# task 2
horizontal = 0
depth = 0 
aim = 0 
for direction, n in directions:
    if direction == "forward":
        horizontal += n 
        depth += aim * n
    elif direction == "down":
        aim += n 
    else:
        aim -= n 

print(horizontal, depth, horizontal*depth)