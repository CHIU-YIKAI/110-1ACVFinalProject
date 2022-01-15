import cv2
import numpy as np
from sklearn.cluster import MeanShift

from levelOne import LevelOneMain
from levelTwo import LevelTwoMain
from levelThree import LevelThreeMain
from levleFour import LevelFourMain
from levelFive import LevelFiveMain
from levelSix import LevelSixMain

def initBBOX(level):
    bboxList = []
    if(level == 1 ):
        tmp = []
        tmp.append(68)
        tmp.append(20)
        tmp.append((1723, 274))
        tmp.append((197, 553))
        tmp.append((0,0,255))
        bboxList = tmp
    elif(level == 2):
        tmp = []
        tmp.append(68)
        tmp.append(20)
        tmp.append((1723,274))       
        tmp.append((197 , 553))
        tmp.append((0,0,255))
        bboxList = tmp
    elif(level == 3):
        tmp = []
        tmp.append(367)
        tmp.append(2)
        tmp.append((1097, 360))       
        tmp.append((160 , 414))
        tmp.append((255,0,0))
        bboxList.append(tmp)
        tmp = []
        tmp.append(367)
        tmp.append(6)
        tmp.append((0, 239))       
        tmp.append((191, 999))
        tmp.append((0,255,0))
        bboxList.append(tmp)
    elif(level == 4):
        tmp = []
        tmp.append(1)
        tmp.append(21)
        tmp.append((1253, 533))       
        tmp.append((1920, 662))
        tmp.append((255,0,0))
        bboxList.append(tmp)
        tmp = []
        tmp.append(1)
        tmp.append(22)
        tmp.append((1292, 459))       
        tmp.append((1920, 661))
        tmp.append((0,255,0))
        bboxList.append(tmp)       
    elif(level == 5):
        tmp = []
        tmp.append(224)
        tmp.append(11)
        tmp.append((546, 291))       
        tmp.append((781, 864))
        tmp.append((0,255,0))
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(12)
        tmp.append((197, 287))       
        tmp.append((567, 996))
        tmp.append((0,0,255))
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(13)
        tmp.append((130, 317))       
        tmp.append((484, 952))
        tmp.append((255,0,255)) # yellow
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(29)
        tmp.append((718, 270))       
        tmp.append((963, 886))
        tmp.append((255,0, 0))
        bboxList.append(tmp)    
    elif(level == 6):
        tmp = []
        tmp.append(224)
        tmp.append(11)
        tmp.append((546, 291))       
        tmp.append((781, 864))
        tmp.append((0,255,0))
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(12)
        tmp.append((197, 287))       
        tmp.append((567, 996))
        tmp.append((0,0,255))
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(13)
        tmp.append((130, 317))       
        tmp.append((484, 952))
        tmp.append((255,0,255)) # yellow
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(29)
        tmp.append((718, 270))       
        tmp.append((963, 886))
        tmp.append((255,0, 0))
        bboxList.append(tmp)    
    return bboxList

def loadImageWithLevel(level):
    startFrame = 0
    EndFrame = 0
    frames = []
    if(level ==1):
        startFrame = 68
        EndFrame = 146
    elif(level == 2):
        startFrame = 68
        EndFrame = 214
    elif(level == 3):
        startFrame = 367
        EndFrame = 464
    elif(level == 4):
        startFrame = 1
        EndFrame = 375
    elif(level == 5):
        startFrame = 224
        EndFrame = 253
    elif(level == 6):
        startFrame = 224
        EndFrame = 430
    
    for i in range(startFrame, EndFrame+1):
        frame = cv2.imread("./MOT17-09/img1/"+str(i).zfill(6) + ".jpg")
        frames.append(frame)
    return frames

levelOneBBOX =  LevelOneMain(initBBOX(1), loadImageWithLevel(1))
