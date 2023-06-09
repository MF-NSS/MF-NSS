correct = set([])
predict = set([])
n = 0
m = 0
mode = True

with open('CD_curated_AUG_num.txt') as infile :
  x = infile.readline().strip()
  dt = x.split(' ')
  n = int(dt[0])
  m = int(dt[1])

  x = infile.readline()
  while len(x) > 0 :
    correct.add(x.strip())
    x = infile.readline()

with open('AA_res.txt') as infile :
  x = infile.readline()
  while len(x) > 0 :
    y = x.strip()
    if mode :
      yy = y.split(' ')
      yy[1] = str(int(yy[1]) - n)
      y = ' '.join(yy)
     
    predict.add(y)
    x = infile.readline()

TP = predict.intersection(correct)

print(len(TP) / len(predict))
print(len(TP) / len(correct))
