#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

rough_result = pd.read_csv( '../data/xgb.csv' )
result_dict = rough_result.set_index( rough_result.index ).T.to_dict( 'list' )
print len(result_dict)

result_new_dict = {}
index = 0
temp_probability = 0
temp_order_id = 0
temp_room_id = 0
for key, value in result_dict.items():
    if index == 0:
        temp_order_id = value[0]
        temp_room_id  = value[1]
        temp_probability = value[2]
    elif value[0] in result_new_dict:
        if value[2] > result_new_dict[value[0]][1]:
            temp_order_id = value[0]
            temp_room_id = value[1]
            temp_probability = value[2]
        else:
            continue
    else:
        temp_order_id = value[0]
        temp_room_id = value[1]
        temp_probability = value[2]
    result_new_dict[temp_order_id] = [ temp_room_id, temp_probability ]

    index += 1

print( len(result_new_dict))
index = 10
for key, value in result_new_dict.items():
    print key, value
    index -= 1
    if index == 0:
        break

result = pd.DataFrame([ 
    [orderid, d[0], d[1]] for orderid, d in result_new_dict.items() ], columns = ["orderid", "predict_roomid", "prob"])
result.to_csv( "../data/result.csv", index = None, encoding = "utf-8" )
