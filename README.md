# UDP Sensor data RealTime Display


# To use "matplotlib" with Qt

Change matplotlib backend and add to python script as follows;
```
# https://matplotlib.org/stable/users/explain/backends.html
vi ~/matplotlib/mpl-data/matplotlibrc

# add
backend: Qt5Agg
```
```python
import matplotlib
matplotlib.use('qtagg')
```
