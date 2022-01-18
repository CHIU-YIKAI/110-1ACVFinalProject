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
    sFrame = firstFrameDate[0] if level <= 2 else firstFrameDate[0][0]
    for i in range(len(resultBBOX)):
        frameID = sFrame + i
        IoU = compouteIoU(bboxGT[i], resultBBOX[i])
        targetID = resultBBOX[i][1]
        print(frameID,targetID, IoU)

# levelOneBBOX =  LevelTwoMain(initBBOX(1), loadImageWithLevel(1))  #ok
# levelTwoBBOX =  LevelTwoMain(initBBOX(2), loadImageWithLevel(2))  #ok
# LevelThreeBBOX = LevelThreeMain(initBBOX(3), loadImageWithLevel(3))   #could be better
# LevelThreeBBOX = LevelFourMain(initBBOX(4), loadImageWithLevel(4))  #very bad
# LevelThreeBBOX = LevelFiveMain(initBBOX(5), loadImageWithLevel(5))    #ok
# LevelThreeBBOX = LevelSixMain(initBBOX(), loadImageWithLevel(6)) # very bad

level = 3
trackOnImage(level)










