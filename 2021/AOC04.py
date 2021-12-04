# represent a ticked number with its negative equivalent

with open('AOC04.txt') as f: 
    lines = f.read().splitlines()
    nums = list(map(int, lines[0].split(','))) 
    boards = [] 
    i = 2 
    board = [] 
    while i < len(lines):
        if lines[i] == '':
            boards.append(board) # end of board, add to boards array and start new board 
            board = [] 
        else:
            board.append(lines[i]) # 
        i += 1
    boards.append(board)

def format_board(b):
    return list(map(int, " ".join(b).split()))

def get(r, c, board):
    # get row and column element but its actually a 1D array
    return board[r*5 + c]

def row_win_check(board):
    for c in range(5):
        flag = True
        for r in range(5):
            if get(r, c, board) >= 0:
                flag = False
                break
        if flag: 
            return True
    return False

def col_win_check(board):
    for r in range(5):
        flag = True
        for c in range(5):
            if get(r, c, board) >= 0:
                flag = False
                break
        if flag: 
            return True
    return False

def find_score(board, num):
    return num * sum([x for x in board if x > 0])


boards = list(map(format_board, boards))

for num in nums: 
    flag = False
    for board in boards: 
        if num in board:
            if num == 0:
                board[board.index(num)] = -0.1
            else:
                board[board.index(num)] = -num
        if row_win_check(board) or col_win_check(board):
            print(find_score(board, num))
            flag = True
            break
    if flag:
        break

# task 2 
# plan: for every number if it appears on a board, turn the number negative (turn 0 to -0.1). Check for a win 
# and then if it wins, add the boards index to a list of indices which need to be removed. remove at the end
# so we dont operate on a list which is being looped over. when a win is detected and list is of length 1
# we have found our final winner
boards_to_remove = []
for num in nums: 
    flag = False
    for board in boards: 
        if num in board:
            if num == 0:
                board[board.index(num)] = -0.1
            else:
                board[board.index(num)] = -num
        if row_win_check(board) or col_win_check(board):
            if len(boards) == 1:
                print(find_score(board, num))
                flag = True
                break
            else:
                boards_to_remove.append(boards.index(board))
    boards = [boards[i] for i in range(len(boards)) if i not in boards_to_remove]
    boards_to_remove = []
    if flag:
        break
            