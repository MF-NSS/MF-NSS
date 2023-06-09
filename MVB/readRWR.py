import numpy as np

n, m = 1872, 3261

with open('RWR.npy', 'rb') as f :
  pred = np.load(f)

with open('RWR.txt', 'w') as f :
  for i in range(n) :
    for j in range(n, n + m) :
      f.write(str(i) + ' ' + str(j) + ' ' + str(pred[i][j]) + '\n')

