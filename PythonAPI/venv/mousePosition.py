import os
import time
import pyautogui as pag

screenWidth, screenHeight = pag.size()
def  func():
        screenWidth, screenHeight = pag.size()
        x, y = pag.position()

        # print("Screen size: (%s %s), Position:(%s, %s)\n" % (screenWidth, screenHeight, x, y))

        list = [(x-960)/105.8, (y-540)/105.8]



        os.system('cls')
        return list

# notMove = False
# while True:
#         while True:
#                 a, b = pag.position()
#                 time.sleep(1)
#                 c, d = pag.position()
#                 if(abs(c-a) > 150 or abs(d-b) > 150):
#                         break
#                 time.sleep(1)
#                 e, f = pag.position()
#                 if(abs(e-a) > 150 or abs(f-b) > 150):
#                       break
#                 notMove = True
#
#                 time.sleep(1)
#                 notMove = False
#
#
# def adc():
#         return notMove


# def getX():
#     xValue = x
#     return xValue
#
# def getY():
#     yValue = y
#     return yValue