#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

import numpy
labels       = numpy.reshape( numpy.array(labels), (len(labels), 1))
features = numpy.reshape( numpy.array(features), (len(features), 1))

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)
print 'labels_test', labels_test
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print 'pred', pred
print 'the number of test', len(features_test)
print 'The accuracy is: ', accuracy_score(labels_test, pred)
all_zeros = numpy.zeros((29,1))
print 'all_zeros', accuracy_score(labels_test, all_zeros)
print 'The precision_score', precision_score(labels_test, pred)
print 'The recall_score', recall_score(labels_test, pred)
