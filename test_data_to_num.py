n, m = 10225, 3283

lbl = {}

with open('labels.txt', 'r', encoding = 'utf-8') as inf :
  x = inf.readline()
  while len(x) > 0 :
    dta = x.strip().split(' ')
    lbl[dta[1]] = int(dta[0])
    x = inf.readline()

with open('test_data.txt', 'r', encoding = 'utf-8') as inf:
  ouf = open('test_data_num.txt', 'w', encoding = 'utf-8') 
  x = inf.readline()
  while len(x) > 0 :
    dta = x.strip().split(',')
    dta[0] = str(lbl[dta[0]])
    dta[1] = str(lbl[dta[1]] - n)
    ouf.write(dta[0] + ' ' + dta[1] + ' ' + dta[2] + '\n')
    x = inf.readline() 
ouf.close()
