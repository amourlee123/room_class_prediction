#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.cross_validation import train_test_split
import pandas as pd
import xgboost as xgb

random_seed = 1225

# load train set
train_set = pd.read_csv( '../data/train_set.csv' )
remove_features = [ "orderid","uid","orderdate","hotelid","roomid","basicroomid","orderid_lastord","orderdate_lastord","hotelid_lastord","roomid_lastord","basicroomid_lastord" ]
train_set = train_set.drop( remove_features, axis = 1 )
train_y = train_set.orderlabel
train_set = train_set.drop( ['orderlabel'], axis = 1 )

# features = list( train_set.columns )
# train_set, vali_set = train_test_split( train_set, test_size = 0.2, random_state = 1)
# train = pd.DataFrame( train_set, columns = features )
# vali  = pd.DataFrame( vali_set,  columns = features )
# train = train.drop( remove_features, axis = 1 )
# train_y = train.orderlabel
# train_X = train.drop( ['orderlabel'], axis = 1 )
# vali = vali.drop( remove_features, axis = 1 )
# vali_y  = vali.orderlabel
# vali_X  = vali.drop( ['orderlabel'], axis = 1 )

#features = list( train_X.columns )
#for feature in features:
#    mean_T = train_X[feature].mean()
#    mean_V = vali_X[feature].mean()
#    var_T = train_X[feature].var()
#    var_V = vali_X[feature].var()
#    if var_T == 0:
#        train_X[feature] = 0
#    else:
#        train_X[feature] = ( train_X[feature] - mean_T ) / var_T
#    if var_T == 0:
#        vali_X[feature] = 0
#    else:
#        vali_X[feature] = ( vali_X[feature] - mean_V ) / var_V


# load test set
test = pd.read_csv( '../data/test_set.csv' )
order_id = test.orderid
test_x = test.drop( remove_features, axis = 1 )
# features = list( test_x.columns )
# for index, feature in enumerate(features):
#    mean = test_x[feature].mean()
#    var = test_x[feature].var()
#    if var == 0:
#        test_x[feature] = 0
#    else:
#        test_x[feature] = ( test_x[feature] - mean ) / var


#train_X.to_csv("gshsh.csv" ,index = None, encoding = 'utf-8')
#train_y.to_csv("y.csv" ,index = None, encoding = 'utf-8')

dtest = xgb.DMatrix( test_x )
dtrain = xgb.DMatrix( train_set, label=train_y )
# dval = xgb.DMatrix( vali_X, label = vali_y )
params = {
        'booster': 'gbtree',
        'objective': 'binary:logistic',
        'early_stopping_rounds': 100,
        'eval_metric': 'auc',
        'gamma': 0.1,
        'max_depth': 8,
        'lambda': 550,
        'subsample': 0.7,
        'colsample_bytree': 0.3,
        'min_child_weight': 2.5,
        'eta': 0.3,
        'seed': random_seed,
        'nthread': 7,
        'silent':1
}

watchlist = [(dtrain, 'train')] 
model = xgb.train( params, dtrain, num_boost_round=10, evals = watchlist)
model.save_model( 'xgb.model' )

test_y = model.predict( dtest, ntree_limit = model.best_ntree_limit )
test_result = pd.DataFrame( columns = ["orderid"] )
test_result.orderid = orderid
test_result['score'] = test_y
test_result.to_csv( "../data/xgb.csv", index=None, encoding='utf-8' ) 
