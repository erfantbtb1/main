# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 07:13:58 2021

@author: giga
"""

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import numpy as np
import matplotlib.pyplot as plt

"""tarife yek panjere baraye app"""
window = Tk()
window.title('center of the mass')
window.geometry('500x300')
position = []
pos_x = []
pos_y = []
                
def graph():
    """sakhtane nemodar baraye rasme shekle morede nazar"""
    fig, axis = plt.subplots()
    plt.xlim(0,10)  
    plt.xticks(np.arange(11))
    plt.ylim(0,10)
    plt.yticks(np.arange(11))
    plt.grid()
    
    
    def start_draw(event):
        """jamavarie mokhtasate noghat daroone yek list va rasme shekl"""
        pos_x.append(event.xdata)
        pos_y.append(event.ydata)
        plt.scatter(pos_x, pos_y)
        plt.draw()
        """keshidane khotoot va kamel kardane shekl"""
        if len(pos_x)>1 and len(pos_y)>1:
            if abs(event.xdata-pos_x[0]) > 0.05*pos_x[0] or abs(event.ydata-pos_y[0]) > 0.05*pos_y[0]:
                plt.plot(pos_x, pos_y)
            else:
                plt.plot([pos_x[-2], pos_x[0]], [pos_y[-2], pos_y[0]])    
                fig.canvas.mpl_disconnect(click)
            
            print([event.xdata, event.ydata])
            
    click = fig.canvas.mpl_connect('button_press_event',start_draw)
   
draw_button = ttk.Button(window, text = 'draw', command = graph)
draw_button.place(x = 150, y = 200)

"""gereftane noghat be soorate file"""

def get_file_address():
    """baz kardane file va rikhtane an dar list"""
    file_name = askopenfilename(filetypes = (("Text File", "*.txt"),("All File", "*.*")))
    with open(file_name) as f:
        position.append(f.readline())
        print(position)
        
get_file_btn = ttk.Button(window, text = "File", command = get_file_address)
get_file_btn.place(x = 300, y = 200)
  
window.mainloop()
