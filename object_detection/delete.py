from decimal import Rounded
from email.errors import MisplacedEnvelopeHeaderDefect
from logging import PlaceHolder
from tkinter import *
from tkinter import messagebox
from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from tokenize import String
import numpy as np
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter.font import BOLD
from setuptools import Command
from PIL import ImageTk, Image
from turtle import color, width
import cv2                      #pip install opencv-python 
import matplotlib.pyplot as plt # pip install matplotlib  
import cvzone                   # pip install cvzone
import sys

    
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = "frozen_inference_graph.pb"

config_file ='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
model = cv2.dnn_DetectionModel(frozen_model,config_file)

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().split('\n')
            
classLabels = []#empty list of python
file_name = 'Labels.txt'
with open(file_name,'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')
    # classables.append(fpt.read())
            
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5,127.5,127.5))
model.setInputSwapRB(True)

confThreshold= 0.55
nmsThreshold= 0.2
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
# Color =(0,255,0)#black name
f_size =3
f_bold =3

f_scale = 1
from pptx.dml.color import RGBColor
RGBColor(0xFF, 0x00, 0x00) 
colour_dict={'Blue': '0xff, 0, 0','Green':'0x00, 0xFF, 0x00','White':'0xFF, 0xFF, 0xFF','Sky_blue':'0xff, 0xff, 0x00','Pink':'0xFF,0x16,0xF4'}

lst = ['Blue','Green','White','Sky_blue','Pink']

