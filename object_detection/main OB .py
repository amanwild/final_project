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
import time                   
import matplotlib.pyplot as plt
import cvzone                 
from gtts import gTTS  
from io import BytesIO
import sys
from pptx.dml.color import RGBColor
from playsound import playsound
import tempfile
import pyttsx3

##################################################IT USED FOR BASIC PROCCESS ###################################################################

RGBColor(0xFF, 0x00, 0x00) 
colour_dict={'Blue': '0xff, 0, 0','Green':'0x00, 0xFF, 0x00','White':'0xFF, 0xFF, 0xFF','Sky_blue':'0xff, 0xff, 0x00','Pink':'0xFF,0x16,0xF4'}

lst = ['Blue','Green','White','Sky_blue','Pink']
    
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = "frozen_inference_graph.pb"


net = cv2.dnn_DetectionModel(weightsPath, configPath)

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
##################################################IT USED FOR color PROCCESSING ###################################################################
def select_color():
    #IT IS FOR RGB COLOR SELECTION
    global i ,Color
    i=int(var.get())
    Color = RGBColor(*map(lambda v : int(v, 16), colour_dict[(lst[i])].split(',')))
    
##################################################IT USED FOR IMAGE PROCCESSING ###################################################################
def show_img():
    
    
    #FOR FILE NAME SELECTION
    file = filedialog.askopenfilename(defaultextension=".txt",filetypes= [("All Files","*.*"),("Text Document","*.txt")])  

    imges = cv2.imread(file)      
   
    if imges is None: #IT RETURN FUNCTION IF PROCCESSING FILE IS EMPTY
        none()
        
    if imges.shape[0]>1000:
        f_size = 4
        f_bold = 5
        box=50
        fixed_height = 3070
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    elif 1000>imges.shape[0]>690:
        f_size = 2
        f_bold = 3
        box=30
        fixed_height = 3070
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    elif 690>imges.shape[0]>550:
        f_size = 1
        f_bold = 2
        box=5
        fixed_height = 10000
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    elif 550>imges.shape[0]>250:
        f_size = 1
        f_bold = 2
        box=10
        fixed_height = 7000
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    else :        
        f_size = .5
        f_bold = 1
        box=5
        fixed_height = 10000
        font = cv2.FONT_HERSHEY_TRIPLEX 
        
    classIds, confs, bbox = net.detect(imges,confThreshold ,nmsThreshold )
    print(classIds,confs)
    label_list = " "
    if len(classIds) > 0:
        f = pyttsx3.init()
        if len(confs) > 0:       
            for classIds,confs,boxes in zip(classIds.flatten(), confs.flatten(), bbox):
                cvzone.cornerRect(imges, boxes)
                cv2.putText(imges,f'{classNames[classIds-1].upper()} {round(confs*100,2)}',(boxes[0]+box,boxes[1]+box),
                    font,f_size,
                    Color,f_bold)
                label_list +=(" " +(classNames[classIds-1]))

                
                
                
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
    else:
        none_detection()
        
##################################################IT USED FOR VIDEO PROCCESSING ###################################################################

def show_vdo():
    file = filedialog.askopenfilename(defaultextension=".txt",filetypes= [("All Files","*.*"),("Text Document","*.txt")]) 
    cap = cv2.VideoCapture(file)
    cap.set(3, 640)
    cap.set(4, 480)

    while (True):
        if file is None :
            none()
            break
        success, frame = cap.read()
        classIds, confs, bbox = net.detect(frame, confThreshold, nmsThreshold)
        
        try:
            for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
                cvzone.cornerRect(frame, box)
                cv2.putText(frame,f'{classNames[classId-1].upper()} {round(conf*100,2)}',(box[0]+10,box[1]+30),font,f_size,Color,f_bold)    
        except:
            print('...')
        cv2.namedWindow("Object Detection in Video in Image (Press q to EXIT)", cv2.WINDOW_NORMAL)   
        cv2.imshow("Object Detection in Video in Image (Press q to EXIT)", frame)             

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 

    cap.release()
    cv2.destroyAllWindows()
##################################################IT USED FOR Web cam PROCCESSING #############################################################

def web_c(pass_entry):
    vdo_path = pass_entry
    cap = cv2.VideoCapture(vdo_path)
    cap.set(3, 1280)
    cap.set(4, 720)
    cap.set(10, 150)

    while (True):
        success, frame = cap.read()
        classIds, confs, bbox = net.detect(frame, confThreshold, nmsThreshold)
        try:
            for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):#bounding boxes
                cvzone.cornerRect(frame, box)
                cv2.putText(frame,f'{classNames[classId-1].upper()} {round(conf*100,2)}',(box[0]+10,box[1]+30),font,f_size,Color,f_bold)    
        except:
            print('...')
        cv2.namedWindow("Object Detection in real time (Press q to EXIT)", cv2.WINDOW_NORMAL)   
        cv2.imshow("Object Detection in real time (Press q to EXIT)", frame)             
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break 
    cap.release()
    cv2.destroyAllWindows()
    
##################################################IT USED FOR IP cam PROCCESSING #############################################################

def ip_cam():
    cap = cv2.VideoCapture(0)
    address = "http://192.168.0.101:8080/video"
    cap.open(address)
    cap.set(3, 640)
    cap.set(4, 480)
    
    while (True):
        success, frame = cap.read()
        classIds, confs, bbox = net.detect(frame, confThreshold, nmsThreshold)
        try:
            for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
                cvzone.cornerRect(frame, box)
                cv2.putText(frame,f'{classNames[classId-1].upper()} {round(conf*100,2)}',(box[0]+10,box[1]+30),font,f_size,Color,f_bold)    
        except:
            print('...')
        # cv2.namedWindow("Object Detection in real time (Press q to EXIT)", cv2.WINDOW_NORMAL)   
        cv2.imshow("Object Detection in real time (Press q to EXIT)", frame)             
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break 
    cap.release()
    cv2.destroyAllWindows()
    
##################################################IT USED FOR BASIC PROCCESSING #############################################################
def none():
    showinfo("File Error", "Could not read the File Name. (file name may be Empty)\n"
             "Try Again")
def none_detection():
    showinfo("Detection Error", "Could not detect any Object\n"
             "Try Again")
def stop():
    cv2.destroyAllWindows()  
def web_cam():
    global pass_entry  
    pass_entry = 0
    print("hello")
    web_c(pass_entry)

    
    
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

