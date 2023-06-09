import pickle
import hashlib

n, m = 2675, 3794
rate = 0

with open('fca_CD.pkl', 'rb') as fn:
  FC = pickle.load(fn)

ouf = open('preliminary.txt', 'w', encoding = 'utf-8') 
row = [0 for i in range(m)]
mat = [row.copy() for i in range(n)]

for i in range(len(FC)) :
  for j in range(i + 1, len(FC)) :
    fc1, fc2 = FC[i], FC[j]
    fca, fcb = [], []
    if len(fc1[0]) > len(fc2[0]) :
      fca = fc1
      fcb = fc2
    else :
      fca = fc2
      fcb = fc1
    int0 = fca[0].intersection(fcb[0])
    int1 = fca[1].intersection(fcb[1])

    if int0 == fcb[0] :
      if int1 == fca[1] :
        rt0 = len(int0) / len(fca[0])
        rt1 = len(int1) / len(fcb[1])

        if rt0 > rate or rt1 > rate :
          pred0 = fca[0] - fcb[0]
          pred1 = fcb[1] - fca[1]
          for x in pred0 :
            for y in pred1 :
              mat[x][y] = 1

for i in range(n) :
  for j in range(m) :
    if mat[i][j] == 1 :
      ouf.write(str(i) + ' ' + str(j) + '\n')
ouf.close()
