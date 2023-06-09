import numpy as np

n, m = 2675, 3794

with open('RWR.npy', 'rb') as f :
  pred = np.load(f)

with open('RWR.txt', 'w') as f :
  for i in range(n) :
    for j in range(n, n + m) :
      f.write(str(i) + ' ' + str(j) + ' ' + str(pred[i][j]) + '\n')

