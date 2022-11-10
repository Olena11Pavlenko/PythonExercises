#Tic Tac Toe
#https://edabit.com/challenge/5Q2RRBNJ8KcjCkPwP

import numpy as np
def tic_tac_toe(inputs):
  inputs = np.array(inputs)
  inputs[inputs == "X"] = 1
  inputs[inputs == "#"] = 5
  inputs[inputs == "O"] = 0
  inputs=inputs.astype(float)
  sum_by_columns = np.sum(inputs, axis = 0)
  sum_by_rows = np.sum(inputs, axis = 1)
  diagonal1 = np.diagonal(inputs)
  diagonal2 = np.array([inputs[0][2], inputs[1][1], inputs[2][0]])
  if np.min(sum_by_columns) == 0 or np.min(sum_by_rows) == 0 or np.sum(diagonal1) == 0 or np.sum(diagonal2) == 0:
    return "Player 2 wins"
  elif np.max(sum_by_columns) == 3 or np.max(sum_by_rows) == 3 or np.sum(diagonal1) == 3 or np.sum(diagonal2) == 3:
    return "Player 1 wins"
  else:
    return "It's a Tie"

print (tic_tac_toe([
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["O", "#", "X"]
  ]))