#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import loadDataset
import featureNorm
import classifier

if (len(sys.argv) != 2):
    print "Usage: %s data_root_directory" %(sys.argv[0])
    sys.exit(1)

if not (os.path.exists(sys.argv[1])):
    sys.exit(1)

if __name__ == '__main__':
    datasetPath = sys.argv[1]
    if (datasetPath[-1] == '/'):
        datasetPath = datasetPath[:-1]
    trainDataset = datasetPath + '/train/'
    testDataset = datasetPath +'/test/'
    testNewDataset = datasetPath + '/test_new/'

    minIntervalNum = 3
    maxIntervalNum = 6
    cvShare = 5
    highestScore = 0

    print ("Loading train dataset...")
    trainDatasetDic = loadDataset.loadDataFromPath(trainDataset)

    for intervalNum in xrange(minIntervalNum, maxIntervalNum):
        print ("intervalNum = %d") %intervalNum
        print ("Feature Normalization for trainDataset...")
        trainDataFeatureDic = featureNorm.featureNorm1(trainDatasetDic, intervalNum)
        trainFeatureList = [trainDataFeatureDic[key]['feature'] for key in trainDataFeatureDic.keys()]
        trainLabelList = [trainDataFeatureDic[key]['label'] for key in trainDataFeatureDic.keys()]

        #select C and intervalNum using Cross Validation
        segFeatDic, segLabelDic = loadDataset.segDataset(trainFeatureList, trainLabelList, cvShare)
        C, score= classifier.classifierCV(segFeatDic, segLabelDic, cvShare)
        print ("Cost parameter C = %f") %C
        print ("Score for C is %f") %score  
        
        #save the optimal parameter C and intervalNum
        if score > highestScore:
            optimalC = C
            highestScore = score
            optimalInterval = intervalNum
            
    #optimal parameters for C and IntervalNum
    print ("Optimal C = %f") %optimalC
    print ("Optimal IntervalNum = %d") %optimalInterval
    
    #use optimalC and optimalInterval to train classifier SVC
    trainDataFeatureDic = featureNorm.featureNorm1(trainDatasetDic, optimalInterval)
    trainFeatureList = [trainDataFeatureDic[key]['feature'] for key in trainDataFeatureDic.keys()]
    trainLabelList = [trainDataFeatureDic[key]['label'] for key in trainDataFeatureDic.keys()]

    SVC = classifier.classifierTrain(optimalC, trainFeatureList, trainLabelList)
    
    #load and depart test dataset1 and dataset2
    print "Load testDataset from test/ ..."
    testDatasetDic = loadDataset.loadDataFromPath(testDataset)
    
    print "Load testNewDataset from test_new/ ..."
    testNewDatasetDic = loadDataset.loadDataFromPath(testNewDataset)
    
    print "Feature normalizatin for testDataset..."
    testDataFeatureDic = featureNorm.featureNorm1(testDatasetDic, optimalInterval)
    testFeatureList = [testDataFeatureDic[key]['feature'] for key in testDataFeatureDic.keys()]
    testLabelList = [testDataFeatureDic[key]['label'] for key in testDataFeatureDic.keys()]
    
    print "Feature normalizatin for testNewDataset..."
    testNewDataFeatureDic = featureNorm.featureNorm1(testNewDatasetDic, optimalInterval)
    testNewFeatureList = [testNewDataFeatureDic[key]['feature'] for key in testNewDataFeatureDic.keys()]
    testNewLabelList = [testNewDataFeatureDic[key]['label'] for key in testNewDataFeatureDic.keys()]
    
    #classifier accuracy for test and test_new dataset
    testDatasetScore = classifier.classifierTest(SVC, testFeatureList, testLabelList)
    testNewDatasetScore = classifier.classifierTest(SVC, testNewFeatureList, testNewLabelList)
    
    print ("classifier accuracy for testDataset: %f") %testDatasetScore
    print ("classifier accuracy for testNewDataset: %f") %testNewDatasetScore

    print ("Congratulations! @billryan did a nice job for tone classifier!")
