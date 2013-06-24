#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

class Blob:

    def __init__(self, centroid, convexHull, convexHullArea, contour, contourArea):
        self.centroid = centroid
        self.convexHull = convexHull
        self.contour = contour
        self.convexHullArea = convexHullArea
        self.contourArea = contourArea

    def getCentroid(self):
        return self.centroid

    def getConvexHull(self):
        return self.convexHull

    def getContour(self):
        return self.contour

    def getConvexHullArea(self):
        return self.convexHullArea

    def getContourArea(self):
        return self.contourArea 

def getBlobs(BW, minSize, maxSize):
    cs, _ = cv2.findContours(BW.astype(np.uint8), mode = cv2.RETR_EXTERNAL, 
        method = cv2.CHAIN_APPROX_SIMPLE)
    blobList = list()
    for con in cs:
        if abs(cv2.contourArea(con)) > minSize and abs(cv2.contourArea(con)) < maxSize:
            m = cv2.moments(con)
            try:
                # image moments
                m10 = m['m10']
                m00 = m['m00']
                m01 = m['m01']

                cHull = cv2.convexHull(con)

                blobList += [Blob((int(m10/m00), int(m01/m00)),
                    cHull, cv2.contourArea(cHull),
                    con, cv2.contourArea(con))]
            except:
				pass
    return blobList
