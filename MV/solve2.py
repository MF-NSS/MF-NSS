from collections import defaultdict

from surprise import NMF
from surprise import SVD
from surprise import Dataset
from surprise import Reader
from surprise import accuracy
from surprise.model_selection import train_test_split
import pickle
import matplotlib.pyplot as plt

def get_top_n(predictions, n = 10) :
  top_n = defaultdict(list)
  for uid, iid, true_r, est, _ in predictions :
    top_n[uid].append((iid, est))
  for uid, user_ratings in top_n.items() :
    user_ratings.sort(key=lambda x: x[1], reverse = True)
    top_n[uid] = user_rating[:n]
  return top_n

# path to dataset file
file_path = 'train.txt'
file_path2 = 'test.txt'

# As we're loading a custom dataset, we need to define a reader. In the
# movielens-100k dataset, each line has the following format:
# 'user item rating timestamp', separated by '\t' characters.
reader = Reader(line_format='user item rating', sep=',', rating_scale=(0, 1))

data = Dataset.load_from_file(file_path, reader=reader)
testset = Dataset.load_from_file(file_path2, reader=reader).build_full_trainset().build_testset()
#trainset, testset = train_test_split(data, test_size = 0.3)
algo = SVD()
algo.fit(data.build_full_trainset())

predictions = algo.test(testset)

accuracy.rmse(predictions, verbose=True)

FPRTPR = {}
PR = {}

min_est = 2
max_est = -1

for uid, _, true_r, est, _ in predictions :
  min_est = min(min_est, est)
  max_est = max(max_est, est)

thres = min_est
step = (max_est - min_est) / 20

while thres < max_est :
  TP, FP, TN, FN = 0, 0, 0, 0
  for uid, _, true_r, est, _ in predictions:
    if true_r >= 0.5 and est >= thres :
      TP += 1
    if true_r >= 0.5 and est < thres :
      FN += 1
    if true_r < 0.5 and est >= thres :
      FP += 1
    if true_r < 0.5 and est < thres :
      TN += 1
  print('Thres: ', thres)
  print('Recall: ', TP / (TP + FN))
  print('Precision: ', TP / (TP + FP))
  print(' ')
  FPR = FP / (FP + TN)
  TPR = TP / (TP + FN)

  FPRTPR[FPR] = TPR
  PR[TP/(TP + FP)] = TPR
  thres += step

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

plt.plot(FPRs, TPRs)
plt.savefig('res.png')

'''
kf = KFold(n_splits=3)

algo = NMF()

for trainset, testset in kf.split(data):

    # train and test algorithm.
    algo.fit(trainset)
    predictions = algo.test(testset)

    # Compute and print Root Mean Squared Error
    accuracy.rmse(predictions, verbose=True)
'''
