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
from pptx.dml.color import RGBColor
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
Color =(0,255,0)#black name
f_size =1
f_bold =2

f_scale = 1
# ########################################################################################################################################
# img = cv2.imread("IMG20171225114621.png")
# # img = cv2.imread('1653050880830.jpg',cv2.IMREAD_COLOR)
# classIds, confs, bbox = net.detect(img,confThreshold ,nmsThreshold )


# # cv2.cvtColor(img , cv2.COLOR_BGR2RGB) #rgb

# # ClassIndex , confidence, bbox = model.detect(img,confThreshold = 0.5 )
# # jjs\++\+||
# for classIds,confs,boxes in zip(classIds.flatten(), confs.flatten(), bbox):
#     cvzone.cornerRect(img, boxes)
#     cv2.putText(img,f'{classNames[classIds-1].upper()} {round(confs*100,2)}',
#                 (boxes[0]+10,boxes[1]+30),
#                 font,f_size,
#                 Color,f_bold)
        
# # for ClassInd , conf, boxes in zip (ClassIndex.flatten(), confidence.flatten(), bbox):                
# #     cv2.rectangle(img,boxes,(255,0,0),2)
    
# #     cv2.putText(img,classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40), font ,f_scale , Color,f_bold)
    
# # cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
# imgs = cv2.resize(img,(1550,840)) 
# cv2.imshow("hello",imgs )
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#####################################################################################################################################################
# cap = cv2.VideoCapture(0) # change to 1 if you are using external web cam
# cap.set(3, 640)
# cap.set(4, 480)

# while True:
#     success, frame = cap.read()
#     # img = me.get_frame_read().frame
#     classIds, confs, bbox = net.detect(frame, confThreshold, nmsThreshold)
    
#     try:
#         for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
#             cvzone.cornerRect(frame, box)
#             cv2.putText(frame,f'{classNames[classId-1].upper()} {round(conf*100,2)}',(box[0]+10,box[1]+30),font,f_size,Color,f_bold)    
#     except:
#         print('...')
        

#     cv2.imshow("Object Detection", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
 
######################################################################################################################
class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()
#for none file            
def none():
    showinfo("File Error", "Could not read the File Name. (file name may be Empty)\n"
             "Try Again")
#for none detection
def none_detection():
    showinfo("Detection Error", "Could not detect any Object\n"
             "Try Again")


