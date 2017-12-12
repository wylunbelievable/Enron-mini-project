# -*- coding: utf-8 -*-
"""
Created on Sat Dec 09 23:13:54 2017

@author: 王岩磊
"""
import numpy as np
from sklearn.metrics import precision_score, recall_score
pred = np.array( [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]) 
true = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0])

#true_negative = true - pred
#print 'ture_negative', true_negative

print 'The precision score', precision_score(true, pred)
print 'The recall_score', recall_score(true, pred)