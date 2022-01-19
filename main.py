from utility import *
from levelOne import LevelOneMain
from levelTwo import LevelTwoMain
from levelThree import LevelThreeMain
from levelFour import LevelFourMain
from levelFive import LevelFiveMain
from levelSix import LevelSixMain

def getResultWithLevel(firstFrameDate, level):
    frames = loadImageWithLevel(level)
    if level == 1:
        result = LevelOneMain(firstFrameDate,frames)
    elif level == 2:
        result = LevelTwoMain(firstFrameDate,frames)
    elif level == 3:
        result = LevelThreeMain(firstFrameDate,frames)
    elif level == 4:
        result = LevelFourMain(firstFrameDate,frames)
    elif level == 5:
        result = LevelFiveMain(firstFrameDate,frames)
    elif level == 6:
        result = LevelSixMain(firstFrameDate,frames)
    return result

def trackOnImage(level):
    firstFrameDate = initBBOX(level)
    bboxGT = loadGroundTruth(level)
    resultBBOX = getResultWithLevel(firstFrameDate, level)
    IoUList = []
    tmpIoUList = []
    tmpIoUList = []

    if level < 3:
        startFrame = firstFrameDate[0]
        allFrameCount = int(len(resultBBOX))
    else:
        startFrame =firstFrameDate[0][0]
        allFrameCount = int(len(resultBBOX) / len(firstFrameDate))
    for i in range(len(resultBBOX)):
        if i % allFrameCount == 0:
            IoUList.append(tmpIoUList)
            tmpIoUList =[]
        IoU = compouteIoU(bboxGT[i], resultBBOX[i])
        tmpIoUList.append(IoU)
    IoUList.append(tmpIoUList)
    return IoUList, startFrame

for i in range(1, 7):
    IoU, sFrame = trackOnImage(i)
    filename = "level" + str(i) + ".png"
    frameList = list(range(sFrame, sFrame + len(IoU[1])))
    drawLineChart(IoU[1:], sFrame, filename)
