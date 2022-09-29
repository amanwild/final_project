from tkinter import *

project = Tk()
project.geometry("800x600")
project.title("testing program")

def sub():
    print("hello world ",use.get()," ",pas.get())

username = Label(project,text = "hello_world")
passsword = Label(project,text = "Goodbye_world")
# username.pack()
# passsword.pack()
username.grid()
passsword.grid()

userv = StringVar()
passv = StringVar()

user_entry = Entry(textvariable= userv)
pass_entry = Entry(textvariable= passv)

use = userv
pas = passv
user_entry.grid(row =0, column = 1)
pass_entry.grid(row =1, column = 1)

submit = Button(project, text="Submit" ,command= sub).grid()
# submit.grid()

project.mainloop()