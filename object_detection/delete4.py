import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
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
from setuptools import Command
from PIL import ImageTk, Image
from turtle import color, width
import cv2                     
import matplotlib.pyplot as plt
import cvzone                   
import sys
from pptx.dml.color import RGBColor

##################################################IT USED FOR BASIC PROCCESS ###################################################################

RGBColor(0xFF, 0x00, 0x00) 
colour_dict={'Blue': '0xff, 0, 0','Green':'0x00, 0xFF, 0x00','White':'0xFF, 0xFF, 0xFF','Sky_blue':'0xff, 0xff, 0x00','Pink':'0xFF,0x16,0xF4'}

lst = ['Blue','Green','White','Sky_blue','Pink']
    
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
            
classLabels = []
file_name = 'Labels.txt'
with open(file_name,'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')

            
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
Color =(0,255,0)#black name
f_size =3
f_bold =3
bg_color = '#5DADE2'
f_scale = 1
window_title = "Object Detection Project"

class App:
    def __init__(self, window, window_title,colour_dict,lst ,configPath,weightsPath,config_file, frozen_model ,net,model,classNames,confThreshold,nmsThreshold,font,Color,f_size,f_bold,f_scale,bg_color):
        self.window = window
        self.window.title(window_title)
        self.colour_dict = colour_dict
        self.model  = model 
        self.bg_color  = bg_color
        self.f_bold  = f_bold
        self.f_size  = f_size
        self.f_scale  = f_scale
        # self.Color  = Color
        self.font  = font
        self.nmsThreshold  = nmsThreshold
        self.confThreshold  = confThreshold
        self.classLabels  = classLabels
        self.classNames  = classNames 
        self.frozen_model  = frozen_model 
        self.config_file  = config_file 
        self.weightsPath  = weightsPath 
        self.configPath  = configPath 
        self.lst  = lst 
        
        self.video_source = filedialog.askopenfilename(defaultextension=".txt",filetypes= [("All Files","*.*"),("Text Document","*.txt")])  
        # open video source (by default this will try to open the computer webcam)
        # self.vid = MyVideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.vid  = PhotoImage(self.video_source)
        self.canvas = tkinter.Canvas(window, width = self.vid.wid, height = self.vid.hgt)
        self.canvas.pack()

        self.i = 0
        self.window.iconbitmap("Custom-Icon-Design-Mono-General-2-Search.ico")        
        self.window.geometry("500x600")
        self.window.minsize(400,200)
        self.window.configure(bg=bg_color )
        
        self.aman = tkinter.Label(window, text ="This is Aman Sahu , the Software Engineer" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
        self.aman.grid(row  = 0, column=0,sticky= N)
##################################################IT USED FOR FRAMING ###################################################################

        self.grids(self)
           
##################################################IT USED FOR BUTTONS ###################################################################
    
        self.command_buttons()        
        
##################################################IT USED FOR RADIO BUTTONS ###################################################################

        self.labels_()        
        self.window.mainloop()

# IT USED FOR FRAMING Function 
    def grids(self,window):    
        self.f0 = tkinter.Frame(self.window,bg = ('#CCCCFF'), borderwidth=3,relief=SUNKEN)
        self.f0.grid(row=0, column=0, sticky=" ",)
        self.f0.grid_columnconfigure(0, weight=1)    
        self.f1 = tkinter.Frame(self.f0,bg = "#BB8FCE", borderwidth=3)
        self.f1.grid(row = 0,column = 0,padx =15,pady= 25)
        self.f2 = tkinter.Frame(self.f0,bg = "#BB8FCE", borderwidth=3)
        self.f2.grid(row = 1,column = 0,padx =15,pady= 25)
        self.f3 = tkinter.Frame(self.f0,bg = "#BB8FCE", borderwidth=3,relief=GROOVE)
        self.f3.grid(row = 0,rowspan = 3,column = 1,padx =15,pady= 25)
        self.f4 = tkinter.Frame(self.f0,bg = "#BB8FCE", borderwidth=3)
        self.f4.grid(row = 3,padx =15,pady= 25)
        self.f5 = tkinter.Frame(self.f0,bg = "#BB8FCE", borderwidth=3)
        self.f5.grid(row=2,padx =15,pady= 25)
        self.f6 = tkinter.Frame(self.f0,bg = "#BB8FCE", borderwidth=3)
        self.f6.grid(row=3, column=1,padx =15,pady= 25)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
# IT USED FOR BUTTONS Function 
    def command_buttons(self):
        self.processing = 0
        self.process_img = Button(self.f1,text ="IMAGE",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font ="comicsansms 20 bold", command = self.show_img, )
        self.process_img.grid(padx = 5,pady = 5)
        self.process_vdo = Button(self.f2,text ="VIDEO",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font = "comicsansms 20 bold", command =self.show_vdo, )
        self.process_vdo.grid(padx = 5,pady = 5)    
        self.process_web_cam = Button(self.f4,text ="WEB CAM",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font ="comicsansms 20 bold", command =self.web_cam, ) 
        self.process_web_cam.grid(padx = 5,pady = 5,ipadx =0,ipady = 0)
        self.process_ip_cam = Button(self.f5,text ="IP CAM",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font ="comicsansms 20 bold", command =self.ip_cam, ) 
        self.process_ip_cam.grid(padx = 5,pady = 5,ipadx =0,ipady = 0)    
        self.process_stop = Button(self.f6,text ="Exit",bg = "#BB8FCE" ,fg = "red",font ="comicsansms 20 bold", command = self.stop, )
        self.process_stop.grid(padx = 5,pady = 5,ipadx = 0,ipady = 0)
        self.process_stop.bind('<Button-1>',quit)
# IT USED FOR RADIO BUTTONS Function 
    def labels_(self):
        self.amans = Label(self.f3,text ="Choose Label Color" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
        self.amans.pack()
        self.var = StringVar()
        self.var.set(0)    
        self.radio = Radiobutton(self.f3,text="Blue",bg = '#0000FF',font ="comicsansms 15 bold",variable=self.var,value=(0),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
        self.radio = Radiobutton(self.f3,text="Green",bg = '#00FF00',font ="comicsansms 15 bold",variable=self.var,value=(1),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
        self.radio = Radiobutton(self.f3,text="White",bg = '#FFFFFF',font ="comicsansms 15 bold",variable=self.var,value=(2),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
        self.radio = Radiobutton(self.f3,text="Aqua",bg = '#00FFFF',font ="comicsansms 15 bold",variable=self.var,value=(3),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
        self.radio = Radiobutton(self.f3,text="Pink",bg = '#FF00FF',font ="comicsansms 15 bold",variable=self.var,value=(4),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
        self.apply =Button(self.f3,text="Apply",padx= 10,command = self.option, bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font ="comicsansms 15 bold").pack(padx = 5,pady = 5,ipadx = 0,ipady = 0)      
# IT USED FOR BASIC PROCCESSING Function 
    def show_img(self):
        
            #IT IS FOR RGB COLOR SELECTION
       
        
        #FOR FILE NAME SELECTION
        self.file = filedialog.askopenfilename(defaultextension=".txt",filetypes= [("All Files","*.*"),("Text Document","*.txt")])  

        print("this is color: ",self.Color)
        print("this is color no.: ",(self.var.get()))
        
        self.imges = cv2.imread(self.file)      
        self.hgt = self.imges.shape[0]
        self.wid = self.imges.shape[1]
        print(self.hgt,self.wid)     
        
        if self.imges is None: #IT RETURN FUNCTION IF PROCCESSING FILE IS EMPTY
            self.none()
            
        if self.imges.shape[0]>1000:
            f_size = 4
            f_bold = 5
            box=50
            fixed_height = 3070
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        elif 1000>self.imges.shape[0]>690:
            f_size = 2
            f_bold = 3
            box=30
            fixed_height = 3070
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        elif 690>self.imges.shape[0]>550:
            f_size = 1
            f_bold = 2
            box=5
            fixed_height = 10000
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        elif 550>self.imges.shape[0]>250:
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
            
        classIds, confs, bbox = net.detect(self.imges,confThreshold ,nmsThreshold )
        print(classIds,confs)
        if len(classIds) > 0:
            if len(confs) > 0:       
                for classIds,confs,boxes in zip(classIds.flatten(), confs.flatten(), bbox):
                    cvzone.cornerRect(self.imges, boxes)
                    cv2.putText(self.imges,f'{classNames[classIds-1].upper()} {round(confs*100,2)}',(boxes[0]+box,boxes[1]+box),
                        font,f_size,
                        Color,f_bold)  
            #FOR WINDOW RESIZE                 
            height_percent = (fixed_height / float(self.imges.shape[1]))
            width_size = int((float(self.imges.shape[0]) * float(height_percent)))
            stretch_near = cv2.resize(self.imges, (width_size,fixed_height),interpolation = cv2.INTER_NEAREST)
            cv2.namedWindow("Display in Image", cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Display in Image',width_size,fixed_height)
            #WINDOW DISPLAY
            cv2.imshow("Display in Image",stretch_near )
            if cv2.waitKey(0)& 0xFF == ord('q'):
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
                cv2.destroyAllWindows()
        else:
            self.none_detection()
        
    def show_vdo(self):
        global i
        i=int(self.var.get())
        print(" i type is: ",type(i))
        Color = RGBColor(*map(lambda v : int(v, 16), colour_dict[(lst[i])].split(',')))
        file = filedialog.askopenfilename(defaultextension=".txt",filetypes= [("All Files","*.*"),("Text Document","*.txt")]) 
        cap = cv2.VideoCapture(file)
        cap.set(3, 640)
        cap.set(4, 480)

        while (True):
            if file is None :
                self.none()
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

    def web_c(self,pass_entry):
        print("web cam")
        self.vdo_path = pass_entry
        self.cap = cv2.VideoCapture(self.vdo_path)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        self.cap.set(10, 150)
        
        
        global i
        i=int(self.var.get())
        print(" i type is: ",type(i))
        Color = RGBColor(*map(lambda v : int(v, 16), colour_dict[(lst[i])].split(',')))
        while (True):
            success, frame = self.cap.read()
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
        self.cap.release()
        cv2.destroyAllWindows()
        
    ##################################################IT USED FOR IP cam PROCCESSING #############################################################

    def ip_cam(self):
        self.cap = cv2.VideoCapture(0)
        self.address = "http://192.168.0.104:8080/video"
        self.cap.open(self.address)
        self.cap.set(3, 640)
        self.cap.set(4, 480)
        global i
        self.i=int(self.var.get())
        print(" i type is: ",type(self.i))
        self.Color = RGBColor(*map(lambda v : int(v, 16), colour_dict[(lst[self.i])].split(',')))
        while (True):
            success, frame = self.cap.read()
            classIds, confs, bbox = net.detect(frame, confThreshold, nmsThreshold)
            try:
                for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
                    cvzone.cornerRect(frame, box)
                    cv2.putText(frame,f'{classNames[classId-1].upper()} {round(conf*100,2)}',(box[0]+10,box[1]+30),font,f_size,self.Color,f_bold)    
            except:
                print('...')
            cv2.namedWindow("Object Detection in real time (Press q to EXIT)", cv2.WINDOW_NORMAL)   
            cv2.imshow("Object Detection in real time (Press q to EXIT)", frame)             
            if cv2.waitKey(1) & 0xFF == ord('q') :
                break 
        self.cap.release()
        cv2.destroyAllWindows()
        
    def none(self):
        showinfo("File Error", "Could not read the File Name. (file name may be Empty)\n"
                "Try Again")
        
    def none_detection(self):
        showinfo("Detection Error", "Could not detect any Object\n"
                "Try Again")
        
    def stop(self):
        cv2.destroyAllWindows(self)  
        
    def web_cam(self):
        global pass_entry  
        self.pass_entry = 0
        print("hello")
        self.web_c(self.pass_entry)
        
    def option(self):
        global i
        self.i = self.var.get() 
        print("Color option seted succesfully!!!",self.i)
     
    


class MyVideoCapture:
    def __init__(self):
    #     # Open the video source
    #     self.vid = cv2.VideoCapture(video_source)
    #     if not self.vid.isOpened():
    #         raise ValueError("Unable to open video source", video_source)

        # # Get video source width and height
        # self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        # self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        pass
    
    def get_frame(self):
        # if self.vid.isOpened():
        #     ret, frame = self.vid.read()
        #     if ret:
        #         # Return a boolean success flag and the current frame converted to BGR
        #         return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        #     else:
        #         return (ret, None)
        # else:
        #     return (ret, None)
        pass

    # Release the video source when the object is destroyed
    def __del__(self):
        # if self.vid.isOpened():
        #     self.vid.release()
        pass

# Create a window and pass it to the Application object

# __name__ == "__main__"
# project = Tk()
# i = 0
# project.iconbitmap("Custom-Icon-Design-Mono-General-2-Search.ico")
# bg_color = '#5DADE2'
# project.geometry("500x600")
# project.minsize(400,200)
# project.configure(bg=bg_color )
# project.title("Object Detection Project")    
# aman = Label(text ="This is Aman Sahu , the Software Engineer" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
# aman.grid(row  = 0, column=0,sticky= N)
App(tkinter.Tk(), window_title,colour_dict,lst ,configPath,weightsPath,config_file, frozen_model ,net,model,classNames,confThreshold,nmsThreshold,font,Color,f_size,f_bold,f_scale,bg_color)