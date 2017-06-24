#!/usr/bin/env python
# -*- coding: utf-8 -*-

def string2num( string ):
    tmp = string
    if( string.replace( '.', '').isdigit() ):
        return float( tmp )
    else:
        return -1

fin  = open( 'train_data.txt', 'r' )
fout = open( 'train_data_processed.txt', 'w' )
fin_train = fin.readlines()
for index, line in enumerate( fin_train ):
    if index == 0:
        continue
    arr = line.split()
    indice = 0
    for index2, char in enumerate( arr ):
        if index2  < 6:
            continue
        if index2 == 6:
            fout.write( char )
            fout.write( '\t' )
        elif char == 'NULL':
            indice += 1
            fout.write( '%d:%d' % ( indice, -1 ) )
            fout.write( '\t' )
        else:
            indice += 1
            fout.write( '%d:%s' % ( indice, string2num( char ) ) )
            fout.write( '\t' )
    fout.write( '\n' )

fin.close()
fout.close()

fin  = open( 'test_data.txt', 'r' )
fout = open( 'test_data_processed.txt', 'w' )
fin_test = fin.readlines()
for index, line in enumerate( fin_test ):
    if index < 1:
        continue
    arr = line.split()
    indice = 0
    for index2, char in enumerate( arr ):
        if index2 < 6:
            continue
        elif char == 'NULL':
            indice += 1
            fout.write( '%d:%d' % ( indice, -1 ) )
            fout.write( '\t' )
        else:
            indice += 1
            fout.write( '%d:%s' % ( indice, string2num( char ) ) )
            fout.write( '\t' )
    fout.write( '\n' )

fin.close()
fout.close()

    
