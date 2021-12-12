with open('AOC11.txt') as f:
    lines = f.read().splitlines()
    grid  = [list(map(int, line)) for line in lines]
    flashed = [[0]*len(grid[0]) for i in range(len(grid))]

def in_bounds(r, c, arr):
    return r >= 0 and r < len(arr) and c >= 0 and c < len(arr[0])

def get_neighbours(r, c, arr):
    # returns list of tuples which are the (row, column) positions of neighbours 
    return [(r+i, c+j) for i in range(-1, 2) for j in range(-1, 2) if in_bounds(r+i, c+j, arr) and not (i==0 and j==0)]

def flash(r, c, arr, flash_arr):
    flash_arr[r][c] = 1
    ns = get_neighbours(r, c, arr)
    for i, j in ns:
        arr[i][j] += 1 # flash increments all neighbours
        if arr[i][j] > 9 and not flash_arr[i][j]:
            flash(i, j, arr, flash_arr)

def show_grid(arr):
    for line in arr:
        print(*line)
    print()

def step(arr, flash_arr):
    s = 0
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            arr[r][c] += 1
            if arr[r][c] > 9 and not flash_arr[r][c]:
                flash(r, c, arr, flash_arr)
    s = sum([sum(line) for line in flash_arr])
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] > 9: arr[r][c] = 0
            flash_arr[r][c] = 0
    return s 

def all_zeroes(arr):
    return all([x == 0 for line in arr for x in line])

total_flashes = 0
for _ in range(100):
    total_flashes += step(grid, flashed)

print(total_flashes)

with open('AOC11.txt') as f:
    lines = f.read().splitlines()
    grid  = [list(map(int, line)) for line in lines]
    flashed = [[0]*len(grid[0]) for i in range(len(grid))]

steps = 0
while not all_zeroes(grid):
    step(grid, flashed)
    steps += 1

print(steps)