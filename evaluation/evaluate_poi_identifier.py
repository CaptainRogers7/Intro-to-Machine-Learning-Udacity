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
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
feat_train, feat_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)


### your code goes here 
clf = DecisionTreeClassifier()
clf = clf.fit(feat_train,labels_train)
pred = clf.predict(feat_test)
print "accuracy:", clf.score(feat_test, labels_test)
predictions = clf.predict(feat_test)
print "predictions:", predictions
print "actuals:", labels_test
from sklearn import metrics
print "precision:", metrics.precision_score(labels_test, predictions)
print "recall:", metrics.recall_score(labels_test, predictions)