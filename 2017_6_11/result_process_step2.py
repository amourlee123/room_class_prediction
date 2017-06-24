#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

csvfile_read   = file( 'step1_result.csv', 'rb' )
reader = csv.reader( csvfile_read )

csvfile_writer = file( 'step2_result.csv', 'wb' )
writer = csv.writer( csvfile_writer )

tmp_orderid = "order_id"
dst_roomid = "predict_roomid"
tmp_predict_p = "probability"
max_predict = 0.0

writer.writerows( [( tmp_orderid, dst_roomid, tmp_predict_p )] )

n = 0
for index, f_line in enumerate( reader ):
    if index < 1:
        continue

    orderid = f_line[0]
    roomid  = f_line[1]
    tmp_predict_p = f_line[2]

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
print ( "共有 %d 条筛选出相邻的数据中最大值的结果" % n )

csvfile_read.close()
csvfile_writer.close()
