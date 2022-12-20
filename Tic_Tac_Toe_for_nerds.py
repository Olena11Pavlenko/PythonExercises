import numpy as np

def unique_players(inputs):
    s = set()
    for row in inputs:
        for i in row:
            s.add(i)
    return s

def average(matrix):
    sum_by_columns = np.sum(matrix, axis = 0)
    sum_by_rows = np.sum(matrix, axis = 1)
    sum_by_diagonal1 = np.sum(np.diagonal(matrix))
    sum_by_diagonal2 = np.sum(np.diagonal(np.fliplr(matrix)))
    num_rows = len(matrix)
    averages = list((np.max(sum_by_columns/num_rows), np.max(sum_by_rows/num_rows), sum_by_diagonal1/num_rows, sum_by_diagonal2/num_rows))
    return averages

def is_winner(game):
    if 1 in average(game):
        return True

def loop_players (inputs):
    inputs = np.array(inputs, dtype="object")
    for player in unique_players(inputs):
        inputs1 = np.where(inputs == player, 1, 0)
        if is_winner(inputs1):
            return player 
    else: return False
    
def tic_tac_toe(inputs):
    looping = loop_players(inputs)
    if looping == False:
        return "It's a Tie"
    else:
        return "Player %s win" % looping

print (tic_tac_toe([
    ["X", "X", "O", "X", "P"],
    ["O", "X", "O", "@", "X"],
    ["X", "@", "O", "O", "O"],
    ["@", "X", "O", "@", "@"],
    ["O", "X", "O", "@", "X"]
    ]))


