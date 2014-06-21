#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.svm import SVC
import numpy as np

#kernelFunc = ['linear', 'sigmoid', 'rbf']
kernelFunc = 'linear'

"""
# classifier for Cross Validation
segmentation of feature and its label
"""
def classifierCV(segFeature, segFeatLabel, cvShare):
    scoreC = {}
    for i in xrange(1, cvShare + 1):
        cvFeat = segFeature[i]
        cvLabel = segFeatLabel[i]
        trainFeat = []
        trainLabel = []
        
        for j in xrange(1, cvShare + 1):
            if j != i:
                trainFeat.extend(segFeature[j])
                trainLabel.extend(segFeatLabel[j])
        #CList = [i / 10000. for i in range(1,11)]
        CList = [0.0001, 0.001, 0.01, 0.1, 1, 5]

        for C in CList:
            print ("Train classifier for C = %f using kernel function %s") %(C, kernelFunc)
            kernelSVC = SVC(C,kernel=kernelFunc)
            kernelSVC.fit(trainFeat, trainLabel)
            
            testScore = kernelSVC.score(cvFeat, cvLabel)
            if scoreC.has_key(C):
                scoreC[C].append(testScore)
            else:
                scoreC[C] = []
                scoreC[C].append(testScore)
            print ("Score for C = %f is %f") %(C, testScore)
    
    for key in scoreC.keys():
        scoreC[key] = np.mean(scoreC[key])
    maxAvgScore = 0
    for key in scoreC.keys():
        if scoreC[key] > maxAvgScore:
            maxAvgScore = scoreC[key]
            maxAvgKey = key
            
    return maxAvgKey, maxAvgScore
    
def classifierTrain(C,trainFeat, trainLabel):
    
    kernelSVC = SVC(C,kernel=kernelFunc)
    kernelSVC.fit(trainFeat, trainLabel)
    return kernelSVC
    
def classifierTest(kernelSVC, testFeat, testLabel):

    return kernelSVC.score(testFeat, testLabel)
