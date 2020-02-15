#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
c1=10.0

for i in range(1,5):
    x=c1**i
    clf = SVC(C=c1**i,kernel='rbf') 
    t0 = time()
    
    clf.fit(features_train,labels_train)
    print "training time:", round(time()-t0, 3), "s"
    t1 = time()
    pred = clf.predict(features_test)
    print "predicting time:", round(time()-t1,3), "s"
    print "The accuracy for C = "+str(x) +"is" + str(accuracy_score(pred,labels_test))
    
#########################################################


