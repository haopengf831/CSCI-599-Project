import airsim
import os
import keyboard
import mousePosition
import time

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# Async methods returns Future. Call join() to wait for task to complete.
client.takeoffAsync().join()
client.moveToPositionAsync(0, 0, 0, 5).join()
client.hoverAsync().join()

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

while True:
    keyboard.wait('m')
    list = mousePosition.func()
    print("Current position" ,list)
    client.moveToPositionAsync(0, list[0], list[1], 3).join()