def show_img():
    # file = filedialog.askopenfilename(defaultextension=".txt",filetypes= [("All Files","*.*"),("Text Document","*.txt")])  
    # # img_path = user_entry.get()
    # code =(var.get())
    # print(var.get())
    # print("this is color: ",Color)
    
    # Color = RGBColor(*map(lambda v : int(v, 16), colour_dict[(lst[i])].split(',')))
    
    global i
    i=int(var.get())
    print(" i type is: ",type(i))
    Color = RGBColor(*map(lambda v : int(v, 16), colour_dict[(lst[i])].split(',')))
    print("this is rgb: ",Color,colour_dict[(lst[i])].split(','))
    imges = cv2.imread('1655207398778.jpg')  

    if imges.shape[0]>1000:
        f_size = 4
        f_bold = 5
        box=50
        fixed_height = 3070
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        # Color =(102, 0, 0)#black name

    elif 1000>imges.shape[0]>690:
        f_size = 2
        f_bold = 3
        box=30
        fixed_height = 3070
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        # Color =(102, 0, 0)#black name
    elif 690>imges.shape[0]>550:
        f_size = 1
        f_bold = 2
        box=5
        fixed_height = 10000
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        # Color =(102, 0, 0)#black name
    elif 550>imges.shape[0]>250:
        f_size = 1
        f_bold = 2
        box=10
        fixed_height = 7000
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        # Color =(102, 0, 0)#black name
    else :        
        f_size = .5
        f_bold = 1
        box=5
        fixed_height = 10000
        font = cv2.FONT_HERSHEY_TRIPLEX 
        # Color =(160, 64, 0)#black name

        
    classIds, confs, bbox = net.detect(imges,confThreshold ,nmsThreshold )
    print(classIds,confs)
    

    # ClassIndex , confidence, bbox = model.detect(imges,confThreshold = 0.5 )
            
    # for ClassInd , conf, boxes in zip (ClassIndex.flatten(), confidence.flatten(), bbox):
    #     cv2.rectangle(img,boxes,(255,0,0),2)
    #     cv2.putText(img,classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40), font ,f_scale , Color,f_bold)

    if len(classIds) > 0:
        if len(confs) > 0:       
            for classIds,confs,boxes in zip(classIds.flatten(), confs.flatten(), bbox):
                cvzone.cornerRect(imges, boxes)
                cv2.putText(imges,f'{classNames[classIds-1].upper()} {round(confs*100,2)}',(boxes[0]+box,boxes[1]+box),
                    font,f_size,
                    Color,f_bold)          
    
    # imges = cv2.resize(img,(1550,840,img.ANTIALIAS)) 

    # imgs = ImageTk.PhotoImage(imges)
    # imges = imges.resize((450, 350))#, Image.ANTIALIAS
        
        height_percent = (fixed_height / float(imges.shape[1]))
        width_size = int((float(imges.shape[0]) * float(height_percent)))
        stretch_near = cv2.resize(imges, (width_size,fixed_height),interpolation = cv2.INTER_NEAREST)
        cv2.namedWindow("Display", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Display',width_size,fixed_height)
        cv2.imshow("Display",stretch_near )
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    # else:
    #     none_detection()

i = 0
def option():
    global i
    i = var.get() 
    
if __name__ == "__main__": 
    
    
    project = Tk()
    # global Color

    project.iconbitmap("Custom-Icon-Design-Mono-General-2-Search.ico")
    bg_color = '#5DADE2'
    project.geometry("500x600")
    project.minsize(400,200)
    project.configure(bg=bg_color )
    project.title("Object Detection Project")

        
        
    aman = Label(text ="This is Aman Sahu , the Software Engineer" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
    aman.grid(row  = 0, column=0,sticky= N)

    f0 = Frame(project,bg = ('#CCCCFF'), borderwidth=3,relief=SUNKEN)
    f0.grid(row=0, column=0, sticky=" ",)
    f0.grid_columnconfigure(0, weight=1)
    
    f1 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
    f1.grid(row = 0,column = 0,padx =25,pady= 25)
    f2 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
    f2.grid(row = 1,column = 0,padx =25,pady= 25)
    f3 = Frame(f0,bg = "#BB8FCE", borderwidth=3,relief=GROOVE)
    f3.grid(row = 0,rowspan = 2,column = 1,padx =25,pady= 25)

    process_img = Button(f1,text ="IMAGE",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE"
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 20 bold", command = show_img, )
    # process_img.grid(row = 0,column = 0)
    process_img.grid(padx = 5,pady = 5)#,anchor = "nw",padx = 5,pady = 5
  
    amans = Label(f3,text ="Choose Label Color" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
    amans.pack()
    var = StringVar()
    var.set(0)
#colour_dict={'Blue': '0xff, 0, 0','Green':'0x00, 0xFF, 0x00','White':'0xFF, 0xFF, 0xFF','Sky_blue':'0xff, 0xff, 0x00','Pink':'0xFF,0x16,0xF4'}

    radio = Radiobutton(f3,text="Blue",bg = '#0000FF'
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 15 bold",variable=var,value=(0)).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
    radio = Radiobutton(f3,text="Green",bg = '#00FF00'
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 15 bold",variable=var,value=(1)).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
    radio = Radiobutton(f3,text="White",bg = '#FFFFFF'
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 15 bold",variable=var,value=(2)).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
    radio = Radiobutton(f3,text="Aqua",bg = '#00FFFF'
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 15 bold",variable=var,value=(3)).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
    radio = Radiobutton(f3,text="Pink",bg = '#FF00FF'
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 15 bold",variable=var,value=(4)).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
    Button(f3,text="Apply",padx= 10,command = option, bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE"
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 13 bold").pack(padx = 5,pady = 5,ipadx = 0,ipady = 0)

        
    # userv = StringVar()
    # passv = StringVar()

    # user_entry = Entry(f3,textvariable= userv,font = cv2.FONT_HERSHEY_COMPLEX_SMALL)
    # pass_entry = Entry(f4,textvariable= passv,font = cv2.FONT_HERSHEY_COMPLEX_SMALL)

    # user_entry = EntryWithPlaceholder(f3, "Enter Image File Name")
    # pass_entry = EntryWithPlaceholder(f4, "Enter Video File Name")
        
    # user_entry.grid(ipady = 10,ipadx = 20 ,pady= 10,padx=10)
    # pass_entry.grid(ipady = 10,ipadx = 20 ,pady= 10,padx=10)
    
    project.grid_rowconfigure(0, weight=1)
    project.grid_columnconfigure(0, weight=1)

    # input_box = Label(project,text ="Nagpur City reports @ 30 november 2022 ")#,bg = "black" ,fg = "white",padx = 5,pady = 5,font = #("comicsansms", 14 , "bold")"comicsansms 15" , borderwidth= 2
    # input_box.grid(row = 1)#fill= "x",padx = 5,pady = 5



    project.mainloop()

