from client import ClientType

class CarClient:

    def __init__(self, clientName, clientIP, numCams, camData):
        self.clientName = clientName
        self.clientIP = clientIP
        self.clientType = ClientType.car_client
        self.numCams = numCams
        self.camData = self.parseCameraData(camData)

    def parseCameraData(self, camData):
        camInfo = []
        # expect: camera id, camera name, camera location
        for i in range(0, len(camData), 3):
            camInfo.append([camData[i], camData[i + 1], camData[i + 2]])

        return camInfo
