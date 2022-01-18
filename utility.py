from difflib import restore
from posixpath import split
import cv2
from matplotlib import pyplot as plt


def SaveToVideo(bboxList, frames, fileName):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(fileName, fourcc, 30.0, (1920,  1080))
    for i in bboxList:
        cv2.rectangle(frames[i[0]], i[2], i[3], i[4], 3)
    for idx, frame in enumerate(frames):
        cv2.putText(frame,str(idx), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255),1,cv2.LINE_AA)
        out.write(frame)

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
        tmp.append((-38, 239))       
        tmp.append((229, 760))
        tmp.append((0,255,0))
        bboxList.append(tmp)
    elif(level == 4):
        tmp = []
        tmp.append(1)
        tmp.append(21)
        tmp.append((1253, 533))       
        tmp.append((63, 129))
        tmp.append((255,0,0))
        bboxList.append(tmp)
        tmp = []
        tmp.append(1)
        tmp.append(22)
        tmp.append((1292, 459))       
        tmp.append((70, 202))
        tmp.append((0,255,0))
        bboxList.append(tmp)       
    elif(level == 5):
        tmp = []
        tmp.append(224)
        tmp.append(11)
        tmp.append((546, 291))       
        tmp.append((235, 573))
        tmp.append((0,255,0))
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(12)
        tmp.append((197, 287))       
        tmp.append((370, 699))
        tmp.append((0,0,255))
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(13)
        tmp.append((130, 317))       
        tmp.append((354, 635))
        tmp.append((255,0,255)) # yellow
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(29)
        tmp.append((718, 270))       
        tmp.append((245, 616))
        tmp.append((255,0, 0))
        bboxList.append(tmp)    
    elif(level == 6):
        tmp = []
        tmp.append(224)
        tmp.append(11)
        tmp.append((546, 291))       
        tmp.append((235, 537))
        tmp.append((0,255,0))
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(12)
        tmp.append((197, 287))       
        tmp.append((370, 699))
        tmp.append((0,0,255))
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(13)
        tmp.append((130, 317))       
        tmp.append((354, 635))
        tmp.append((255,0,255)) # yellow
        bboxList.append(tmp)

        tmp = []
        tmp.append(224)
        tmp.append(29)
        tmp.append((718, 270))       
        tmp.append((245, 616))
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

def loadGroundTruth(level):

    filename = "./GroundTruth/Level" + str(level) + ".txt"
    f = open(filename, 'r')
    lines = f.readlines()
    result =[]
    for line in lines:
        
        lineData = line.split(',')
        
        result.append([int(x) for x in lineData[:6]])
    return result

def compouteIoU(bboxGroundTruth, bbox):
    areaGT = bboxGroundTruth[4] * bboxGroundTruth[5]
    area = (bbox[3][0]- bbox[2][0]) * (bbox[3][1]- bbox[2][1])
    w = min(bbox[3][0], bboxGroundTruth[2] + bboxGroundTruth[4]) - max(bboxGroundTruth[2] , bbox[2][0])
    h = min(bbox[3][1], bboxGroundTruth[3] + bboxGroundTruth[5]) - max(bboxGroundTruth[3] , bbox[2][1])
    
    if w <= 0 or h <= 0:
        return 0
    areaC = w * h

    return areaC / (areaGT + area - areaC)

def drawLineChart():
    years = [1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]
    pops = [2.5,2.7,3,3.3,3.6,4.0,
        4.4,4.8,5.3,6.1,6.5,6.9,7.3]
    deaths = [1.2,1.7,1.8,2.2,2.5,2.7,2.9,3,3.1,3.2,3.5,3.6,4]


    plt.title("test")
    plt.ylabel("IoU")
    plt.xlabel("years")
    plt.plot(years, pops, color= 'r')
    plt.plot(years, deaths, color ='g')
    plt.savefig("test.png")







