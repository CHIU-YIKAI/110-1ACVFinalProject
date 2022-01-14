from imp import IMP_HOOK
from re import X
import traceback
from xmlrpc.client import MAXINT


import cv2
import numpy as np

def LevelOneMain(bboxList, frames):

    trackWindow = (bboxList[2][0],bboxList[2][1],bboxList[3][0],bboxList[2][1])
    roi = frames[0][bboxList[2][1]:bboxList[2][1]+bboxList[3][1], bboxList[2][0]:bboxList[2][0]+bboxList[3][1]]
    HSVroi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(HSVroi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
    roiHist = cv2.calcHist([HSVroi], [0], mask, [180], [0,180])
    cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)

    termCrit = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 10, 1)
    for frame in frames:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roiHist, [0,180], 1)
        ret, trackWindow = cv2.CamShift(dst, trackWindow, termCrit)
        pts = np.int0(cv2.boxPoints(ret))
        
        frame = cv2.polylines(frame, [pts], True, 255, 2)
        x = pts[1][0] if pts[1][0] < pts[3][0] else pts[3][0]
        y = pts[1][1] if pts[1][1] < pts[3][1] else pts[3][1]
        
        cv2.rectangle(frame, (x, y),(int(x + bboxList[3][0]), int(y + bboxList[3][1] )),bboxList[4],5)
        cv2.imshow("test", frame)
        cv2.waitKey(0)