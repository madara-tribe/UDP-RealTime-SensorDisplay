# RealTime Display for UDP Sensor data with Qt

Get sensor data from jetson and send to GUI on Mac (Pyside)



# To use "matplotlib" with PyQt5

Change matplotlib backend and add to python script as follows;
```
# https://matplotlib.org/stable/users/explain/backends.html
vi ~/matplotlib/mpl-data/matplotlibrc

# add
backend: Qt5Agg
```
```python
import matplotlib
matplotlib.use('Qt5Agg')
```

## PyQt version check
```python
from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
print("Qt: v", QT_VERSION_STR, "\tPyQt: v", PYQT_VERSION_STR)
```




# References
- [PyQt + Matplotlib Real-Time plot Arduino](https://org-technology.com/posts/pyqt-matplotlib-realtime-plot-3.html)
