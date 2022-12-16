#Tic Tac Toe
#https://edabit.com/challenge/5Q2RRBNJ8KcjCkPwP

import numpy as np
def tic_tac_toe(inputs):
  inputs = np.array(inputs)
  inputs[inputs == "X"] = 4
  inputs[inputs == "#"] = 0
  inputs[inputs == "O"] = 1
  inputs=inputs.astype(float)
  sum_by_columns = np.sum(inputs, axis = 0)
  sum_by_rows = np.sum(inputs, axis = 1)
  diagonal1 = np.diagonal(inputs)
  diagonal2 = np.array([inputs[0][2], inputs[1][1], inputs[2][0]])
  print (inputs)
  if np.min(sum_by_columns) == 3 or np.min(sum_by_rows) == 3 or np.sum(diagonal1) == 3 or np.sum(diagonal2) == 3:
    return "Player 2 wins"
  elif np.max(sum_by_columns) == 12 or np.max(sum_by_rows) == 12 or np.sum(diagonal1) == 12 or np.sum(diagonal2) == 12:
    return "Player 1 wins"
  else:
    return "It's a Tie"

print (tic_tac_toe([
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["O", "#", "X"]
  ]))