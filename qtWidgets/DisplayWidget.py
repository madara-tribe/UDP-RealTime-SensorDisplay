import time
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QGridLayout,
                             QHBoxLayout, QVBoxLayout, QLCDNumber, QLabel)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ApplicationWindow(QWidget):
    def __init__(self, server):
        super().__init__()

        self.initCanvas()
        self.initFigure()
        self.initUI()
        self.server = server
        self.now_time = 0
        self.stime = time.time()
        
    def initUI(self):
        # LCD number
        self.lcd1 = QLCDNumber(self)
        self.lcd1.setStyleSheet("QWidget { background-color: rgb(100, 100, 255) }")
        self.lcd2 = QLCDNumber(self)
        self.lcd2.setStyleSheet("QWidget { background-color: rgb(100, 100, 255) }")

        startButton = QPushButton("Start")
        startButton.clicked.connect(self.onStartButton)
        stopButton = QPushButton("Stop")
        stopButton.clicked.connect(self.onStopButton)

        l1 = QHBoxLayout()
        l1.addWidget(self.canvas)

        l2 = QVBoxLayout()
        l2.addWidget(startButton)
        l2.addWidget(stopButton)

        l3 = QGridLayout()
        l3.addWidget(QLabel("Time:"), 0, 0)
        l3.addWidget(self.lcd1, 0, 1)
        l3.addWidget(QLabel("s"), 0, 2)
        l3.addWidget(QLabel("Voltage:"), 1, 0)
        l3.addWidget(self.lcd2, 1, 1)
        l3.addWidget(QLabel("V"), 1, 2)

        l23 = QVBoxLayout()
        l23.addLayout(l2)
        l23.addLayout(l3)
        l23.addStretch(1)

        lMain = QHBoxLayout()
        lMain.addLayout(l1)
        lMain.addLayout(l23)

        self.setLayout(lMain)

        self.setWindowTitle("Realtime Monitor")

    def initCanvas(self):
        self.fig = Figure(figsize=(6, 5), dpi=100)
        self.axes = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)

    def initFigure(self):
        self.t = np.zeros(100)
        self.y = np.zeros(100)
        self.li, = self.axes.plot(self.t, self.y)
        self.axes.set_xlabel("Time[s]")
        self.axes.set_ylabel("Voltage[V]")
        self.axes.set_ylim(0, 100)
        
    def initTime(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFigure)
        self.timer.start()
        
    def time_count(self):
        self.now_time = time.time()-self.stime
        time.sleep(0.01)
        
        
    def updateFigure(self):
        # time plot
        self.time_count()
        self.serT = self.now_time
        self.t = np.append(self.t, self.serT)
        self.t = np.delete(self.t, 0)
        
        # sensor data plot
        self.serY = self.server._receive() # np.random.random_sample()
        self.y = np.append(self.y, self.serY)
        self.y = np.delete(self.y, 0)
        
        self.data.append([self.serT, self.serY])
        self.li.set_xdata(self.t)
        self.li.set_ydata(self.y)
        self.axes.set_xlim(min(self.t), max(self.t))
        
        self.canvas.draw()
        self.lcd1.display(self.t[99])
        self.lcd2.display(self.y[99])
        
    def onStartButton(self):
        self.initFigure()
        self.data = []
        self.initTime()
        
    def onStopButton(self):
        self.timer.stop()
        
