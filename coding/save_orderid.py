# -*- coding: utf-8 -*-

f = open('test_data.txt', 'r')
fs = open('orderid.txt', 'w')
fs2 = open('fs2.txt', 'w')

lines = f.readlines()

n = 0
m = 0

sets = set()

tmp = ''

for index, line in enumerate( lines ):
    
    arr = line.split()
    if arr[0] in sets or index == 0:
        continue
    else:
        sets.update( [arr[0]] )
        fs.write( arr[0] )
        fs.write( '\n' )
        m += 1

for index, line in enumerate( lines ):
    arr = line.split()
   
    if index == 0:
        continue
    elif tmp == arr[0]:
        continue
    else:
        fs2.write( arr[0] )
        fs2.write( '\n' )
        tmp = arr[0]
        n += 1


print m
print n
f.close()
fs.close()
