import pickle

with open('Katz.pkl', 'rb') as fp :
  predict = pickle.load(fp)

with open('Katz_res.txt', 'w', encoding = 'utf-8') as fp :
  for i in predict :
    fp.write(str(i[0]) + ' ' + str(i[1]) + ' ' + str(predict[i]) + '\n')
