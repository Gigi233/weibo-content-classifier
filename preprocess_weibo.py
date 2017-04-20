# -*- coding: utf-8 -*-
import codecs
#from imp import reload
import numpy as np
import os
import sys

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding('utf-8')

def loadData(files):
    train_data = []
    train_label = []
    test_data = []
    test_label = []
    train_total = 0
    test_total = 0
    size_total = 0
    kind = 0
    path = os.getcwd() + '/data/'
    for f in files:
        f = path + f
        fp = codecs.open(f, 'r', 'utf-8')
        #print "open {f}:".format(f=f)
        lines = fp.readlines()
        size = len(lines)
        test_size = int(round(size/5))
        train_size = int(size - test_size)
        data = []
        label = []
        data.append(lines)
        tmp = np.zeros((9,), dtype=np.int)
        tmp[kind] = 1
        for i in range(0, size):
            label.append(tmp)
        #print "size = {s1}".format(s1=size)
        fp.close()
        train_data.append(data[:train_size])
        train_label.append(label[:train_size])
        test_data.append(data[train_size:size])
        test_label.append(label[train_size:size])

        size_total = size_total + size
        train_total = train_total + train_size
        test_total = test_total + test_size
        kind = kind + 1
    print ('train', train_total, 'test', test_total, 'total', size_total)
    return train_data, train_label, test_data, test_label

datalist = ['edu','entertainment','finance','health','housing','military','sports','stock','tech']
train_data, train_label, test_data, test_label = loadData(datalist)
