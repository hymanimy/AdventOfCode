with open('AOC10.txt') as f:
    lines = f.read().splitlines()

def find_closing_bracket(s,i):
    # returns the of closing bracket to an opening bracket 
    # if there is no closing bracket, return -1
    j=1
    opening = ['[', '(', '<', '{']
    closing = [']', ')', '>', '}']
    while j > 0:
        i+=1
        if i >= len(s):
            return -1
        if s[i] in opening: 
            j+=1
        else: 
            j-=1
    return s[i]

def matching(bracket1, bracket2):
    # checks if an opening bracket and closing bracket are the same type
    opening = ['[', '(', '<', '{']
    closing = [']', ')', '>', '}']
    return opening.index(bracket1) == closing.index(bracket2)

def corrupted_line(s):
    # returns the closing bracket of a corrupted chunk or returns -1
    opening = ['[', '(', '<', '{']
    for i, char in enumerate(s):

        # ignore closing brackets 
        if char not in opening:
            continue
        closing_bracket = find_closing_bracket(line, i)
        if closing_bracket == -1:
            # ignore the case where a chunk doesnt finish
            continue
        if not matching(char, closing_bracket):
            return closing_bracket
    
    return -1

illegal_characters = []
incomplete_lines   = [] 
for line in lines:
    c = corrupted_line(line)
    if c != -1: 
        illegal_characters.append(c)
    else:
        incomplete_lines.append(line)


points = {')': 3, ']': 57, '}': 1197, '>': 25137}
score = sum([points[x] for x in illegal_characters])
print(score)

# task 2 
def incomplete_line(s):
    # returns the string required to add to s to make it complete
    opening = ['[', '(', '<', '{']
    closing = [']', ')', '>', '}']
    missing_characters = []
    for i, char in enumerate(s):

        # ignore closing brackets 
        if char not in opening:
            continue
        closing_bracket = find_closing_bracket(line, i)
        if closing_bracket == -1:
            expected_character = closing[opening.index(char)]
            missing_characters.append(expected_character)
    
    return missing_characters[::-1]

def complete_line(s):
    # returns an array with all the brackets required to complete a line
    opening = ['[', '(', '<', '{']
    closing = [']', ')', '>', '}']
    missing_characters = []
    for i, char in enumerate(s):
        if char not in opening:
            continue
        x = find_closing_bracket(s, i)
        if x == -1:
            # this means the bracket was never closed 
            expected_bracket = closing[opening.index(char)]
            missing_characters.append(expected_bracket)
    return missing_characters[::-1]

def autocomplete_score(s):
    score = 0
    completion_characters = complete_line(s)
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    for char in completion_characters:
        score *= 5
        score += points[char]
    return score

def find_middle(arr):
    return arr[len(arr)//2]

scores = [] 
for line in incomplete_lines:
    scores.append(autocomplete_score(line))

scores.sort()
print(find_middle(scores))




