from pathlib import Path

from client.ClientManager import ClientManager
from client.CarClient import CarClient
import time


class CameraManager:

    def __init__(self, clientManager: ClientManager):
        self.alive = True
        self.cameraList = []
        self.clientManager = clientManager

    def getNumCameras(self):
        return len(self.cameraList)

    """
    Camera data is defined as follows:
    { "camera_id" : "int" ,
      "camera_name: "name" ,
      "camera_pos" : "front or left or right or rear" }
    """

    def getCameraImage(self, cam_id):
        self.clientManager.command = "IMAGE_CAM_" + str(cam_id)

        start_time = time.time()
        duration = 0

        # we wait till image is received or 15 seconds
        while not self.clientManager.responses["images"] == "IMAGE_RECEIVED" and duration < 15.0:
            duration = time.time() - start_time

        # check if we actually got the file
        imageFile = Path("images/cam_" + str(cam_id) + ".png")

        return imageFile.is_file()

    def fetchCameraData(self):
        camInfoJson = {}

        camData = self.clientManager.clientCar.camData

        for i in range(len(camData)):
            camInfoJson[str(i)] = {
                "camera_id": camData[i][0],
                "camera_name": camData[i][1],
                "camera_pos": camData[i][2]
            }

        return camInfoJson
