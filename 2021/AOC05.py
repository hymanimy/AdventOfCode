import re
with open('AOC05.txt') as f: 
    s = re.sub(' -> ', ',', f.read())
    coords = s.splitlines()

is_straight_line = lambda arr : arr[0] == arr[2] or arr[1] == arr[3]
straight_lines = list(filter(is_straight_line, map(lambda x : list(map(int, x.split(','))), coords)))

def generate_points(line):
    minx = min(line[0], line[2])
    maxx = max(line[0], line[2])
    miny = min(line[1], line[3])
    maxy = max(line[1], line[3])
    if minx == maxx or miny == maxy:
        return set((x, y) for x in range(minx, maxx+1) for y in range(miny, maxy+1))
    else:
        # diagonal line
        xdir = 1 if line[0] < line[2] else -1 
        ydir = 1 if line[1] < line[3] else -1 
        return set((line[0] + i*xdir, line[1] + i*ydir) for i in range(maxx - minx + 1))

def get_intersections(line1, line2):
    return generate_points(line1).intersection(generate_points(line2))

intersections = set()
for i in range(len(straight_lines)):
    for j in range(i+1, len(straight_lines)):
        line1, line2 = straight_lines[i], straight_lines[j]
        intersections = intersections.union(get_intersections(line1, line2))

print(len(intersections))

lines = list(map(lambda x : list(map(int, x.split(','))), coords))

intersections = set()
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        line1, line2 = lines[i], lines[j]
        intersections = intersections.union(get_intersections(line1, line2))

print(len(intersections))





