correct = set([])
predict = set([])
n, m = 10225, 3283
mode = True

with open('test_data_num.txt') as infile :
  x = infile.readline()

  x = infile.readline()
  while len(x) > 0 :
    dta = x.strip().split(' ')
    if dta[2] == '1' :
      correct.add(dta[0] + ' ' + dta[1])
    x = infile.readline()

with open('preliminary.txt') as infile :
  x = infile.readline()
  while len(x) > 0 :
    y = x.strip()
     
    predict.add(y)
    x = infile.readline()

TP = predict.intersection(correct)

print(len(TP) / len(predict))
print(len(TP) / len(correct))

correct = sorted(list(correct))
predict = sorted(list(predict))

ouf1 = open('shuchu.txt', 'w', encoding = 'utf-8')
ouf2 = open('shuchu2.txt', 'w', encoding = 'utf-8')
for i in correct :
  ouf1.write(i + '\n')
for i in predict :
  ouf2.write(i + '\n')
ouf1.close()
ouf2.close()
