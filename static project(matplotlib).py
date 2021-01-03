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
                fig.canvas.mpl_disconnect(click)
                pos_x.pop()
                pos_y.pop()
                pos_x.append(pos_x[0])
                pos_y.append(pos_y[0])
                plt.fill(pos_x, pos_y, color = "cyan") 

            
    click = fig.canvas.mpl_connect('button_press_event',start_draw)
   
draw_button = ttk.Button(window, text = 'draw', command = graph)
draw_button.place(x = 100, y = 200)

"""gereftane noghat be soorate file(excel, txt)"""

def get_file_address():
    """baz kardane file va rikhtane an dar list"""
    file_name = askopenfilename(filetypes = (("Text File", "*.txt"),("All File", "*.*")))
    with open(file_name) as f:
        position.append(f.readline())
        print(position)
        
get_file_btn = ttk.Button(window, text = "File", command = get_file_address)
get_file_btn.place(x = 350, y = 200)



"""gereftan be soorate dasti(shekl haye moshakhas)"""

def open_shapes():
    
    fig, axis = plt.subplots()
    plt.xlim(0,10)  
    plt.xticks(np.arange(11))
    plt.ylim(0,10)
    plt.yticks(np.arange(11))
    plt.grid()
    
    top = Toplevel()
    top.geometry("400x200")
    top.title('Common Shapes')
    
    voroodi = Entry(top, width = 50)
    voroodi.place(x = 150, y = 0)
    
    shape_box = Listbox(top)
    shape_box.insert(0, 'Circle')
    shape_box.insert(1, 'Rectangle')
    shape_box.insert(2, 'square')
    shape_box.insert(3, 'triangle')
    shape_box.insert(4, 'section')
    shape_box.place(x = 150, y = 100)
    
    def to_int(a):
        list_string = a.split(',')
        list_string.remove('(')
        list_string.remove(')')
        for x in list_string:
            list_adad = []
            list_adad.append(int(x))
        return list_adad
    
    def circle():
        khosoosiat = to_int(voroodi.get())
        dayere = plt.Circle((khosoosiat[0], khosoosiat[1]), khosoosiate[2])
        axis.add_artist(dayere)
    
    def triangle():
        
         
get_shape_btn = ttk.Button(window, text = 'shape', command = open_shapes)
get_shape_btn.place(x = 225, y = 200)  
  
window.mainloop()
