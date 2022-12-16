#1) Create a function that takes a list of character inputs from a Tic Tac Toe game. 
# Inputs will be taken from player1 as "X", player2 as "O", and empty spaces as "#". 
# The program will return the winner or tie results.
#2) generalize the task to any matrix size (3+). I.e. you need to find if any player has full row/column/diagonal
#3) generalize the task to any symbol, i.e. there could be players A - B, X - O, S - K. And result should say "Player S won"

import numpy as np
def tic_tac_toe(inputs):
    num = 1000
    inputs = np.array(inputs, dtype="object")
    inputs[inputs == "X"] = num
    inputs[inputs == "#"] = 0
    inputs[inputs == "O"] = 1
    inputs=inputs.astype(int)
    sum_by_columns = np.sum(inputs, axis = 0)
    sum_by_rows = np.sum(inputs, axis = 1)
    diagonal1 = np.diagonal(inputs)
    diagonal2 = np.diag(np.fliplr(inputs))
    num_rows = len(inputs)
    print (inputs)
    if np.min(sum_by_columns) == num_rows or np.min(sum_by_rows) == num_rows or np.sum(diagonal1) == num_rows or np.sum(diagonal2) == num_rows:
        return "Player 2 wins"
    elif np.max(sum_by_columns) == num_rows*num or np.max(sum_by_rows) == num_rows*num or np.sum(diagonal1) == num_rows*num or np.sum(diagonal2) == num_rows*num:
        return "Player 1 wins"
    else:
        return "It's a Tie"

print (tic_tac_toe([
  ["X", "X", "O"],
  ["O", "X", "O"],
  ["X", "O", "#"]
]))