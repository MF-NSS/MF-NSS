import matplotlib.pyplot as plt
cX, cY = [], []
pX, pY = [], []
correct = set([])
predict = set([])
n, m = 2675, 3794
mode = True

with open('test_num.txt') as infile :
  x = infile.readline()
  while len(x) > 0 :
    dta = x.strip().split(' ')
    if dta[2] == '1' :
      cX.append(int(dta[0]))
      cY.append(int(dta[1]))
      correct.add((dta[0], dta[1]))
    x = infile.readline()

with open('preliminary.txt') as infile :
  x = infile.readline()
  while len(x) > 0 :
    y = x.strip()
    yy = y.split(' ')
    #yy[1] = str(int(yy[1]))
    predict.add((yy[0], yy[1]))
    
    pX.append(int(yy[0]))
    pY.append(int(yy[1]))
    x = infile.readline()

'''
plt.hist2d(cX,cY,(n,m))
fig1 = plt.gcf()
fig1.savefig('1.png')

plt.clf()

plt.hist2d(pX,pY,(n,m))
fig1 = plt.gcf()
fig1.savefig('2.png')
'''

TP = predict.intersection(correct)
print(len(TP), len(predict), len(correct))

correct = sorted(list(correct))
predict = sorted(list(predict))

ouf1 = open('shuchu.txt', 'w', encoding = 'utf-8')
ouf2 = open('shuchu2.txt', 'w', encoding = 'utf-8')
for i in correct :
  ouf1.write(str(i[0]) + ' ' + str(i[1]) + '\n')
for i in predict :
  ouf2.write(str(i[0]) + ' ' + str(i[1]) + '\n')
ouf1.close()
ouf2.close()
