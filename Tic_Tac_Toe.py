#1) Create a function that takes a list of character inputs from a Tic Tac Toe game. 
# Inputs will be taken from player1 as "X", player2 as "O", and empty spaces as "#". 
# The program will return the winner or tie results.
#2) generalize the task to any matrix size (3+). I.e. you need to find if any player has full row/column/diagonal
#3) generalize the task to any symbol, i.e. there could be players A - B, X - O, S - K. And result should say "Player S won"

import numpy as np
def tic_tac_toe(inputs):
    num1 = 1000
    num2 = 100
    inputs = np.array(inputs, dtype="object")
    inputs = np.where(inputs == "X", num1, inputs)
    inputs = np.where(inputs == "@", num2, inputs)
    inputs = np.where(inputs == "#", 0, inputs)
    inputs = np.where(inputs == "O", 1, inputs)
    #inputs[inputs == "X"] = num1
    #inputs[inputs == "@"] = num2
    #inputs[inputs == "#"] = 0
    #inputs[inputs == "O"] = 1
    inputs=inputs.astype(int)
    sum_by_columns = np.sum(inputs, axis = 0)
    sum_by_rows = np.sum(inputs, axis = 1)
    diagonal1 = np.diagonal(inputs)
    diagonal2 = np.diag(np.fliplr(inputs))
    num_rows = len(inputs)
    if np.min(sum_by_columns) == num_rows or np.min(sum_by_rows) == num_rows or np.sum(diagonal1) == num_rows or np.sum(diagonal2) == num_rows:
        return "Player O wins"
    elif np.max(sum_by_columns) == num_rows*num1 or np.max(sum_by_rows) == num_rows*num1 or np.sum(diagonal1) == num_rows*num1 or np.sum(diagonal2) == num_rows*num1:
        return "Player X wins"
    elif num2*num_rows in sum_by_columns or num2*num_rows in sum_by_rows or np.mean(diagonal1) == num2 or np.mean(diagonal2) == num2:
        return "Player @ wins"
    else:
        return "It's a Tie"

print (tic_tac_toe([
  ["X", "X", "O", "@"],
  ["O", "X", "O", "@"],
  ["X", "@", "O", "O"],
  ["@", "X", "O", "@"]
]))