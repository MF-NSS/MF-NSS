lblC = {}
lblD = {}

n, m = 10225, 3283

edges = []

with open('CD_curated_AUG.csv', 'r', encoding = 'utf-8') as infile :
  x = infile.readline()
  while len(x) > 0 :
    dta = x.strip().split(',')
    edges.append(dta)
    x = infile.readline()

with open('labels.txt', 'r', encoding = 'utf-8') as infile:
  x = infile.readline()
  while len(x) > 0 :
    dta = x.strip().split(' ')
    a, b = int(dta[0]), dta[1]
    if a < n :
      lblC[b] = a
    else :
      lblD[b] = a - n
    x = infile.readline()

with open('CD_curated_AUG_num.txt', 'w', encoding = 'utf-8') as outfile :
  outfile.write(str(n) + ' ' + str(m) + '\n')
  for dta in edges :
    if dta[0] in lblC.keys() and dta[1] in lblD.keys() :
      outfile.write(str(lblC[dta[0]]) + ' ' + str(lblD[dta[1]]) + '\n')
