import numpy as np
import pickle

lst = []

class FCAmat :

  def __init__(self) :
    self.max_attr = 0
    self.max_obj = 0
    self.full_obj_se = np.array([])
    self.full_attr_se = np.array([])
    self.out = []
    self.thres1 = 1
    self.thres2 = 1

  def setNM(self, n, m) :
    self.max_attr = m
    self.max_obj = n
    self.full_obj_v = np.ones(n, dtype = np.dtype(int))
    self.full_attr_v = np.ones(m, dtype = np.dtype(int))

  def read_from_file(self, fn) :
    with open(fn, 'r', encoding = 'utf-8') as inp :
      xy = inp.readline().strip().split(' ')
      self.setNM(int(xy[0]), int(xy[1]))

      tmpmat = []
      ln_vec = []
      for j in range(self.max_attr) :
        ln_vec.append(0)
      for i in range(self.max_obj) :
        tmpmat.append(ln_vec.copy())

      ln = inp.readline()
      while len(ln) :
        ln_lst = ln.strip().split(' ')
        tmpmat[int(ln_lst[0])][int(ln_lst[1])] = 1
        ln = inp.readline()
      
      self.mat = np.array(tmpmat, dtype = np.dtype(int))

  def updown(self, attr_se) :
    ret_obj = np.array(self.full_obj_v)
    for attr in attr_se :
      ret_obj *= self.mat[:, attr].reshape(-1)
    ret_obj = set(list(np.where(ret_obj > 0)[0]))

    ret_attr = np.array(self.full_attr_v)
    for obj in ret_obj :
      ret_attr *= self.mat[obj]
    ret_attr = set(list(np.where(ret_attr > 0)[0]))

    return ret_obj, ret_attr

  def LCM(self, nowcon) :
    if len(nowcon[1]) >= self.thres2 :
      self.out.append(nowcon)
      if len(self.out) % 100 == 0 :
        print(len(self.out))
        with open('fca_CD.pkl', 'wb') as fp :
          pickle.dump(lst, fp)

    if len(nowcon[1]) > 0 :
      mx = max(nowcon[1])
    else :
      mx = -1

    for i in range(self.max_attr) :
      if not i in nowcon[1] :
        nextcon = self.updown(nowcon[1] | set([i]))
        if len(nextcon[0]) >= self.thres1 :
          if len(nextcon[1]) > len(nowcon[1]) :
            ad = min(nextcon[1] - nowcon[1])
            if ad > mx and ad == i:
              if nextcon[1] == set([0, 1, 2, 3, 4, 5]) :
                print(nowcon)
              self.LCM(nextcon)

  def doLCM(self, th1, th2) :
    self.thres1 = th1
    self.thres2 = th2
    self.LCM(self.updown(set([])))
    return self.out


fca = FCAmat()
fca.read_from_file('CD_curated_num.txt')
lst = fca.doLCM(70, 1)

with open('fca_CD.pkl', 'wb') as fp :
  pickle.dump(lst, fp)
