import airsim
import os
import keyboard
import mousePosition
import time
import pyautogui as pag

screenWidth, screenHeight = pag.size()


# connect to the AirSim simulator
client = airsim.MultirotorClient()

client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# Async methods returns Future. Call join() to wait for task to complete.
client.takeoffAsync().join()
client.moveToPositionAsync(0, 0, 0, 5).join()
client.hoverAsync().join()
# time.sleep(10)
# client.moveToPositionAsync(5, 14, 0, 5).join()

# print(client.getMultirotorState())


# time.sleep(3)
# client.moveToPositionAsync(0, 0, -5.1, 3).join()
# client.hoverAsync().join()
#
# time.sleep(2)

# take images
responses = client.simGetImages([
    airsim.ImageRequest("0", airsim.ImageType.DepthVis),
    airsim.ImageRequest("1", airsim.ImageType.DepthPlanar, True)])
print('Retrieved images: %d', len(responses))

# do something with the images
for response in responses:
    if response.pixels_as_float:
        print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
        airsim.write_pfm(os.path.normpath('/temp/py1.pfm'), airsim.get_pfm_array(response))
    else:
        print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
        airsim.write_file(os.path.normpath('/temp/py1.png'), response.image_data_uint8)

notMove = False
count = 0
zaxis = 0
m = 0
n = 0
while True:
    # if(mousePosition.abc() == True):
    #     print("Moving back")


    keyboard.wait('m')
    a, b = pag.position()
    if((a>500 and a<900) and (b>14 and b<84)):
        zaxis = zaxis + 5
        client.moveToPositionAsync(zaxis, m, n, 3).join()
    elif ((a > 980 and a < 1380) and (b > 14 and b < 84)):
        zaxis = zaxis - 5
        client.moveToPositionAsync(zaxis, m, n, 3).join()
    else:
        list = mousePosition.func()
        print("Current position" ,list)
        if(list[0]>=0 and list[1]>=0):
            m = list[0]+zaxis
            n = list[1]+ 0.56*zaxis
            client.moveToPositionAsync(0.01 + zaxis, m, n, 3).join()
        if (list[0] < 0 and list[1] >= 0):
            m = list[0] - zaxis
            n = list[1] + 0.56 * zaxis
            client.moveToPositionAsync(0.01 + zaxis, m, n, 3).join()
        if (list[0] < 0 and list[1] < 0):
            m = list[0] - zaxis
            n = list[1] - 0.56 * zaxis
            client.moveToPositionAsync(0.01 + zaxis, m, n, 3).join()
        if (list[0] >= 0 and list[1] < 0):
            m = list[0] + zaxis
            n = list[1] - 0.56 * zaxis
            client.moveToPositionAsync(0.01 + zaxis, m, n, 3).join()
        client.hoverAsync().join()
    # time.sleep(1)
    # c, d = pag.position()
    # if (abs(c - a) < 150 and abs(d - b) < 150):
    #     count = count + 1
    # time.sleep(1)
    # e, f = pag.position()
    # if (abs(e - a) < 150 and abs(f - b) < 150):
    #     count = count + 1
    # if(count == 2):
    #     notMove = True
    #     zaxis = zaxis + 5
    #     print("not moving")
    #     client.moveToPositionAsync(zaxis, m, n, 3).join()
    #     count = 0
    # time.sleep(1)
    # notMove = False
    # count = 0


    # time.sleep(10)
    # print(client.getMultirotorState())





