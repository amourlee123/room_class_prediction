#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xgboost as xgb
# read in data
train_data = xgb.DMatrix( 'train_data_processed.txt' )

# specify parameters via map
param = {'max_depth':6, 'eta':0.3, 'silent':1, 'objective':'binary:logistic' }
num_round = 5
bst = xgb.train( param, train_data, num_round )

#preds=bst.predict(dtest)
bst.save_model( '0001.model' )


