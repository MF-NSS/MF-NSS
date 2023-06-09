from pyrwr.rwr import RWR
import numpy as np

n, m = 2675, 3794

rwr = RWR()

rwr.read_graph('train_num.tsv', 'undirected')

lst = []

for seed in range(1, n + m + 1) :
  lst.append(list(rwr.compute(seed, 0.0001, 1e-9, 400)))

with open('RWR.npy', 'wb') as f :
  np.save(f, np.array(lst))
