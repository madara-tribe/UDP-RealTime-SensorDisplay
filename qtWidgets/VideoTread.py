import os
import cv2
import time
import numpy as np
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QLabel


class Thread(QThread):
    updateFrame = Signal(QImage)
    def __init__(self, parent=None, vid_size=None, server=None):
        QThread.__init__(self, parent)
        self.vid_side = vid_size
        self.server = server
        
    def openCV2Qimage(self, cvImage):
        cvImage = cv2.resize(cvImage, (self.vid_side, self.vid_side))
        height, width, channel = cvImage.shape
        bytesPerLine = channel * width
        cvImageRGB = cv2.cvtColor(cvImage, cv2.COLOR_BGR2RGB)
        image = QImage(cvImageRGB, width, height, bytesPerLine, QImage.Format_RGB888)
        return image
    
    def run(self):
        """Read frame from camera and repaint QLabel widget.
        """
        frame = cv2.imread("sample.png")
        while True:
            #print('Waiting message')
            self.pred_time = self.server._receive()
            ########################
            
            # Creating and scaling QImage
            img = self.openCV2Qimage(frame)
            scaled_img = img.scaled(self.vid_side, self.vid_side, Qt.KeepAspectRatio)
            # Emit signal
            self.updateFrame.emit(scaled_img)

        sys.exit(-1)

    
