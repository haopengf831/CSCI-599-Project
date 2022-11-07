import os
import time
import pyautogui as pag

def  func():
        screenWidth, screenHeight = pag.size()
        x, y = pag.position()

        # print("Screen size: (%s %s), Position:(%s, %s)\n" % (screenWidth, screenHeight, x, y))

        list = [(x-960)/105.8, (y-540)/105.8]



        os.system('cls')
        return list

# def getX():
#     xValue = x
#     return xValue
#
# def getY():
#     yValue = y
#     return yValue