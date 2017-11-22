import numpy as np
import cv2
import os

class dataLoader:

    def __init__(self, preprocessor=None):
        self.preprocessor = preprocessor

        if self.preprocessor is None:
            self.preprocessor = []

    def load(self, imagePaths, indexAsClass=-2, colorSpace='RGB', verbose=-1):

        images = []
        labels = []

        for i, imagePath in enumerate(imagePaths):

            image = cv2.imread(imagePath)

            if colorSpace == 'YcrCb':
                image = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
            elif colorSpace == 'HLS':
                image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
            elif colorSpace == 'Gray':
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            elif colorSpace == 'RGB':
                pass


            label = imagePath.split(os.path.sep)[indexAsClass]

            if self.preprocessor is not None:
                for preprocessor in self.preprocessor:
                    image = preprocessor.preprocess(image)

            images.append(image)
            labels.append(label)

            if i > 0 and verbose > 0 and (i + 1) % verbose == 0:
                print('[INFO]processed {:5}/{:5}'.format((i + 1), len(imagePaths)))

        return (np.array(images), np.array(labels))

