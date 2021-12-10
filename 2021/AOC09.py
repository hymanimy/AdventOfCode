with open('AOC09.txt') as f:
    heights = [list(map(int, line)) for line in  f.read().splitlines()]

def in_bounds(r, c, arr):
    return r >= 0 and r < len(arr) and c >= 0 and c < len(arr[0])

def get_neighbours(r, c, arr):
    return [(r+i,c+j) for (i, j) in [(1,0), (-1,0), (0,-1), (0,1)] if in_bounds(r+i, c+j, arr)]
    # return [arr[r+i][c+j] for i in range(-1, 2) for j in range(-1, 2) if in_bounds(r+i, c+j, arr) and (i != 0 or j != 0)]

def is_lowpoint(r, c, arr):
    neighbours = get_neighbours(r, c, arr)
    return all([arr[r][c] < arr[i][j] for i, j in neighbours])

risk_sum = 0
low_points = []
for r in range(len(heights)):
    for c in range(len(heights[0])):
        if is_lowpoint(r, c, heights):
            low_points.append((r, c))
            risk_sum += heights[r][c] + 1

print(f'The risk sum of all the low points is {risk_sum}')

def basin(r, c, arr):
    # returns the size of the basin corresponding to arr[r][c]
    # should be depth first search
    
    visited = []
    stack = [(r, c)] # tracks what we have to explore
    while len(stack) > 0:
        cur = stack.pop()
        if cur not in visited: 
            visited.append(cur)
            for neighbour in get_neighbours(cur[0], cur[1], arr):
                if arr[neighbour[0]][neighbour[1]] != 9: # we dont wanna consider 9's
                    stack.append(neighbour)
    return len(visited)

basin_sizes = []
for r, c in low_points:
    basin_sizes.append(basin(r, c, heights))

basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])


