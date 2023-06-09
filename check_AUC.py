predict = {}
correct = []
n, m = 10225, 3283

min_v = 1e+10
max_v = -1.0

with open('RWR.txt', 'r', encoding = 'utf-8') as infile :
  x = infile.readline()
  while len(x) > 0 :
    yy = x.strip().split(' ')
    predict[(int(yy[0]), int(yy[1]) - n)] = float(yy[2])
    x = infile.readline()
    min_v = min(min_v, float(yy[2]))
    max_v = max(max_v, float(yy[2]))

with open('test_data_num.txt', 'r', encoding = 'utf-8') as infile :
  x = infile.readline()
  while len(x) > 0 :
    dta = x.strip().split(' ')
    correct.append((int(dta[0]), int(dta[1]), int(dta[2])))
    x = infile.readline()

TP, FP, TN, FN = 0, 0, 0, 0

FPRTPR = {}
PR = {}

thres = min_v

while thres < max_v :
  for sample in correct :
    if (sample[0], sample[1]) in predict.keys() :
      pdv = predict[(sample[0], sample[1])]
    else :
      pdv = 0.0

    if sample[2] == 1 and pdv >= thres :
      TP += 1
    if sample[2] == 0 and pdv >= thres:
      FP += 1
    if sample[2] == 1 and pdv < thres:
      FN += 1
    if sample[2] == 0 and pdv < thres:
      TN += 1

  print('Thres:', thres)
  print('Precision:', TP / (TP + FP))
  print('Recall:', TP / (TP + FN))

  FPR = FP / (FP + TN)
  TPR = TP / (TP + FN)

  FPRTPR[FPR] = TPR
  PR[TP/(TP + FP)] = TPR
  thres += 0.05 * (max_v - min_v)

FPRs = sorted(list(FPRTPR.keys()))
Ps = sorted(list(PR.keys()))
TPRs = []

AUC = 0
lastFPR = 0
lastTPR = 0
for FPR in FPRs :
  AUC += (FPR - lastFPR) * ((FPRTPR[FPR] + lastTPR) / 2)
  TPRs.append(FPRTPR[FPR])
  lastFPR = FPR
  lastTPR = FPRTPR[FPR]

print('AUC: ', AUC)

AUPR = 0
lastP = 0
lastR = 0
for P in Ps :
  AUPR += (P - lastP) * ((PR[P] + lastR) / 2)
  lastP = P
  lastR = PR[P]

print('AUPR: ', AUPR)
