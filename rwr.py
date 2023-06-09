from pyrwr.rwr import RWR
import numpy as np

n, m = 10225, 3283

rwr = RWR()

rwr.read_graph('CD_curated_num.tsv', 'undirected')

lst = []

for seed in range(1, n + m + 1) :
  lst.append(list(rwr.compute(seed, 0.01, 1e-9, 600)))

with open('RWR.npy', 'wb') as f :
  np.save(f, np.array(lst))
