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
    self.thres = (1, 1)

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

  def attrtoobj(self, attr_se) :
    ret_obj = np.array(self.full_obj_v)
    for attr in attr_se :
      ret_obj *= self.mat[:, attr].reshape(-1)
    ret_obj = set(list(np.where(ret_obj > 0)[0]))
    return ret_obj

  def objtoattr(self, obj_se) :
    ret_attr = np.array(self.full_attr_v)
    for obj in obj_se :
      ret_attr *= self.mat[obj]
    ret_attr = set(list(np.where(ret_attr > 0)[0]))

    return ret_attr

  def LCM(self, nowcon, dim) :
    if len(nowcon[dim]) >= self.thres[dim] :
      self.out.append(nowcon)
      if len(self.out) % 100 == 0 :
        print(len(self.out))
        with open('fca_CD_' + str(len(self.out) // 100) + '.pkl', 'wb') as fp :
          pickle.dump(lst, fp)

    if len(nowcon[dim]) > 0 :
      mx = max(nowcon[dim])
    else :
      mx = -1

    rngmx = 0
    if dim == 1 :
      rngmx = self.max_attr
    else :
      rngmx = self.max_obj

    for i in range(rngmx) :
      if not i in nowcon[dim] :
        nextcon = (None, None)
        if dim == 1 :
          obj = self.attrtoobj(nowcon[dim] | set([i]))
          attr = self.objtoattr(obj)
        else :
          attr = self.objtoattr(nowcon[dim] | set([i]))
          obj = self.attrtoobj(attr)
        nextcon = (obj, attr)

        if len(nextcon[1 - dim]) >= self.thres[1 - dim] :
          if len(nextcon[dim]) > len(nowcon[dim]) :
            ad = min(nextcon[dim] - nowcon[dim])
            if ad > mx and ad == i:
              self.LCM(nextcon, dim)

  def doLCM(self, th1, th2, dim) :
    self.thres = (th1, th2)
    obj, attr = set([]), set([])
    if dim == 1 :
      obj = self.attrtoobj(set([]))
      attr = self.objtoattr(obj)
    else :
      attr = self.objtoattr(set([]))
      obj = self.attrtoobj(attr)

    self.LCM((obj, attr), dim)
    return self.out


fca = FCAmat()
fca.read_from_file('train_num.txt')
lst = fca.doLCM(400, 1, 1)
print('Over Half')
lst = fca.doLCM(1, 400, 0)

with open('fca_CD.pkl', 'wb') as fp :
  pickle.dump(lst, fp)
