# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:02:03 2021

@author: giga
"""
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as plp

"""tarife yek panjere baraye app"""

window = Tk()
window.title('center of the mass')
window.geometry('500x300')

position = []
pos_x = []
pos_y = []
position_khorooji = []
x_khorooji = []
y_khorooji = []
                                               
"""gereftane noghat be soorate file(excel, txt)"""

def get_file_address():
    """baz kardane file va rikhtane an dar list"""
    file_name = askopenfilename(filetypes = (("Text File", "*.txt"),("All File", "*.*")))
    
    with open(file_name) as f:
        position = f.readlines()
        position = ''.join(position).splitlines()
        position = [list(map(int, i.split(','))) for i in position]
        position = np.array(position)
        x_coords = position[0::, 0:1:]
        y_coords = position[0::, 1::]
        
        
        def center_xVorodi(x, y, x_min, x_max):
            """ghesmate asli baraye mohasebeye eleman"""
            z = np.polyfit(x, y, 2)
            za = np.append(z, 0)
            f = np.poly1d(z)
            fa = np.poly1d(za)
            makhraj = np.poly1d.integ(f)
            soorat = np.poly1d.integ(fa)
            center = (soorat(x_max)-soorat(x_min))/(makhraj(x_max)-makhraj(x_min))
            return center
            
get_file_btn = ttk.Button(window, text = "File", command = get_file_address)
get_file_btn.place(x = 350, y = 200)

label_show = ttk.Label(window, text = 'Center of mass: ', )
label_show.config(font = 'mitra', background = 'light grey')
label_show.place(x = 150, y = 50)

"""gereftan be soorate dasti(shekl haye moshakhas)"""

def open_shapes():
    
    fig, axis = plt.subplots()
    plt.xlim(0,20)  
    plt.xticks(np.arange(21))
    plt.ylim(0,20)
    plt.yticks(np.arange(21))
    plt.grid()
    top = Toplevel()
    top.geometry("400x200")
    top.title('Hand draw')
    
    voroodi = Entry(top, width = 50)
    voroodi.place(x = 50, y = 0)
    
    var = StringVar()
    
    shekl_voroodi = Radiobutton(top, text = 'Entry', variable = var)
    hole = Radiobutton(top, text = 'Hole', variable = var)
    shekl_voroodi.place(x = 250, y = 45)
    hole.place(x = 250, y = 65)
    shekl_voroodi.config(value = '0')
    hole.config(value = '1') 
    
    shape_box = Listbox(top) 
    shape_box.insert(0, 'Circle')
    shape_box.insert(1, 'Rectangle')
    shape_box.insert(2, 'Square')
    shape_box.insert(3, 'Triangle')
    shape_box.insert(4, 'Section')
    
    shape_box.place(x = 150, y = 100)
    
    def to_int(adad):
        
        list_adad = list(map(float, adad.split(",")))
        return list_adad
            
    def start_draw(event):
        x_in = []
        y_in = []
        x_out = []
        y_out = []
        
        """jamavarie mokhtasate noghat daroone yek list va rasme shekl"""
        pos_x.append(event.xdata)
        pos_y.append(event.ydata)
        
        """keshidane khotoot va kamel kardane shekl"""
            
        if len(pos_x)>1:
            plt.scatter(pos_x, pos_y, color ="red")
            plt.draw()
            
            if var.get() == '0':
                rang = 'cyan'
                x_in.append(event.xdata)
                y_in.append(event.ydata)
                
            if var.get() == '1':
                x_out.append(event.xdata)
                y_out.append(event.ydata)
                rang = 'white'
                
            if abs(event.xdata-pos_x[0]) > 0.05*pos_x[0] or \
            abs(event.ydata-pos_y[0]) > 0.05*pos_y[0]:
                plt.plot(pos_x, pos_y, color = "dodgerblue")
                    
            else:
                plt.scatter(pos_x[0], pos_y[0], color ="red")
                plt.draw()
                plt.plot([pos_x[-2], pos_x[0]], [pos_y[-2], pos_y[0]], 
                             color = "dodgerblue")    
                pos_x.pop()
                pos_y.pop()
                pos_x.append(pos_x[0])
                pos_y.append(pos_y[0])
                plt.fill(pos_x, pos_y, color = rang)
                pos_x.clear()
                pos_y.clear()
                
                if x_in and x_out and y_in and y_out:
                    print(x_in, x_out, y_in, y_out)
           
    
    click = fig.canvas.mpl_connect('button_press_event', start_draw)
        
    def circle():
        khosoosiat = to_int(voroodi.get())
        if var.get() == '0':
            dayere = plt.Circle((khosoosiat[0], khosoosiat[1]), khosoosiat[2],
                                color = 'cyan' )
            
        else:
            dayere = plt.Circle((khosoosiat[0], khosoosiat[1]), khosoosiat[2],
                                color = 'dodgerblue', fill = False)
        axis.add_artist(dayere)
        plt.draw()
    
    def triangle():
        khosoosiat = to_int(voroodi.get())
        x_cords = [khosoosiat[0], khosoosiat[2], khosoosiat[4],
                   khosoosiat[0]]
        y_cords = [khosoosiat[1], khosoosiat[3], khosoosiat[5],
                   khosoosiat[1]]
        
        if var.get() == '0':
            plt.plot(x_cords, y_cords, color = 'dodgerblue')            
            plt.fill(x_cords, y_cords, color = 'cyan')
            
        else:
            plt.plot(x_cords, y_cords, color = 'dodgerblue')
            plt.fill(x_cords, y_cords, color = 'white')
             
        plt.draw()
    
    def rectangle():
        
        khosoosiat = to_int(voroodi.get())
        x_cords = [khosoosiat[0], khosoosiat[2], khosoosiat[2],
                   khosoosiat[0], khosoosiat[0]] 
        y_cords = [khosoosiat[1], khosoosiat[1], khosoosiat[3], 
                   khosoosiat[3], khosoosiat[1]]
        
        
        
        if var.get() == '0':
            plt.plot(x_cords, y_cords, color = 'dodgerblue' )            
            plt.fill(x_cords, y_cords, color = 'cyan')
            
        else:
            plt.plot(x_cords, y_cords, color = 'dodgerblue' )
            plt.fill(x_cords, y_cords, color = 'white')
             
        plt.draw()
        
    def show():
        
        if shape_box.get(shape_box.curselection()) == 'Circle':
            circle()
         
        elif shape_box.get(shape_box.curselection()) == 'Triangle':
            triangle()
            
        elif shape_box.get(shape_box.curselection()) == 'Rectangle':
            rectangle()
         
        else:
            rectangle()
            
    btn_show = ttk.Button(top, text = 'Show', command = show)
    btn_show.place(x = 150, y = 50)
   
get_shape_btn = ttk.Button(window, text = 'shape', command = open_shapes)
get_shape_btn.place(x = 100, y = 200)  
  
window.mainloop()
