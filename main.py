from utility import *
from levelOne import LevelOneMain
from levelTwo import LevelTwoMain
from levelThree import LevelThreeMain
from levelFour import LevelFourMain
from levelFive import LevelFiveMain
from levelSix import LevelSixMain

import time
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--level', default=1, type=int)

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
    return IoUList, startFrame, firstFrameDate

def main(args):
    sTime = time.time()
    IoU, sFrame, firstFrameData = trackOnImage(args.level)
    eTime = time.time()
    filename = "level" + str(args.level) + ".png"
    frameList = list(range(sFrame, sFrame + len(IoU[1])))
    if args.level < 3:
        firstFrameData = [firstFrameData,[]]
    totalIoU = drawLineChart(IoU[1:], sFrame, filename, firstFrameData)
    print(filename[:-4], totalIoU, eTime - sTime)



if __name__ == '__main__':
      args = parser.parse_args()
      main(args)