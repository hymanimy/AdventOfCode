with open('AOC08.txt') as f:
    lines = f.read().splitlines()
    digits = [line.split('|')[0].split() for line in lines]
    outputs = [line.split('|')[1].split() for line in lines]

wires_for_digit = [
    'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 
    'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'
]

number_of_wires = [len(s) for s in wires_for_digit]

# task 1 
count = 0
uniques = [2, 4, 3, 7] # 1 4 7 8 
for output in outputs:
    for string in output:
        if len(string) in uniques:
            count += 1

print(count)

# task 2 

def print_possibilities(arr):
    wires_for_digit = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    for digit in arr:
        options = [(i, s) for i, s in enumerate(wires_for_digit) if len(s) == len(digit)]
        print(f'{"".join(sorted(digit))} can be {options}')

def use_easy_clues(digits):
    # this is only going to consider the easy clues to narrow the search
    all_segments = set('abcdefg') # set containing letters a through g 
    options = {k:all_segments for k in all_segments} # key is wire and it has a set of possible segments it can map to
    wires_for_digit = [set('abcefg'), set('cf'), set('acdeg'), set('acdfg'), set('bcdf'), set('abdfg'), set('abdefg'), set('acf'), set('abcdefg'), set('abcdfg')]
    unique_digits = [1, 4, 7, 8] # digits which have a unique number of segments 
    uniques       = [2, 4, 3, 7] # parallel array
    for digit in digits:
        if len(digit) in uniques:
            # Find the associated number it will be 
            num = unique_digits[uniques.index(len(digit))]
            for char in digit:
                options[char] = options[char].intersection(wires_for_digit[num])
    return options

def remove_impossible_options(options):
    # if there are n wires which have n of the same options, then nothing else can have those options
    for i in range(1, 8):
        sets_of_length_i = [v for v in options.values() if len(v) == i]
        for s in sets_of_length_i:
            occurences = len([1 for v in options.values() if s == v]) # how many times does this set occur (shouldnt be more than i)
            if occurences > i: print('error!!!')
            if occurences == i: 
                # remove all elements of this set from every other set 
                for k in options:
                    if options[k] != s:
                        options[k] = options[k].difference(s)
    return options

def one_fell_swoop(nums):
    ops = use_easy_clues(nums)
    ops_copy = dict(ops)
    while ops_copy != remove_impossible_options(ops):
        ops_copy = dict(ops)
    return ops

def find_final_clue(digits, options):
    # there is only one 5 segment signal which has has bd in it (it is abdfg which is 5) say its LMNOP
    # if we have a pair of wires which map to bd, then we can use this to deduce further clues
    # find bd pair
    bd_pair = {k for k in options if options[k] == {'b', 'd'}}
    # 5 segment signal which has the wires which map to bd in it 
    bd_pair_signal = set() # LMNOP
    pair1, pair2 = bd_pair
    for digit in digits:
        if len(digit) == 5 and pair1 in digit and pair2 in digit:
            bd_pair_signal = set(digit)
            break
    # print(bd_pair_signal)
    bd_pair_signal.difference_update(bd_pair)
    bd_pair_signal_maps_to = {'a', 'f', 'g'}
    # print(f'{bd_pair_signal} maps to {bd_pair_signal_maps_to}')
    # print(bd_pair_signal)
    for x in bd_pair_signal:
        options[x] = options[x].intersection({'a', 'f', 'g'})

    remove_impossible_options(options)

    # there is one 6 segment signal which doesnt include d (0, 'abcefg')
    # find which signal maps to abcefg and doesnt include one of the bd pair 
    # this will imply that the one remaining maps to b and that the one missing maps to d
    for digit in digits:
        if len(digit) == 6 and (pair1 not in digit or pair2 not in digit):
            # print(digit)
            if pair1 in digit: 
                # print(f'{pair1} maps to b')
                options[pair1] = {'b'}
                options[pair2] = {'d'}
            else: 
                # print(f'{pair2} maps to b')
                options[pair2] = {'b'}
                options[pair1] = {'d'}

def decode(options, outs):
    answers = {k: next(iter(options[k])) for k in options}
    number = ''
    wires_for_digit = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    signal_to_number = {w: i for i, w in enumerate(wires_for_digit)}
    for out in outs:
        translated_signal = ''.join(sorted([answers[k] for k in out]))
        # print(f'{out} becomes {translated_signal} which is the digit {signal_to_number[translated_signal]}')
        number += str(signal_to_number[translated_signal])
    return int(number)

def find_digits(digits, outputs):
    ops = one_fell_swoop(digits)
    find_final_clue(digits, ops)
    s = decode(ops, outputs)
    return s

s = 0
for i in range(len(digits)):
    s += find_digits(digits[i], outputs[i])

print(s)








# ['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb']
# 'be' corresponds to 'cf' (b is c or f and e is c or f) (can use a dictionary to represent these options i.e. {b:cf, e:cf}
# 'cfbegad' corresponds 'abcdefg' but {c:abcdefg, f:abcdefg, b:} TELLS US NOTHING 
# cgeb -> bcdf {c: bcdf, g: bcdf, e: cf, b: cf}
# edb -> acf {e: cf, d: }










