class CameraManager:

    def __init__(self):
        self.alive = True
        self.cameraList = []

    def getNumCameras(self):
        return len(self.cameraList)

    """
    Camera data is defined as follows:
    { "camera_id" : "int" ,
      "camera_name: "name" ,
      "camera_pos" : "front or left or right or rear" }
    """

    def fetchCameraData(self):
        pass