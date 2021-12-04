with open("AOC03.txt") as f:
    nums =  f.read().splitlines()

gamma_rate = ""
num_length = len(nums[0])
for position in range(num_length):
    zero_count = 0
    for num in nums:
        b = num[position]
        if b == '0': 
            zero_count += 1
    if zero_count > len(nums) - zero_count:
        gamma_rate += '0'
    else:
        gamma_rate += '1'

flip = lambda x : '0' if x == '1' else '1'
epsilon_rate = "".join([flip(x) for x in gamma_rate])

print(int(gamma_rate, 2) *  int(epsilon_rate, 2))

def oxygen_rating(arr, position):
    
    if len(arr) == 1:
        return arr
    
    zero_count = 0
    for elem in arr:
        b = elem[position]
        if b == '0': zero_count += 1
    if zero_count > len(arr) - zero_count: # more 0's than 1's 
        return [elem for elem in arr if elem[position] == '0']
    else:
        return [elem for elem in arr if elem[position] == '1']

def c02_rating(arr, position):
    
    if len(arr) == 1:
        return arr
    
    zero_count = 0
    for elem in arr:
        b = elem[position]
        if b == '0': zero_count += 1
    if zero_count <= len(arr) - zero_count: # less 0's than 1's 
        return [elem for elem in arr if elem[position] == '0']
    else:
        return [elem for elem in arr if elem[position] == '1']


oxy_arr, c02_arr = nums[:], nums[:]
position = 0 
while len(oxy_arr) != 1 and position < len(oxy_arr[0]):
    oxy_arr = oxygen_rating(oxy_arr, position)
    position += 1

position = 0 
while len(c02_arr) != 1 and position < len(c02_arr[0]):
    c02_arr = c02_rating(c02_arr, position)
    position += 1

print(int(oxy_arr[0], 2) * int(c02_arr[0], 2))







    



