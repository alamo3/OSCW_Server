import socket

TEST_IP = '192.168.68.114'
PORT = 52346


def recvData(s: socket):
    data = s.recv(1024)
    return data.decode()

def sendStr(s: socket, str: str):
    s.send(bytes(str, 'utf-8'))


if __name__ == "__main__":
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clientSocket.connect((TEST_IP, PORT))
    clientSocket.send(bytes('MockClient,3,0,front camera,camera_front,1,back camera,back_camera,2,left camera,left_camera', 'utf-8'))

    dataStr = recvData(clientSocket)

    if not dataStr == "CONNECTED":
        print("Error connecting!")
        exit(-1)

    imageFile = open('Test.png', 'rb').read()
    # Test image sending

    sendStr(clientSocket, 'IMAGE')

    if recvData(clientSocket) == "CAM_ID":
        sendStr(clientSocket, str(0))

    if recvData(clientSocket) == "SIZE":
        sendStr(clientSocket, str(len(imageFile)))

    if recvData(clientSocket) == "SEND_IMAGE":
        clientSocket.send(imageFile)

    if recvData(clientSocket) == "TRANSFER_SUCCESS":
        print("Transfer test successfully complete!")
    else:
        print("Transfer test failed")


