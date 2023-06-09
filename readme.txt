------ CTD Dataset ------

Run AA,JC,CN,PA:

  Change the filename in line 14 of adamic_adar.py to '**.pkl'
  Change line 12 of adamic_adar.py to 'predict = **_predict(G, df_nodes)'
  
  Run 'python3 adamic_adar.py'

  Change the filename in line 3 of readBigraph.py to '**.pkl'
  Change the filename in line 6 of readBigraph.py to '**_res.txt'
  Change the filename in line 8 of check_AUC.py to '**_res.txt'

  Run 'python3 readBigraph.py'
  Run 'python3 check_AUC.py'

  **=AA,JC,CN,PA

Run RWR:

  Change the filename in line 8 of check_AUC.py to 'RWR_res.txt'

  Run 'python3 rwr.py'
  Run 'python3 readRWR.py'
  Run 'python3 check_AUC.py'

Run MF:

  Run 'python3 methodA.py'

Run MF-NSS :

  Run 'python3 methodB.py'

Run SRNMF :

  Download the ICTC repository from https://github.com/jungwoonshin/ICTC into another folder, say 'ICTC/'
  move 'my_data.py' to 'ICTC/'
  open 'pre_processing.py', add the following lines to the function get_data(dataset) :
# ========
    if dataset == 'CTD' :
        adj, features, adj_train, train_edges, val_edges, val_edges_false, test_edges, test_edges_false, edges_all, edges_false_all = my_data.get_CTD_edges()
# ========
  open 'ICTC/args.py', edit the line "dataset = **" to "dataset = 'CTD'" 
  copy 'CD_curated.csv' to 'ICTC/'
  copy 'CD_curated_AUG.csv' to 'ICTC/'
  run 'python3 ICTC/srnmf.py'

----- MovieLens Dataset -----

First, go to the MV/ directory.

Run AA,JC,CN,PA:

  Change the filename in line 14 of adamic_adar.py to '**.pkl'
  Change line 12 of adamic_adar.py to 'predict = **_predict(G, df_nodes)'
  
  Run 'python3 adamic_adar.py'

  Change the filename in line 3 of readBigraph.py to '**.pkl'
  Change the filename in line 6 of readBigraph.py to '**_res.txt'
  Change the filename in line 8 of check_AUC.py to '**_res.txt'

  Run 'python3 readBigraph.py'
  Run 'python3 check_AUC.py'

  **=AA,JC,CN,PA

Run MF :

  Run 'python3 solve3.py'

Run MF-NSS :

  Run 'python3 solve2.py'

Run RWR :

  Change the filename in line 8 of check_AUC.py to 'RWR_res.txt'

  Run 'python3 rwr.py'
  Run 'python3 readRWR.py'
  Run 'python3 check_AUC.py'

Run SRNMF :

  Download the ICTC repository from https://github.com/jungwoonshin/ICTC into another folder, say 'ICTC/'
  move 'my_data.py' to 'ICTC/'
  open 'pre_processing.py', add the following lines to the function get_data(dataset) :
# ========
    if dataset == 'MV' :
        adj, features, adj_train, train_edges, val_edges, val_edges_false, test_edges, test_edges_false, edges_all, edges_false_all = my_data.get_MV_edges()
# ========
  open 'ICTC/args.py', edit the line "dataset = **" to "dataset = 'MV'" 
  copy 'train_num.txt' to 'ICTC/' and rename it 'train_num_MV.txt'
  copy 'test_num.txt' to 'ICTC/' and rename it 'test_num_MV.txt'
  run 'python3 ICTC/srnmf.py'

----- HetRec Dataset -----

First, go to the MVB/ directory.

Run AA,JC,CN,PA:

  Change the filename in line 14 of adamic_adar.py to '**.pkl'
  Change line 12 of adamic_adar.py to 'predict = **_predict(G, df_nodes)'
  
  Run 'python3 adamic_adar.py'

  Change the filename in line 3 of readBigraph.py to '**.pkl'
  Change the filename in line 6 of readBigraph.py to '**_res.txt'
  Change the filename in line 8 of check_AUC.py to '**_res.txt'

  Run 'python3 readBigraph.py'
  Run 'python3 check_AUC.py'

  **=AA,JC,CN,PA

Run MF :

  Run 'python3 solve3.py'

Run MF-NSS :

  Run 'python3 solve2.py'

Run RWR :

  Change the filename in line 8 of check_AUC.py to 'RWR_res.txt'

  Run 'python3 rwr.py'
  Run 'python3 readRWR.py'
  Run 'python3 check_AUC.py'

Run SRNMF :

  Download the ICTC repository from https://github.com/jungwoonshin/ICTC into another folder, say 'ICTC/'
  move 'my_data.py' to 'ICTC/'
  open 'pre_processing.py', add the following lines to the function get_data(dataset) :
# ========
    if dataset == 'MVB' :
        adj, features, adj_train, train_edges, val_edges, val_edges_false, test_edges, test_edges_false, edges_all, edges_false_all = my_data.get_MV_edges()
# ========
  open 'ICTC/args.py', edit the line "dataset = **" to "dataset = 'MVB'" 
  copy 'train_num.txt' to 'ICTC/' and rename it 'train_num_MVB.txt'
  copy 'test_num.txt' to 'ICTC/' and rename it 'test_num_MVB.txt'
  run 'python3 ICTC/srnmf.py'
