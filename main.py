import cv2

from utility import *
from levelOne import LevelOneMain
from levelTwo import LevelTwoMain
from levelThree import LevelThreeMain
from levleFour import LevelFourMain
from levelFive import LevelFiveMain
from levelSix import LevelSixMain

levelOneBBOX =  LevelOneMain(initBBOX(1), loadImageWithLevel(1))
levelTwoBBOX =  LevelTwoMain(initBBOX(2), loadImageWithLevel(2))
