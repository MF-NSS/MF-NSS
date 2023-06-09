import pickle
from bigraph.preprocessing import import_files, make_graph
from bigraph.bigraph import aa_predict
from bigraph.bigraph import cn_predict
from bigraph.bigraph import jc_predict
from bigraph.bigraph import pa_predict
from bigraph.bigraph import katz_predict

df, df_nodes = import_files('CD_curated_num.csv', 'labels.csv')
#df, df_nodes = import_files()
G = make_graph(df)
predict = katz_predict(G, df_nodes)

with open('Katz.pkl', 'wb') as fp :
  pickle.dump(predict, fp)

#print(predict)
