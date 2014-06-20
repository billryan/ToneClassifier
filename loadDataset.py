#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random

def loadDataFromPath(dataStr):
    dataDic = {}
    labelDic = {'four': 4, 'three': 3, 'two': 2, 'one': 1}
    dirList = os.listdir(dataStr)
    for dirName in dirList:
        fileList = os.listdir(dataStr + dirName)
        for fileName in fileList:
            filePrefix, fileSuffix = os.path.segext(fileName)
            fileSuffix = fileSuffix[1:]
            fileRead = open(dataStr + dirName + '/' + fileName)
            featureList = [float(line) for line in fileRead.readlines()]
            if dataDic.has_key(filePrefix):
                dataDic[filePrefix][fileSuffix] = featureList
            else:
                dataDic[filePrefix] = {}
                dataDic[filePrefix]['label'] = labelDic[dirName]
                dataDic[filePrefix][fileSuffix] = featureList
    return dataDic

"""
# trainFeatureList, trainLabelList, crossValidationShare
seg = segmentation
crossValidationShare = 1 / M
"""
def segData(tFList, tLList, cVShare):
    segData = {}
    segLabel = {}
    tFLen = len(tFList)
    spacedPointsIndex = [i for i in xrange(0, tFLen, tFLen / cVShare)]
    spacedPointsIndex[-1] = max(spacedPointsIndex[-1], tFLen)
   
    tFIndex = [i for i in xrange(tFLen)]
    random.shuffle(tFIndex)

    for i in xrange(1, cVShare + 1):   
        for j in xrange(spacedPointsIndex[i - 1], spacedPointsIndex[i]):
            if segData.has_key(i):
                segData[i].append(tFList[tFIndex[j]])
                segLabel[i].append(tFList[tFIndex[j]])
            else:
                segData[i] = []
                segLabel[i] = []
                segData[i].append(tFList[tFIndex[j]])
                segLabel[i].append(tFList[tFIndex[j]])
    return segData, segLabel
