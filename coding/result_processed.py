# -*- coding: utf-8 -*-

import csv

csvfile1 = file( './result0170611.csv', 'rb' )
reader = csv.reader( csvfile1 )


csvfile2 = file( 'result.csv', 'wb' )
writer = csv.writer( csvfile2 )

csv_upload = file( 'uploadfile.csv', 'wb' )
writer_upload = csv.writer( csv_upload )

writer_upload.writerows( [('orderid', 'predict_roomid')] )

sets = set()
n = 0

for index, line in enumerate(reader):
    tmp_orderid = line[0]
    if  tmp_orderid in sets or index == 0:
        continue
    else:
        sets.update( [tmp_orderid] )
        max_prob = 0
        room_id = ''
        csv_tmp = file( './result0170611.csv', 'rb' )
        reader_tmp = csv.reader( csv_tmp )
        for line2 in reader_tmp:
            if line2[0] == tmp_orderid:
                if line2[2] > max_prob:
                    max_prob = line2[2]
                    room_id = line2[1]
        writer.writerows([( tmp_orderid, room_id, max_prob )])
        writer_upload.writerows( [( tmp_orderid, room_id )] )
        n += 1
        csv_tmp.close()


print n
csvfile1.close()
csvfile2.close()
csv_upload.close()
