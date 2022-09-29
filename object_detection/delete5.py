from cProfile import label
from decimal import Rounded
from email.errors import MisplacedEnvelopeHeaderDefect
from logging import PlaceHolder
from tkinter import *
from tkinter import messagebox
from cgitb import text
from tkinter import filedialog
import os
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter.font import BOLD
from winsound import PlaySound
from setuptools import Command
from PIL import ImageTk, Image
from turtle import color, width
import cv2                     
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt
import cvzone                 
from pptx.dml.color import RGBColor
from playsound import playsound
import pyttsx3

##################################################IT USED FOR BASIC PROCCESS ###################################################################

RGBColor(0xFF, 0x00, 0x00) 
colour_dict={'Blue': '0xff, 0, 0','Green':'0x00, 0xFF, 0x00','White':'0xFF, 0xFF, 0xFF','Sky_blue':'0xff, 0xff, 0x00','Pink':'0xFF,0x16,0xF4'}

lst = ['Blue','Green','White','Sky_blue','Pink']
    
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = "frozen_inference_graph.pb"

Known_distance = 30  # Inches
Known_width = 5.7  # Inches
Distance_level = 0

net = cv2.dnn_DetectionModel(weightsPath, configPath)

net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)


classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().split('\n')
            
            
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

confThreshold= 0.55
nmsThreshold= 0.2
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
Color =(255,0,0)
f_size =3
f_bold =3
f_scale = 1

COLORS = [(255,0,0),(255,0,255),(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (0, 255, 255)
WHITE = (255, 255, 255)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 242)
GOLDEN = (32, 218, 165)
LIGHT_BLUE = (255, 9, 2)
PURPLE = (128, 0, 128)
CHOCOLATE = (30, 105, 210)
PINK = (147, 20, 255)
ORANGE = (0, 69, 255)
##################################################IT USED FOR color PROCCESSING ###################################################################
def select_color():
    #IT IS FOR RGB COLOR SELECTION
    global i ,Color
    i=int(var.get())
    Color = RGBColor(*map(lambda v : int(v, 16), colour_dict[(lst[i])].split(',')))
    
##################################################IT USED FOR Distance PROCCESSING ###################################################################
def FocalLength(measured_distance, real_width, width_in_rf_image):
    return (width_in_rf_image * measured_distance) / real_width

def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):
    return (real_face_width * Focal_Length) / face_width_in_frame
def object_detector(image):
    classes, scores, boxes = net.detect(image, confThreshold, nmsThreshold)
    # creating empty list to add objects data
    data_list =[]
    for (classid, score, box) in zip(classes, scores, boxes):
        # define color of each, object based on its class id 
        color= COLORS[int(classid) % len(COLORS)]
    

        # draw rectangle on and label on object
        cv.rectangle(image, box, color, 2)
        cv.putText(image, "hello", (box[0], box[1]-14), font, 0.5, color, 2)
    
        # getting the data 
        # 1: class name  2: object width in pixels, 3: position where have to draw text(distance)
        if classid ==0: # person class id 
            data_list.append([classNames[classid[0]], box[2], (box[0], box[1]-2)])
        elif classid ==67:
            data_list.append([classNames[classid[0]], box[2], (box[0], box[1]-2)])
        # if you want inclulde more classes then you have to simply add more [elif] statements here
        # returning list containing the object data. 
    return data_list
