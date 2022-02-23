import socket
import threading
import traceback

from client import CarClient


class ClientManager:

    def __init__(self, port, bindIP):
        self.clientCar = None
        self.port = port
        self.bindIP = bindIP
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectedToCar = False
        self.serverThread = None


    def startListening(self):
        self.serverSocket.bind((self.bindIP, self.port))
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.serverSocket.listen(2)
        self.serverThread = threading.Thread(target=self.server, daemon= True)
        self.serverThread.start()

    def getString(self, byteMessage):
        return byteMessage.decode()

    def handleImageTransfer(self, conn):

        conn.send(bytes('CAM_ID', 'utf-8'))
        cam_id = conn.recv(1024).decode()

        conn.send(bytes('SIZE', 'utf-8'))

        size = conn.recv(1024)
        size = int(size)

        conn.send(bytes('SEND_IMAGE', 'utf-8'))

        image = conn.recv(size * 2)

        file = open("images/"+"cam_"+cam_id+".png", "wb")
        file.write(image)
        file.close()

        conn.send(bytes('TRANSFER_SUCCESS', 'utf-8'))

    def server(self):
        while True:

            try:
                conn, addr = self.serverSocket.accept()

                conn.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                self.connectedToCar = True

                data = conn.recv(1024)  # first transmission will be for identification
                dataStr = data.decode()

                # expect to receive clientName, numCams and camData split by commas

                carClientInfo = dataStr.split(",")

                self.clientCar = CarClient.CarClient(carClientInfo[0], addr, int(carClientInfo[1]), carClientInfo[2:])

                conn.send(bytes('CONNECTED','utf-8'))

                conn.settimeout(7.0)

                while True:
                    # expect a ping every few seconds to keep connection alive
                    try:
                        dataStr = conn.recv(1024).decode()

                        if dataStr == "IMAGE":
                            self.handleImageTransfer(conn)

                    except socket.timeout:
                        traceback.print_exc()
                        self.connectedToCar = False
                        conn.close()
                        print("Connection failure!")
                        break


            except:
                traceback.print_exc()
                print("Error ocurred!")
                continue