def show_img():
    global i
    i=int(var.get())
    print(" i type is: ",type(i))
    Color = RGBColor(*map(lambda v : int(v, 16), colour_dict[(lst[i])].split(',')))
    print("this is rgb: ",Color,colour_dict[(lst[i])].split(','))
    
    file = filedialog.askopenfilename(defaultextension=".txt",filetypes= [("All Files","*.*"),("Text Document","*.txt")])  
    # img_path = user_entry.get()
    # global Color
    # code =(var.get())
    # Color =(var.get())
    
    print("this is color: ",Color)
    print("this is color: ",(var.get()))
    imges = cv2.imread(file)  
    
    hgt = imges.shape[0]
    wid = imges.shape[1]
    print(hgt,wid)     
    if imges is None:
        none()
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
        cv2.namedWindow("Display in Image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Display in Image',width_size,fixed_height)
        cv2.imshow("Display in Image",stretch_near )
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    else:
        none_detection()
    
    

def show_vdo():
    # vdo_path = pass_entry.get()
    global i
    i=int(var.get())
    print(" i type is: ",type(i))
    Color = RGBColor(*map(lambda v : int(v, 16), colour_dict[(lst[i])].split(',')))
    file = filedialog.askopenfilename(defaultextension=".txt",filetypes= [("All Files","*.*"),("Text Document","*.txt")]) 
    # cap = cv2.VideoCapture(vdo_path)
    cap = cv2.VideoCapture(file)
    cap.set(3, 640)
    cap.set(4, 480)

    while (True):
        if file is None :
            none()
            break
        success, frame = cap.read()
        # frame = cv2.resize(frame, (28, 28)) 
        # img = me.get_frame_read().frame
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

def web_c(pass_entry):
    vdo_path = pass_entry
    
    cap = cv2.VideoCapture(vdo_path)
    cap.set(3, 640)
    cap.set(4, 480)
    global i
    i=int(var.get())
    print(" i type is: ",type(i))
    Color = RGBColor(*map(lambda v : int(v, 16), colour_dict[(lst[i])].split(',')))
    while (True):
        success, frame = cap.read()
        # img = me.get_frame_read().frame
        classIds, confs, bbox = net.detect(frame, confThreshold, nmsThreshold)
        
        try:
            for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
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

def stop():

    processing = 1
    cv2.destroyAllWindows()  


def web_cam():
    global pass_entry  
    pass_entry = 0
    print("hello")
    web_c(pass_entry)
    

def option():
    global i
    i = var.get() 

if __name__ == "__main__": 
    
    
    project = Tk()
    i = 0
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
    f1.grid(row = 0,column = 0,padx =15,pady= 25)
    f2 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
    f2.grid(row = 1,column = 0,padx =15,pady= 25)
    f3 = Frame(f0,bg = "#BB8FCE", borderwidth=3,relief=GROOVE)
    f3.grid(row = 0,rowspan = 3,column = 1,padx =15,pady= 25)
    # f4 = Frame(f0,bg = "#BB8FCE", borderwidth=3,relief=GROOVE)
    # f4.grid(row = 1,column = 1,padx =25,pady= 25)
    f5 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
    f5.grid(row=2,padx =15,pady= 25)
    f6 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
    f6.grid(row=3, columnspan=2,padx =15,pady= 25)

    processing = 0
    process_img = Button(f1,text ="IMAGE",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE"
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 20 bold", command = show_img, )
    # process_img.grid(row = 0,column = 0)
    process_img.grid(padx = 5,pady = 5)#,anchor = "nw",padx = 5,pady = 5

    process_vdo = Button(f2,text ="VIDEO",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE"
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 20 bold", command =show_vdo, )
    # process_vdo.grid(row = 1,column = 2)
    process_vdo.grid(padx = 5,pady = 5)#, fill= "y",padx = 5,pady = 5
    
    process_web_cam = Button(f5,text ="WEB CAM",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE"
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 20 bold", command =web_cam, ) 
    # process_vdo.grid(row = 1,column = 2)
    process_web_cam.grid(padx = 5,pady = 5,ipadx =0,ipady = 0)#, fill= "y",padx = 5,pady = 5

    process_stop = Button(f6,text ="Exit",bg = "#BB8FCE" ,fg = "red"
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 20 bold", command = stop, )
    # process_vdo.grid(row = 1,column = 2)
    process_stop.grid(padx = 5,pady = 5,ipadx = 0,ipady = 0)#, fill= "y",padx = 5,pady = 25
    process_stop.bind('<Button-1>',quit)
   
    
    amans = Label(f3,text ="Choose Label Color" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
    amans.pack()
    var = StringVar()
    var.set(0)
#colour_dict={'Blue': '0xff, 0, 0','Green':'0x00, 0xFF, 0x00','White':'0xFF, 0xFF, 0xFF','Sky_blue':'0xff, 0xff, 0x00','Pink':'0xFF,0x16,0xF4'}

    radio = Radiobutton(f3,text="Blue",bg = '#0000FF'
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 15 bold",variable=var,value=(0),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
    radio = Radiobutton(f3,text="Green",bg = '#00FF00'
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 15 bold",variable=var,value=(1),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
    radio = Radiobutton(f3,text="White",bg = '#FFFFFF'
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 15 bold",variable=var,value=(2),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
    radio = Radiobutton(f3,text="Aqua",bg = '#00FFFF'
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 15 bold",variable=var,value=(3),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
    radio = Radiobutton(f3,text="Pink",bg = '#FF00FF'
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 15 bold",variable=var,value=(4),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
    Button(f3,text="Apply",padx= 10,command = option, bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE"
                ,font = #("comicsansms", 12 , "bold")
                "comicsansms 15 bold").pack(padx = 5,pady = 5,ipadx = 0,ipady = 0)
    
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