##################################################IT USED FOR IMAGE PROCCESSING ###################################################################
def show_img():
    
    
    file = filedialog.askopenfilename(defaultextension=".txt",filetypes= [("All Files","*.*"),("Text Document","*.txt")])  

    imges = cv2.imread(file)      
    f_size = 4
    f_bold = 5
    box=50
    fixed_height = 3070
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    
    classIds, confs, bbox = net.detect(imges,confThreshold ,nmsThreshold )
    print(classIds,confs)
    label_list = " "
    if len(classIds) > 0:
        f = pyttsx3.init()
        if len(confs) > 0:       
            data_list =[]
            for (classIds,confs,boxes) in zip(classIds.flatten(), confs.flatten(), bbox):
                
                cvzone.cornerRect(imges, boxes)
                cv2.putText(imges,f'{classNames[classIds-1].upper()} {round(confs*100,2)}',(boxes[0]+box,boxes[1]+box),
                    font,f_size,
                    Color,f_bold)
                
                label_list +=(" " +(classNames[classIds-1]))
                if classIds ==0: # person class id 
                    data_list.append([classNames[classIds[0]], box[2], (box[0], box[1]-2)])
                elif classIds ==67:
                    data_list.append([classNames[classIds[0]], box[2], (box[0], box[1]-2)])
            return data_list
            
                
                
                
        print(data_list,"data list")
        print(label_list)
        f.say(label_list)
        f.runAndWait()
        f.stop()
        #FOR WINDOW RESIZE                 
        height_percent = (fixed_height / float(imges.shape[1]))
        width_size = int((float(imges.shape[0]) * float(height_percent)))
        stretch_near = cv2.resize(imges, (width_size,fixed_height),interpolation = cv2.INTER_NEAREST)
        cv2.namedWindow("Display in Image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Display in Image',width_size,fixed_height)
        #WINDOW DISPLAY
        cv2.imshow("Display in Image",stretch_near )
        
        
        
        if cv2.waitKey(0)& 0xFF == ord('q'):
            # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
            cv2.destroyAllWindows()

###################################IT USED FOR MAIN FUNCTION INITIALIZATION PROCCESSING ###################################################################

__name__ == "__main__"
project = Tk()
i = 0
project.iconbitmap("Custom-Icon-Design-Mono-General-2-Search.ico")
bg_color = '#5DADE2'
project.geometry("500x600")
project.minsize(400,200)
project.configure(bg=bg_color )
project.title("Object Detection Project")    
aman = Label(text ="ACCURATE OBJECT  DETECTION APPROCH BASED ON MACHINE LEARNIG" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
aman.grid(row  = 0, column=0,sticky= N)

ref_person = cv.imread('ReferenceImages/image14.png')
person_data = object_detector(ref_person)
person_width_in_rf = person_data[0][1]
print(f"Person width in pixels : {person_width_in_rf}")

    
##################################################IT USED FOR FRAMING ###################################################################

f0 = Frame(project,bg = ('#CCCCFF'), borderwidth=3,relief=SUNKEN)
f0.grid(row=0, column=0, sticky=" ",)
f0.grid_columnconfigure(0, weight=1)
f1 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
f1.grid(row = 0,column = 0,padx =15,pady= 25)
f2 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
f2.grid(row = 1,column = 0,padx =15,pady= 25)
f3 = Frame(f0,bg = "#BB8FCE", borderwidth=3,relief=GROOVE)
f3.grid(row = 0,rowspan = 3,column = 1,padx =15,pady= 25)
f4 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
f4.grid(row = 3,padx =15,pady= 25)
f5 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
f5.grid(row=2,padx =15,pady= 25)
f6 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
f6.grid(row=3, column=1,padx =15,pady= 25)
    
##################################################IT USED FOR BUTTONS ###################################################################

processing = 0
process_img = Button(f1,text ="IMAGE",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font ="comicsansms 20 bold", command = show_img, )
process_img.grid(padx = 5,pady = 5)
process_vdo = Button(f2,text ="VIDEO",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font = "comicsansms 20 bold", command =show_vdo, )
process_vdo.grid(padx = 5,pady = 5)    
process_web_cam = Button(f4,text ="WEB CAM",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font ="comicsansms 20 bold", command =web_cam, ) 
process_web_cam.grid(padx = 5,pady = 5,ipadx =0,ipady = 0)
process_ip_cam = Button(f5,text ="IP CAM",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font ="comicsansms 20 bold", command =ip_cam, ) 
process_ip_cam.grid(padx = 5,pady = 5,ipadx =0,ipady = 0)    
process_stop = Button(f6,text ="Exit",bg = "#BB8FCE" ,fg = "red",font ="comicsansms 20 bold", command = stop, )
process_stop.grid(padx = 5,pady = 5,ipadx = 0,ipady = 0)
process_stop.bind('<Button-1>',quit)

##################################################IT USED FOR RADIO BUTTONS ###################################################################

amans = Label(f3,text ="Choose Label Color" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
amans.pack()
var = StringVar()
var.set(0)    
radio = Radiobutton(f3,text="Blue",bg = '#0000FF',font ="comicsansms 15 bold",variable=var,value=(0),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
radio = Radiobutton(f3,text="Green",bg = '#00FF00',font ="comicsansms 15 bold",variable=var,value=(1),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
radio = Radiobutton(f3,text="White",bg = '#FFFFFF',font ="comicsansms 15 bold",variable=var,value=(2),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
radio = Radiobutton(f3,text="Aqua",bg = '#00FFFF',font ="comicsansms 15 bold",variable=var,value=(3),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
radio = Radiobutton(f3,text="Pink",bg = '#FF00FF',font ="comicsansms 15 bold",variable=var,value=(4),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
Button(f3,text="Apply",padx= 10,command = select_color, bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font ="comicsansms 15 bold").pack(padx = 5,pady = 5,ipadx = 0,ipady = 0)
project.grid_rowconfigure(0, weight=1)
project.grid_columnconfigure(0, weight=1)
project.mainloop()

