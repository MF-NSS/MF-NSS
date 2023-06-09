n, m = 2675, 3794

lblC = {}
lblD = {}

with open('labels.txt', 'r', encoding = 'utf-8') as inf :
  x = inf.readline()
  while len(x) > 0 :
    dta = x.strip().split(' ')
    if int(dta[0]) < n :
      lblC[dta[1]] = str(int(dta[0]))
    else :
      lblD[dta[1]] = str(int(dta[0]) - n)
    x = inf.readline()

with open('test.txt', 'r', encoding = 'utf-8') as inf:
  ouf = open('test_num.txt', 'w', encoding = 'utf-8') 
  x = inf.readline()
  while len(x) > 0 :
    dta = x.strip().split(',')
    ouf.write(lblC[dta[0]] + ' ' + lblD[dta[1]] + ' ' + dta[2] + '\n')
    x = inf.readline() 
ouf.close()
