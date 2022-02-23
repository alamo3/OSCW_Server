from client.ClientManager import ClientManager
from client.CarClient import CarClient

class CameraManager:

    def __init__(self, clientManager : ClientManager):
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

    def fetchCameraData(self):
        camInfoJson = {}

        camData = self.clientManager.clientCar.camData

        for i in range(len(camData)):

            camInfoJson[str(i)] = {
                "camera_id" : camData[i][0],
                "camera_name" : camData[i][1],
                "camera_pos" : camData[i][2]
            }

        return camInfoJson