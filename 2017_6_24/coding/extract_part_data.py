#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
path = "../../ctrip/"
import csv

f_train = open( path + 'competition_train.txt', 'r' )
csvcontent = file('../data/train_set.csv','wb') 
writer = csv.writer( csvcontent )

if len( sys.argv ) > 1:
    for i in range( int(sys.argv[1]) ):
        line = f_train.readline()
        a = []
        line = line.split()
        for item in line:
            if item == 'NULL':
                a.append( -1 )
            else:
                a.append( item )
        writer.writerow( a )
    csvcontent.close()
f_train.close()


f_test = open( path + 'competition_test.txt', 'r' )
csvcontent = file('../data/test_set.csv', 'wb')
writer = csv.writer( csvcontent )

if len( sys.argv ) > 1:
    for i in range( int(sys.argv[1]) ):
        line = f_test.readline()
        a = []
        line = line.split()
        for item in line:
            if item == 'NULL':
                a.append( -1 )
            else:
                a.append( item )
        writer.writerow( a )
    csvcontent.close()
f_test.close()
