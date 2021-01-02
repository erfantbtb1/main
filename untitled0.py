# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:31:40 2021

@author: Lion
"""

import matplotlib.pyplot as plt
import numpy as np

pos_x = []
pos_y = []

def start_draw(event):
    """jamavarie mokhtasate noghat daroone yek list va rasme shekl"""
    pos_x.append(event.xdata)
    pos_y.append(event.ydata)
    
    """keshidane khotoot va kamel kardane shekl"""
    
    if len(pos_x)>1:
        plt.scatter(pos_x, pos_y, color ="red")
        plt.draw()
        if abs(event.xdata-pos_x[0]) > 0.05*pos_x[0] or \
        abs(event.ydata-pos_y[0]) > 0.05*pos_y[0]:
            plt.plot(pos_x, pos_y, color = "dodgerblue")
            
        else:
            plt.scatter(pos_x[0], pos_y[0], color ="red")
            plt.draw()
            plt.plot([pos_x[-2], pos_x[0]], [pos_y[-2], pos_y[0]], 
                     color = "dodgerblue")    
            fig.canvas.mpl_disconnect(button)
            pos_x.pop()
            pos_y.pop()
            pos_x.append(pos_x[0])
            pos_y.append(pos_y[0])
            plt.fill(pos_x, pos_y, color = "cyan") 

    else : 
        plt.scatter(pos_x[0], pos_y[0], color ="red")
        plt.draw()
    print([event.xdata, event.ydata])

"""moshakhasate nemoodar""" 
   
fig,axis = plt.subplots()

plt.xlim(0,10)
plt.xticks(np.arange(11))

plt.ylim(0,10)
plt.yticks(np.arange(11))

plt.grid()

"""mouse click event for getting points"""

button = fig.canvas.mpl_connect('button_press_event',start_draw)
 