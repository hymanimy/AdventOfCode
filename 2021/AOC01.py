# Data wrangle 
with open("AOC01.txt") as f: 
    nums = list(map(int, f.read().splitlines()))

# Task 1 
increased = 0 
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        increased += 1

print(increased)

# Task 2 
increased = 0 
for i in range(1, len(nums)-2):
    if nums[i] + nums[i+1] + nums[i+2] > nums[i-1] + nums[i] + nums[i+1]:
        increased += 1

print(increased)