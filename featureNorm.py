#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# feature normalization with average and variance
def featureNorm1(datasetDic, intervalNum):
    featureDic = {}
    for key in datasetDic.keys():
        f0List = datasetDic[key]['f0']
        engyList = datasetDic[key]['engy']
        i = 0
        j = len(f0List)
        step = j / intervalNum
        spacedPointsList = [i for i in xrange(0, j - (j % intervalNum) + 1, step)] 
        spacedPointsList[-1] = max(spacedPointsList[-1],j)
        #curStepListLen = len(curStepList)
        for i in xrange(intervalNum):
            minJ = spacedPointsList[i]
            maxJ = spacedPointsList[i + 1]
            f0Mu = float(np.mean(f0List[minJ:maxJ]))
            engyMu = float(np.mean(engyList[minJ:maxJ]))
            f0Sigma = float(np.std(f0List[minJ:maxJ]))
            engySigma = float(np.std(engyList[minJ:maxJ]))
            if featureDic.has_key(key):
                featureDic[key]['feature'].extend([f0Mu, f0Sigma, engyMu, engySigma])
            else:
                featureDic[key] = {}
                featureDic[key]['feature'] = []
                featureDic[key]['label'] = datasetDic[key]['label']
                featureDic[key]['feature'].extend([f0Mu, f0Sigma, engyMu, engySigma])
    return featureDic

# feature normalization with average and variance, but without feature energy
def featureNorm2(datasetDic, intervalNum):
    featureDic = {}
    for key in datasetDic.keys():
        f0List = datasetDic[key]['f0']
        #engyList = datasetDic[key]['engy']
        i = 0
        j = len(f0List)
        step = j / intervalNum
        spacedPointsList = [i for i in xrange(0, j - (j % intervalNum) + 1, step)] 
        spacedPointsList[-1] = max(spacedPointsList[-1],j)
        #curStepListLen = len(curStepList)
        for i in xrange(intervalNum):
            minJ = spacedPointsList[i]
            maxJ = spacedPointsList[i + 1]
            f0Mu = float(np.mean(f0List[minJ:maxJ]))
            #engyMu = float(np.mean(engyList[minJ:maxJ]))
            f0Sigma = float(np.std(f0List[minJ:maxJ]))
            #engySigma = float(np.std(engyList[minJ:maxJ]))
            if featureDic.has_key(key):
                #featureDic[key]['feature'].extend([f0Mu, f0Sigma, engyMu, engySigma])
                featureDic[key]['feature'].extend([f0Mu, f0Sigma])
            else:
                featureDic[key] = {}
                featureDic[key]['feature'] = []
                featureDic[key]['label'] = datasetDic[key]['label']
                #featureDic[key]['feature'].extend([f0Mu, f0Sigma, engyMu, engySigma])
                featureDic[key]['feature'].extend([f0Mu, f0Sigma])
    return featureDic

# feature normalization with average and difference
def featureNorm3(datasetDic, intervalNum):
    featureDic = {}
    for key in datasetDic.keys():
        f0List = datasetDic[key]['f0']
        #engyList = datasetDic[key]['engy']
        i = 0
        j = len(f0List)
        step = j / intervalNum
        spacedPointsList = [i for i in xrange(0, j - (j % intervalNum) + 1, step)] 
        spacedPointsList[-1] = max(spacedPointsList[-1],j)
        #curStepListLen = len(curStepList)
        for i in xrange(intervalNum):
            minJ = spacedPointsList[i]
            maxJ = spacedPointsList[i + 1]
            f0Mu = float(np.mean(f0List[minJ:maxJ]))
            f0Diff = np.mean(np.diff(f0List[minJ:maxJ]))
            #engyMu = float(np.mean(engyList[minJ:maxJ]))
            #f0Sigma = float(np.std(f0List[minJ:maxJ]))
            #engySigma = float(np.std(engyList[minJ:maxJ]))
            if featureDic.has_key(key):
                #featureDic[key]['feature'].extend([f0Mu, f0Sigma, engyMu, engySigma])
                #featureDic[key]['feature'].extend([f0Mu, f0Sigma])
                featureDic[key]['feature'].extend([f0Mu, f0Diff])
            else:
                featureDic[key] = {}
                featureDic[key]['feature'] = []
                featureDic[key]['label'] = datasetDic[key]['label']
                #featureDic[key]['feature'].extend([f0Mu, f0Sigma, engyMu, engySigma])
                featureDic[key]['feature'].extend([f0Mu, f0Diff])
    return featureDic
