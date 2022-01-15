import cv2
import numpy as np
from utility import *
# def SaveToVideo(bboxList, frames):
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter('LevelTwo.mp4', fourcc, 30.0, (1920,  1080))
#     for i in bboxList:
#         cv2.rectangle(frames[i[0]], i[1], i[2], i[3], 3)
#     for frame in frames:
#         out.write(frame)

def LevelTwoMain(bboxList, frames):
    w = bboxList[3][0]
    h = bboxList[3][1]

    findBBOXList = []

    trackWindow = (bboxList[2][0],bboxList[2][1],w,h)
    roi = frames[0][bboxList[2][1]:bboxList[2][1]+h, bboxList[2][0]:bboxList[2][0]+h]
    HSVroi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(HSVroi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
    roiHist = cv2.calcHist([HSVroi], [0], mask, [180], [0,180])
    cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)

    termCrit = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 10, 1)
    for idx, frame in enumerate(frames):
        bbox = []
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roiHist, [0,180], 1)
        ret, trackWindow = cv2.CamShift(dst, trackWindow, termCrit)
        pts = np.int0(cv2.boxPoints(ret))
        
        x = pts[1][0] if pts[1][0] < pts[3][0] else pts[3][0]
        y = pts[1][1] if pts[1][1] < pts[3][1] else pts[3][1]
        bbox.append(idx)
        bbox.append((x, y))
        bbox.append((int(x + w), int(y + h)))
        bbox.append(bboxList[4])
        findBBOXList.append(bbox)
    SaveToVideo(findBBOXList, frames, "LevelTwo.mp4")
    return findBBOXList