import socket
import threading
import traceback


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

    def server(self):
        while True:

            try:
                conn, addr = self.serverSocket.accept()

                conn.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                self.connectedToCar = True

                data = conn.recv(1024)
                dataStr = data.decode()

            except socket.timeout:
                traceback.print_exc()
                self.connectedToCar = False
                print("Connection failure!")
                continue
            except:
                traceback.print_exc()
                print("Error ocurred!")
                continue

