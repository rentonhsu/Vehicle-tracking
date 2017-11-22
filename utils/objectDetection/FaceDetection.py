import cv2

class FaceDetector:
    cascPath = r'C:\Users\User\Desktop\coding\practice\Study_Group-master\haarcascade_frontalface_default.xml'

    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)

    def getFaces(self, gray):
        return self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )