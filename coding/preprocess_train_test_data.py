# -*- coding: utf-8 -*-
"""
Created on Sat May  6 10:27:41 2017

@author: liuweiwei
"""

def string_to_num( string ):
    tmp = string
    if( string.replace( '.', '' ).isdigit() ):
        return float( tmp )
    else:
        return -1


f = open( 'train_data.txt', 'r' )
fo = open( 'train_data_processed.txt', 'w' )
f_train = f.readlines()
for index, l in enumerate( f_train ):
    if index < 1:
        continue
    arr = l.split()
    indice = 0
    for index2, char in enumerate( arr ):
        if index2<6:
            continue
        if index2==6:
            fo.write(char)
            fo.write( '\t' )
        elif char == 'NULL':
            indice += 1
            fo.write( '%d:%d' % ( indice, -1 ) )
            fo.write( '\t' )
        else:
            indice += 1
            fo.write( '%d:%s' % ( indice, string_to_num( char ) ) )
            fo.write( '\t' )
    fo.write( '\n' )
    
f.close()
fo.close()


f = open( 'test_data.txt', 'r' )
fo = open( 'test_data_processed.txt', 'w' )
f_test = f.readlines()
for index, l in enumerate( f_test ):
    if index < 1:
        continue
    arr = l.split()
    indice = 0
    for index2, char in enumerate( arr ):
        if index2 < 6:
            continue
        elif char == 'NULL':
            indice += 1
            fo.write( '%d:%d' % ( indice, -1 ) )
            fo.write( '\t' )
        else:
            indice += 1
            fo.write( '%d:%s' % ( indice, string_to_num( char ) ) )
            fo.write( '\t' )
    fo.write( '\n' )
    
f.close()
fo.close()
