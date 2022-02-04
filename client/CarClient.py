from client import ClientType

class CarClient:

    def __init__(self, clientName, clientIP, numCams, camData):
        self.clientName = clientName
        self.clientIP = clientIP
        self.clientType = ClientType.car_client
        self.numCams = numCams


