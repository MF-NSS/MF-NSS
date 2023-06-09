import random

def inc(array, key, value) :
  if not key in array.keys() :
    array[key] = set([value])
  else :
    array[key].add(value)
    
CG = {}
DG = {}
CD = {}
CDD = {}
CDD2 = {}

Cs, Gs, Ds = [], [], []

with open('CG.csv', 'r', encoding = 'utf-8') as file :
  x = file.readline()
  while len(x) > 0 :
    dta = x.strip().split(',')
    inc(CG, dta[0], dta[1])
    Gs.append(dta[1])
    x = file.readline()
    
with open('GD_curated.csv', 'r', encoding = 'utf-8') as file :
  x = file.readline()
  while len(x) > 0 :
    dta = x.strip().split(',')
    inc(DG, dta[1], dta[0])
    Gs.append(dta[0])
    x = file.readline() 

with open('CD_curated.csv', 'r', encoding = 'utf-8') as infile :
  x = infile.readline()
  while len(x) > 0 :
    dta = x.strip().split(',')
    inc(CDD, dta[0], dta[1])
    Cs.append(dta[0])
    Ds.append(dta[1])
    x = infile.readline()
    
with open('CD_curated_AUG.csv', 'r', encoding = 'utf-8') as infile :
  x = infile.readline()
  while len(x) > 0 :
    dta = x.strip().split(',')
    if not(dta[0] in CDD.keys() and dta[1] in CDD[dta[0]]):
      inc(CDD2, dta[0], dta[1])
    #Cs.append(dta[0])
    #Ds.append(dta[1])
    x = infile.readline()

Css = sorted(list(set(Cs)))
Gss = sorted(list(set(Gs)))
Dss = sorted(list(set(Ds)))

'''
idC, idG, iDD = {}, {}, {}

for id, C in enumerate(Css) :
  idC[C] = id
for id, G in enumerate(Gss) :
  idG[G] = id
for id, D in enumerate(Dss) :
  idD[D] = id
'''
  
for chemical in CG.keys() :
  for disease in DG.keys() :
    if CG[chemical] == DG[disease] :
      inc(CD, chemical, disease)

with open('input_hint_by_aug.txt', 'w', encoding = 'utf-8') as outfile :         
  for C in Css :
    for D in Dss :
      if C in CDD.keys() and D in CDD[C]:
        outfile.write(C + ',' + D + ',1\n')
      elif not (C in CDD2.keys() and D in CDD2[C]) :
        if random.random() < 1 :
          outfile.write(C + ',' + D + ',0\n')

one = 0
onezero = 0
with open('test_data.txt', 'w', encoding = 'utf-8') as outfile :         
  for C in Css :
    for D in Dss :
      if C in CDD2.keys() and D in CDD2[C] and not (C in CDD.keys() and D in CDD[C]):
        outfile.write(C + ',' + D + ',1\n')
        one += 1
        onezero += 1
      else :
        outfile.write(C + ',' + D + ',0\n')
        onezero += 1
print(one / onezero)
