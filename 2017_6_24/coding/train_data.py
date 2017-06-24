#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.cross_validation import train_test_split
import pandas as pd
import xgboost as xgb

random_seed = 1225

# load data
train_set = pd.read_csv( '../data/train_set.csv' )
test_set  = pd.read_csv( '../data/test_set.csv' )

remove_features = [ "orderid","uid","orderdate","hotelid","roomid","basicroomid","orderid_lastord","orderdate_lastord","hotelid_lastord","roomid_lastord","basicroomid_lastord" ]
train_set = train_set.drop( remove_features, axis = 1 )
order_id  = test_set.orderid
room_id = test_set.roomid
test_set  =  test_set.drop( remove_features, axis = 1 )


y = train_set.orderlabel
X = train_set.drop( ['orderlabel'], axis = 1 )
# save data set
# test_set.to_csv( "test.csv", index = None, encoding = "utf-8" )
# train_set.to_csv( "train.csv", index = None, encoding = "utf-8" )

# split train_set to train set and validate set
# features = list( train_set.columns )
# train, val = train_test_split( train_set, test_size = 0.2, random_state = 1)
# train = pd.DataFrame( train, columns = features )
# val = pd.DataFrame( val, columns = features )
# y = train.orderlabel
# X = train.drop( ['orderlabel'], axis = 1 )
# val_y = val.orderlabel
# val_X = val.drop( ['orderlabel'], axis = 1 )

features_norm = list( X.columns )
for feature in features_norm:
    mean_X = X[feature].mean()
    var_X  = X[feature].var()
#    mean_V = val_X[feature].mean()
#    var_V  = val_X[feature].var()
    if var_X == 0:
        X[feature] = 0
    else:
        X[feature] = ( X[feature] - mean_X ) / var_X
#    if var_V == 0:
#        val_X[feature] = 0
#    else:
#        val_X[feature] = ( val_X[feature] - mean_V ) / var_V

for feature in features_norm:
    mean = test_set[feature].mean()
    var = test_set[feature].var()
    if var == 0:
        test_set[feature] = 0
    else:
        test_set[feature] = ( test_set[feature] - mean ) / var

# print( test_set.shape )
# print( y.shape )
# print( X.shape )

dtest = xgb.DMatrix( test_set )
dtrain = xgb.DMatrix( X, label=y )

neg = len(train_set[ train_set.orderlabel == 0]) 
pos = len( train_set[train_set.orderlabel == 1])

params = {
        'booster': 'gbtree',
        'objective': 'binary:logistic',
        'early_stopping_rounds': 100,
        'scale_pos_weight': 27.0/972.0,
        'eval_metric': 'auc',
        'gamma': 0.1,
        'max_depth': 8,
        'lambda': 550,
        'subsample': 0.7,
        'colsample_bytree': 0.3,
        'min_child_weight': 2.5,
        'eta': 0.007,
        'nthread': 7
}
param = {
        'booster': 'gbtree',
        'objective':'binary:logistic',
        'scale_pos_weight': neg/pos,
#        'lambda': 600,
        'max_depth':6, 
        'eta':0.3, 
        'silent':1, 
        'seed': random_seed,
#        'eta': 0.007,
        'nthread': 12
        }
num_round = 5

# watchlist = [(dtrain, 'train'), (dval, 'val')] # the early stopping is based on last set in the earllist
# model = xgb.train( params, dtrain, num_boost_round=200, evals = watchlist )
model = xgb.train( param, dtrain, num_boost_round = 20 )
model.save_model( 'xgb.model' )


#predict test set (from the best iteration)
test_y = model.predict( dtest, ntree_limit = model.best_ntree_limit )
test_result = pd.DataFrame( columns = ["order_id", "room_id"] )
test_result.order_id = order_id
test_result.room_id = room_id
test_result['score'] = test_y
test_result.to_csv( "../data/xgb.csv", index=None, encoding='utf-8' )  #remember to edit xgb.csv , add ""
