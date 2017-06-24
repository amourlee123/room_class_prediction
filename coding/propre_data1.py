# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:08:38 2017

@author: li_yu
"""

import numpy as np 
A_train_path = './data/A_train.csv'
B_train_path = './data/B_train.csv'
B_test_path = './data/B_test.csv'

def convert_to_float1(datapath):
    train = []
    f = open(datapath,'r')
    if datapath == A_train_path:
        num = 40001
    elif datapath == B_train_path:
        num = 2001
    else:
        num = 15463
    for i in range(num):
        line = f.readline()
        line = line.strip('\n')
        line = line.split(',')
        line.append(line[134])
        line.remove(line[134])
        train.append(line)
    train.remove(train[0])

    # convert items to float list
    train_new = []
    for i in range(len(train)):
        item = []
        train[i].remove(train[i][0])
        for j in range(len(train[i])):
            if train[i][j]=='':
                item.append(-1.)
                item.append(1.)            
            elif j != len( train[0] ) - 1:
                item.append(float(train[i][j]))
                item.append(0.)
            else:
                item.append(float(train[i][j]))
        train_new.append(item)
    return train_new


def convert_to_float2(datapath):
    test=[]
    f = open(datapath,'r')
    for i in range(15464):
        line = f.readline()
        # print(line)
        line = line.strip('\n')
        line = line.split(',')
        test.append(line)
    test.remove(test[0])

    # convert items to float list
    test_new = []
    for i in range(len(test)):
        item = []
        test[i].remove(test[i][0])
        for j in range(len(test[i])):
            if test[i][j] == '':
                item.append(-1.)
                item.append(1.)            
            else:
               item.append(float(test[i][j]))
               item.append(0.) 

        test_new.append(item)
    return test_new


A_train = convert_to_float1(A_train_path)
B_train = convert_to_float1(B_train_path)
B_test = convert_to_float2(B_test_path)

def mean_var():
    mean_list = []
    var_list = []
    for i in range(489):
        Atrain_list = [ x[2*i] for x in A_train if x[2*i] != -1 ]
        Btrain_list = [ x[2*i] for x in B_train if x[2*i] != -1 ]
        Btest_list = [ x[2*i] for x in B_test if x[2*i] != -1 ]
        datalist = Atrain_list + Btrain_list + Btest_list
        mean = sum(datalist) / len(datalist)
        tmp_for_var = [ (x-mean)**2 for x in datalist ]
        var = ( sum(tmp_for_var) / len(tmp_for_var) )**0.5
        mean_list.append( mean )
        var_list.append( var )
    return mean_list, var_list

mean, var = mean_var()

def norm( dataMatrix, mean, var ):
    #norm A_train
    for i in range( len(dataMatrix) ):
        for j in range( len(mean) ):
            if dataMatrix[i][2*j] == -1:
                continue
            try:
                dataMatrix[i][ 2*j ] = ( dataMatrix[i][2*j] - mean[j] ) / var[j]
            except ZeroDivisionError:
                dataMatrix[i][ 2*j ] = 0.
    return dataMatrix

A_train = norm(A_train, mean, var)
B_train = norm(B_train, mean, var)
B_test = norm(B_test, mean, var)

'''
#norm B_train        
for i in range(len(B_train)):
    for j in range(len(mean_list)):
        if B_train[i][2*j] == -1:
            continue
        try:
            B_train[i][2*j] = (B_train[i][2*j] - mean_list[j])/var_list[j]
        except ZeroDivisionError:
            B_train[i][2*j]=0.
#norm B_test
for i in range(len(B_test)):
    for j in range(len(mean_list)):
        if B_test[i][2*j] == -1:
            continue
        try:
            B_test[i][2*j] = (B_test[i][2*j] - mean_list[j])/var_list[j]
        except ZeroDivisionError:
            B_test[i][2*j]=0.
'''
def label_list(dataMatrix):
    # get A_train label list
    train_label = []
    for i in range(len(dataMatrix)):
        train_label.append(dataMatrix[i][-1])
    label1 = [i for i in range(len(train_label)) if train_label[i]==1]
    label0 = [i for i in range(len(train_label)) if train_label[i]==0]
    return label1, label0

A_label1, A_label0 = label_list(A_train)
B_label1, B_label0 = label_list(B_train)

A1_subset_0=[]
A2_subset_0=[]
A3_subset_0=[]
A4_subset_0=[]
A5_subset_0 = []
A1_subset_1=[]
A2_subset_1=[]
A3_subset_1=[]
A4_subset_1=[]
A5_subset_1 = []
B1_subset_1=[]
B2_subset_1=[]
B3_subset_1=[]
B4_subset_1=[]
B5_subset_1 = []
B1_subset_0=[]
B2_subset_0=[]
B3_subset_0=[]
B4_subset_0=[]
B5_subset_0 = []

A_subnum1 = len(A_label1) // 5
A_subnum0 = len(A_label0) // 5
for i in range(A_subnum1):
    A1_subset_1.append(A_train[A_label1[i]])
    A2_subset_1.append(A_train[A_label1[i + A_subnum1*1]])
    A3_subset_1.append(A_train[A_label1[i + A_subnum1*2]])
    A4_subset_1.append(A_train[A_label1[i + A_subnum1*3]])
    A5_subset_1.append(A_train[A_label1[i + A_subnum1*4]])
for i in range(A_subnum0):
    A1_subset_0.append(A_train[A_label0[i]])
    A2_subset_0.append(A_train[A_label0[i + A_subnum0*1]])
    A3_subset_0.append(A_train[A_label0[i + A_subnum0*2]])
    A4_subset_0.append(A_train[A_label0[i + A_subnum0*3]])
    A5_subset_0.append(A_train[A_label0[i + A_subnum0*4]])

B_label1.append(B_label0[0])
B_label1.append(B_label0[1])
B_label0.remove(B_label0[0])
B_label0.remove(B_label0[1])

B_subnum1 = len(B_label1) // 5
B_subnum0 = len(B_label0) // 5
for i in range(B_subnum1):
    B1_subset_1.append(B_train[B_label1[i]])
    B2_subset_1.append(B_train[B_label1[i + B_subnum1*1]])
    B3_subset_1.append(B_train[B_label1[i + B_subnum1*2]])
    B4_subset_1.append(B_train[B_label1[i + B_subnum1*3]])
    B5_subset_1.append(B_train[B_label1[i + B_subnum1*4]])
for i in range(B_subnum0):
    B1_subset_0.append(B_train[B_label0[i]])
    B2_subset_0.append(B_train[B_label0[i + B_subnum0*1]])
    B3_subset_0.append(B_train[B_label0[i + B_subnum0*2]])
    B4_subset_0.append(B_train[B_label0[i + B_subnum0*3]])
    B5_subset_0.append(B_train[B_label0[i + B_subnum0*4]])
# A subset
A1_val = A1_subset_0 + A1_subset_1
A1_train = A2_subset_0 + A2_subset_1 + A3_subset_0 + A3_subset_1 + A4_subset_0 + A4_subset_1 + A5_subset_0 + A5_subset_1

A2_val = A2_subset_0 + A2_subset_1
A2_train = A1_subset_0 + A1_subset_1 + A3_subset_0 + A3_subset_1 + A4_subset_0 + A4_subset_1 + A5_subset_0 + A5_subset_1

A3_val = A3_subset_0 + A3_subset_1
A3_train = A1_subset_0 + A1_subset_1 + A2_subset_0 + A2_subset_1 + A4_subset_0 + A4_subset_1 + A5_subset_0 + A5_subset_1

A4_val = A4_subset_0 + A4_subset_1
A4_train = A1_subset_0 + A1_subset_1 + A2_subset_0 + A2_subset_1 + A3_subset_0 + A3_subset_1 + A5_subset_0 + A5_subset_1

A5_val = A5_subset_0 + A5_subset_1
A5_train = A1_subset_0 + A1_subset_1 + A2_subset_0 + A2_subset_1 + A3_subset_0 + A3_subset_1 + A4_subset_0 + A4_subset_1

# B subset
B1_val = B1_subset_0 + B1_subset_1
B1_train = B2_subset_0 + B2_subset_1 + B3_subset_0 + B3_subset_1 + B4_subset_0 + B4_subset_1 + B5_subset_0 + B5_subset_1

B2_val = B2_subset_0 + B2_subset_1
B2_train = B1_subset_0 + B1_subset_1 + B3_subset_0 + B3_subset_1 + B4_subset_0 + B4_subset_1 + B5_subset_0 + B5_subset_1

B3_val = B3_subset_0 + B3_subset_1
B3_train = B1_subset_0 + B1_subset_1 + B2_subset_0 + B2_subset_1 + B4_subset_0 +B4_subset_1 + B5_subset_0 + B5_subset_1

B4_val = B4_subset_0 + B4_subset_1
B4_train = B1_subset_0 + B1_subset_1 + B2_subset_0 + B2_subset_1 + B3_subset_0 + B3_subset_1 + B5_subset_0 + B5_subset_1

B5_val = B5_subset_0 + B5_subset_1
B5_train = B1_subset_0 + B1_subset_1 + B2_subset_0 + B2_subset_1 + B3_subset_0 + B3_subset_1 + B4_subset_0 + B4_subset_1






'''
#A training set
A1_train=[]
A2_train=[]
A3_train=[]
A4_train=[]
A5_train=[]
for i in range(820):
    A1_train.append(A_train[A_label1[i]])
    A2_train.append(A_train[A_label1[i + 820]])
    A3_train.append(A_train[A_label1[i + 820 * 2]])
    A4_train.append(A_train[A_label1[i + 820 * 3]])
    A5_train.append(A_train[A_label1[i + 820 * 4]])
for i in range(5578):
    A1_train.append(A_train[A_label0[i]])
    A2_train.append(A_train[A_label0[i + 5578]])
    A3_train.append(A_train[A_label0[i + 5578 * 2]])
    A4_train.append(A_train[A_label0[i + 5578 * 3]])
    A5_train.append(A_train[A_label0[i + 5578 * 4]])  
# A validation set
A1_val=[]
A2_val=[]
A3_val=[]
A4_val=[]
A5_val=[]
for i in range(207):
    A1_val.append(A_train[A_label1[i + 820 * 5]])
    A2_val.append(A_train[A_label1[i + 820 * 5 + 207]])
    A3_val.append(A_train[A_label1[i + 820 * 5 + 207*2]])
    A4_val.append(A_train[A_label1[i + 820 * 5 + 207*3]])
    A5_val.append(A_train[A_label1[i + 820 * 5 + 207*4]])
for i in range(1395):
    A1_val.append(A_train[A_label0[i + 5578 * 5]])
    A2_val.append(A_train[A_label0[i + 5578 * 5 + 1395]])
    A3_val.append(A_train[A_label0[i + 5578 * 5 + 1395*2]])
    A4_val.append(A_train[A_label0[i + 5578 * 5 + 1395*3]])
    A5_val.append(A_train[A_label0[i + 5578 * 5 + 1395*4]])
#B training set
B1_train=[]
B2_train=[]
B3_train=[]
B4_train=[]
B5_train=[]
for i in range(24):
    B1_train.append(B_train[B_label1[i]])
    B2_train.append(B_train[B_label1[i + 24]])
    B3_train.append(B_train[B_label1[i + 24 * 2]])
    B4_train.append(B_train[B_label1[i + 24 * 3]])
    B5_train.append(B_train[B_label1[i + 24 * 4]])
for i in range(74):
    B1_train.append(B_train[B_label0[i]])
    B2_train.append(B_train[B_label0[i + 74]])
    B3_train.append(B_train[B_label0[i + 74 * 2]])
    B4_train.append(B_train[B_label0[i + 74 * 3]])
    B5_train.append(B_train[B_label0[i + 74 * 4]])  
# A validation set
B1_val=[]
B2_val=[]
B3_val=[]
B4_val=[]
B5_val=[]
for i in range(4):
    B1_val.append(A_train[A_label1[i + 24 * 5]])
    B2_val.append(A_train[A_label1[i + 24 * 5 + 4]])
    B3_val.append(A_train[A_label1[i + 24 * 5 + 4*2]])
    B4_val.append(A_train[A_label1[i + 24 * 5 + 4*3]])
for i in range(7):
    B5_val.append(A_train[A_label1[i + 24 * 5 + 4*4]])
for i in range(76):
    B1_val.append(A_train[A_label0[i + 74 * 5]])
    B2_val.append(A_train[A_label0[i + 74 * 5 + 76]])
    B3_val.append(A_train[A_label0[i + 74 * 5 + 76*2]])
    B4_val.append(A_train[A_label0[i + 74 * 5 + 76*3]])
for i in range(73):
    B5_val.append(A_train[A_label0[i + 74 * 5 + 76*4]])
'''
np.save('./data/A_train.npy', A_train)
np.save('./data/B_train.npy', B_train)
np.save('./data/B_test.npy', B_test)

np.save('./data/1/A_train.npy', A1_train)
np.save('./data/1/A_val.npy', A1_val)
np.save('./data/1/B_train.npy', B1_train)
np.save('./data/1/B_val.npy', B1_val)

np.save('./data/2/A_train.npy', A2_train)
np.save('./data/2/A_val.npy', A2_val)
np.save('./data/2/B_train.npy', B2_train)
np.save('./data/2/B_val.npy', B2_val)

np.save('./data/3/A_train.npy', A3_train)
np.save('./data/3/A_val.npy', A3_val)
np.save('./data/3/B_train.npy', B3_train)
np.save('./data/3/B_val.npy', B3_val)

np.save('./data/4/A_train.npy', A4_train)
np.save('./data/4/A_val.npy', A4_val)
np.save('./data/4/B_train.npy', B4_train)
np.save('./data/4/B_val.npy', B4_val)

np.save('./data/5/A_train.npy', A5_train)
np.save('./data/5/A_val.npy', A5_val)
np.save('./data/5/B_train.npy', B5_train)
np.save('./data/5/B_val.npy', B5_val)

