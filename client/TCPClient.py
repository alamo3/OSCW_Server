from client import ClientType

class TCPClient:

    def __init__(self, clientName, clientIP):
        self.clientName = clientName
        self.clientIP = clientIP
        self.clientType = ClientType.car_client


