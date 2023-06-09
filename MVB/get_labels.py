Cs = set([])
Ds = set([])
lblC = {}
lblD = {}

edges = []

with open('train.txt', 'r', encoding = 'utf-8') as infile :
  x = infile.readline()
  while len(x) > 0 :
    dta = x.strip().split(',')
    edges.append(dta)
    Cs.add(dta[0])
    Ds.add(dta[1])
    x = infile.readline()

Cs = list(Cs)
Ds = list(Ds)

for i, C in enumerate(Cs) :
  lblC[C] = i

for i, D in enumerate(Ds) :
  lblD[D] = i + len(Cs)

with open('labels.csv', 'w', encoding = 'utf-8') as outfile :
  for C in Cs :
    outfile.write(str(lblC[C]) + ',' + C + '\n')
  for D in Ds :
    outfile.write(str(lblD[D]) + ',' + D + '\n')

with open('train_num.csv', 'w', encoding = 'utf-8') as outfile :
  for dta in edges :
    if dta[2] == '1' :
      outfile.write(str(lblC[dta[0]]) + ',' + str(lblD[dta[1]]) + ',1\n')
