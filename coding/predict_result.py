#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xgboost as xgb
import numpy as np
import csv
import sys


def string_to_num(string):
    tmp = string
    if string.replace( '.', '' ).isdigit():
        return float( tmp )
    else:
        return -1

def process_one_line( l ):
    arr = l.split()
    order = arr[0]
    roomid = arr[5]
    
    return order, roomid
		
#################### 预测概率 ##################################
dtest = xgb.DMatrix( 'test_data_processed.txt' )
bst = xgb.Booster( { 'nthread':4 } )    # init model
bst.load_model( "0001.model" )          # load trained model
dpred = bst.predict( dtest )

#################### 存储OrderId RoomId Probabilities ###########
f = open( 'test_data.txt', 'r' )
f_test = f.readlines()

csvfile = file( sys.argv[1] + '.csv', 'wb' )
writer = csv.writer( csvfile )
writer.writerows( [( 'order_id', 'predict_roomid', 'probability' )] )

n = 0

for index, f_line in enumerate( f_test ):
    if index == 0:
        continue
    else:
        n += 1
        orderid, roomid = process_one_line( f_line )
        writer.writerows( [( orderid, roomid, dpred[i - 1] )] )

'''
tmp_orderid = "order_id"
dst_roomid = "predict_roomid"
tmp_predict_p = "probability"
max_predict = 0.0



csvfile = file( sys.argv[1] + '.csv', 'wb' )
writer = csv.writer( csvfile )
writer.writerows( [( tmp_orderid, dst_roomid, tmp_predict_p )] )

for index, f_line in enumerate( f_test ):
    m += 1
    if index < 1:
        continue

    orderid, roomid = test_process_one_line( f_line )
    tmp_predict_p = dpred[ index-1 ]
    
    if tmp_orderid == orderid:
        if tmp_predict_p > max_predict:
            dst_roomid = roomid
            max_predict = tmp_predict_p
    else:
        if n == 0:
            tmp_orderid = orderid
            dst_roomid = roomid
            max_predict = tmp_predict_p
            n += 1
        else:
            writer.writerows( [( tmp_orderid, dst_roomid, max_predict )] )
            tmp_orderid = orderid
            dst_roomid = roomid
            max_predict = tmp_predict_p
            n += 1

writer.writerows([( tmp_orderid, dst_roomid, max_predict )])
'''   

print n
csvfile.close() 
f.close()
