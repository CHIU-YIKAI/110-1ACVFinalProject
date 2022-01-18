
import cv2

from utility import SaveToVideo

def findTemplate(frame, XYplace, WHsize):
    x = 0 if XYplace[0] < 0 else 1920 if XYplace[0] > 1920 else XYplace[0]
    y = 0 if XYplace[1] < 0 else 1080 if XYplace[1] > 1080 else XYplace[1]
    w = WHsize[0]
    h = WHsize[1]
    img = frame[y:y+h, x:x+w]
    return img

def isMovingSameDirection(firstLoc, backLoc, nowLoc):   
    flag =(firstLoc[0] -nowLoc[0] ) * (backLoc[0] - nowLoc[0]) > 0
    return flag

def LevelSixMain(bboxList, frames):
    findBBOXList = []
    for i in bboxList:
        template = findTemplate(frames[0], i[2], i[3])
        backLoc = i[2]
        firstLoc = i[2]

        for idx, frame in enumerate(frames):
            bbox = []
            result = cv2.matchTemplate(frame, template, cv2.TM_SQDIFF_NORMED )    
            cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX)
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
            if isMovingSameDirection(firstLoc, backLoc, minLoc):
                template = findTemplate(frame, minLoc, i[3])
                backLoc = minLoc
            bbox.append(idx)
            bbox.append(i[1])
            bbox.append(minLoc)
            bbox.append((minLoc[0] + i[3][0], minLoc[1] + i[3][1]))
            bbox.append(i[4])
            findBBOXList.append(bbox)

    SaveToVideo(findBBOXList, frames, "levelSix.mp4")
    return findBBOXList