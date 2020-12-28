# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 06:47:42 2020

@author: giga
"""
import matplotlib.pyplot as plt
import numpy as np

pos = []
def onclick(event):
    """jamavarie mokhtasate noghat daroone yek list"""
    pos.append([event.xdata, event.ydata])
    plt.scatter(event.xdata, event.ydata, s=10)
    print([event.xdata, event.ydata])
    print(len(pos))
    
f,a = plt.subplots()
plt.xlim(0,10)
plt.xticks(np.arange(11))
plt.ylim(0,10)
plt.yticks(np.arange(11))
plt.grid()
f.canvas.mpl_connect('button_press_event',onclick)
f.show()    
