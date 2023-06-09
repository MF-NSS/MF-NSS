import random
posrate = 1
negrate = 1
tstrate = 0.1

def inc(array, key, value) :
  if key in array.keys() :
    array[key].add(value)
  else :
    array[key] = set([])

usr = set([])
mov = set([])

mat = {}
ma2t = {}
tmat = {}
neg, pos = 0, 0
tstcnt = {'0':0,'1':0}

with open('um.txt', 'r', encoding = 'utf-8') as f :
  tsf = open('test.txt', 'w', encoding = 'utf-8')
  x = f.readline()
  x = f.readline()
  while len(x) > 0 :
    dta = x.strip().split(',')
    usr.add(dta[0])
    mov.add(dta[1])

    if random.random() < tstrate :
      tsf.write(x)
      tstcnt[dta[2]] += 1
      inc(tmat, dta[0], dta[1])
    else :
      if dta[2] == '1' :
        inc(mat, dta[0], dta[1])
      if dta[2] == '0' :
        inc(ma2t, dta[0], dta[1])

    x = f.readline()
tsf.close()

ouf = open('train.txt', 'w', encoding = 'utf-8') 
for user in usr :
  for movie in mov :
    if user in mat.keys() and movie in mat[user] and random.random() < posrate: 
      ouf.write(user + ',' + movie + ',1\n')
      pos += 1
    else :
      if (not user in tmat.keys() or not movie in tmat[user]) and random.random() < negrate :
      #if user in ma2t.keys() and movie in ma2t[user] :
        ouf.write(user + ',' + movie + ',0\n')
        neg += 1
print(pos, neg)
print(tstcnt['1'], tstcnt['0'])
