with open('AOC07.txt') as f: 
    positions = [int(x) for x in f.read().split(',')] 

def align(arr, n):
        # aligns an array of positions to a number n 
        # returns the number of moves it requires
        return sum([abs(e - n) for e in arr])

lowest_value = float('inf')
lowest_align = -1
# note anything lower than the min or higher than the max would obviously give too big an answer
for i in range(min(positions), max(positions)):
    x = align(positions, i)
    if x < lowest_value:
        lowest_value = x
        lowest_align = i

print(f"Aligning to {lowest_align} requires this much fuel: {lowest_value}")

def new_align(arr, n):
    # same idea as before just change the fuel amount 
    # if there's n steps then there is 1 + 2 + ... + n units of fuel required 
    # i.e. just use the triangular number formula 
    triangular = lambda x : x*(x+1)//2
    return sum([triangular(abs(e - n)) for e in arr])

lowest_value = float('inf')
lowest_align = -1
# note anything lower than the min or higher than the max would obviously give too big an answer
for i in range(min(positions), max(positions)):
    x = new_align(positions, i)
    if x < lowest_value:
        lowest_value = x
        lowest_align = i

print(f"Aligning to {lowest_align} requires this much fuel: {lowest_value}")