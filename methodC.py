import random

def inc(array, key, value) :
  if not key in array.keys() :
    array[key] = set([value])
  else :
    array[key].add(value)
    
CDD = {}

Cs, Ds = [], []

with open('CD_curated_AUG.csv', 'r', encoding = 'utf-8') as infile :
  x = infile.readline()
  while len(x) > 0 :
    dta = x.strip().split(',')
    inc(CDD, dta[0], dta[1])
    Cs.append(dta[0])
    Ds.append(dta[1])
    x = infile.readline()
    
Cs = sorted(list(set(Cs)))
Ds = sorted(list(set(Ds)))

Css, Dss = [], []

for C in Cs :
  if C in CDD.keys() :
    Css.append(C)
    for D in CDD[C] :
      Dss.append(D)

Dss = sorted(list(set(Dss)))

tst = set([])

Csss, Dsss = set([]), set([])

for C in Css :
  for D in Dss :
    if D in CDD[C] :
      if random.random() < 0.1 :
        tst.add((C, D))
      else :
        Csss.add(C)
        Dsss.add(D)
    else :
      if random.random() < 0.1 :
        tst.add((C, D))
      else :
        Csss.add(C)
        Dsss.add(D)

print(len(Css), len(Csss))
print(len(Dss), len(Dsss))

pos = 0
neg = 0
with open('90per_aug.txt', 'w', encoding = 'utf-8') as outfile :
  for C in Csss :
    for D in Dsss :
      if not (C, D) in tst :
        if D in CDD[C] :
          outfile.write(C + ',' + D + ',1\n')
          pos += 1
        elif random.random() < 1/6 :
          outfile.write(C + ',' + D + ',0\n')
          neg += 1
print(pos, neg, pos/(pos + neg))

pos = 0
neg = 0
with open('90per_aug_test.txt', 'w', encoding = 'utf-8') as outfile : 
  for C in Csss :
    for D in Dsss :
      if (C, D) in tst :
        if D in CDD[C] :
          outfile.write(C + ',' + D + ',1\n')
          pos += 1
        else :
          outfile.write(C + ',' + D + ',0\n')
          neg += 1
print(pos, neg, pos/(pos + neg))
