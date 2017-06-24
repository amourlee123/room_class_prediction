#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

path = '../ctrip/'

f_train = open( path + 'competition_train.txt', 'r' )
f_test = open( path + 'competition_test.txt', 'r' )

if len( sys.argv ) > 2:
    test_lines = f_test.readlines()[:int(sys.argv[1])]
    train_lines = f_train.readlines()[:int(sys.argv[2])]
else:
    test_lines = f_test.readlines()
    train_lines = f_train.readlines()

fout_test = open( 'test_data.txt', 'w' )
fout_train = open( 'train_data.txt', 'w' )

fout_test.writelines( test_lines )
fout_train.writelines( train_lines )

f_test.close()
f_train.close()
fout_test.close()
fout_train.close()
