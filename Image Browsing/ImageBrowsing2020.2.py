from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as tmsg
import os
os.chdir(r"C:\Users\Admin\PycharmProjects\BITshine\gallery")
windwo=Tk()
windwo.title("Image")
windwo.geometry("600x500")
windwo.config(background="#c4d6ff")

def list_file():
    global lst_box
    for i in os.listdir():
        if i.endswith(".png") or i.endswith(".ico") or i.endswith(".jpg") or i.endswith(".jfif") :
            lst_box.insert(ACTIVE,f"{i}")


def open_img():
    global file,real_img2
    file=askopenfilename(defaultextension='*.png',filetypes=[("All File","*.*")])
    img2 = Image.open(file)
    resized2 = img2.resize((1027, 760), Image.ANTIALIAS)
    real_img2 = ImageTk.PhotoImage(resized2)
    #Label(windwo, image=real_img2).pack()

def set_img():
    global file,img_lbl,real_img2
    img2 = Image.open(combo_img.get())
    resized2 = img2.resize((1027, 760), Image.ANTIALIAS)
    real_img2 = ImageTk.PhotoImage(resized2)
    if  file==None and combo_img.get()=="":
        tmsg.showwarning("Image","You are not open any images")

    else:
        img_lbl=Label(windwo,image=real_img2)
        img_lbl.pack()

def delete_img():
    global img_lbl
    img_lbl.destroy()

def select():
    print(combo_img.get())

def change_path():
    global img_list
    img_list=[]
    if path_var.get()=="":
        tmsg.showwarning("Path","Please Enter proper path")
    else:
        os.chdir(path_var.get())
        for i in os.listdir():
            if i.endswith(".png") or i.endswith(".ico") or i.endswith(".jpg") or i.endswith(".jfif"):
                img_list.append(i)
        combo_img["values"] = img_list
        combo_img.current(0)

def picasa_img():
    img2 = Image.open(combo_img.get())
    img2.rotate(0).show()
#Setting images
frame2=Frame(windwo)
frame2.pack(side=TOP)
#Setting Labels
file=None
frame1=Frame(windwo)
frame1.pack(side=BOTTOM)
#Creating ComboBox
img_list=[]
for i in os.listdir():
    if i.endswith(".png") or i.endswith(".jpg") or i.endswith(".ico") or i.endswith(".png"):
        img_list.append(i)
        pass


frame3=Frame(windwo)
frame3.pack(side=TOP)
Label(frame3,text="Enter Path",font="Times 12").pack(side=LEFT)

path_var=StringVar()
path=Entry(frame3,font="Times 12 bold",textvariable=path_var)
path.pack(side=LEFT)

#Creating changing path button
path_btn=Button(frame3,text="Change Path" ,command=change_path,bg="#00ffee")
path_btn.pack(side=LEFT,padx=10)

combo_var=IntVar()
combo_img=ttk.Combobox(frame3,width=23,font="Times 12 ")
combo_img.pack()
combo_img["values"]=img_list
combo_img.current(0)

#Creation open button

open_btn=Button(frame1,text="Open",command=open_img,bg="#00ffee")
open_btn.pack(side=LEFT,padx=4)

#Creating set button
set_btn=Button(frame1,text="Set Open Image",bg="#00ffee",command=set_img)
set_btn.pack(side=LEFT,padx=4)

picasa=Button(frame1,text="Picasa 3",bg="#00ffee",command=picasa_img)
picasa.pack(side=LEFT,padx=5)
#Creating delete button
delete_btn=Button(frame1,text="Delete",command=delete_img,bg="#00ffee")
delete_btn.pack(side=LEFT)
windwo.mainloop()
