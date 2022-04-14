from tkinter import *
from tkinter import ttk,font
from tkinter.font import Font
import tkinter.colorchooser as tcc

window=Tk()
window.geometry("644x444")
window.title("Fonts")

#def fonts(event):
    #global style
    #style=combo_var.get()
   # label.config(font=combo_var.get())
    #label.update()
    #print(combo_var.get())

def color(event):
    clr=tcc.askcolor()
    label.config(fg=clr[1])

#def sizef(event):
#    global styy
 #   siz=int(combo_sizevar.get())
  #  label.config(font=f"f{styy} {siz} italic")

#def weightt(event):
 #   global weight_font
   # weight_font=radio_var.get()
  #  label.config(font=f"f{styy} 18 {weight_font}")

def style(evemn):
    global styy,siz,weight_font
    global no
    label.config(font=f"{combo_var.get()} {int(combo_sizevar.get())} {weight_styles[radio_var.get()]}")

#Ending the defining the function
styy="lucida"
siz=56
weight_font="italic"
#style=Font(size=12,weight="bold",slant="italic",underline=0)
label=Label(window,text="Choose the your Favourate font",font=f"f{styy} 12 italic")
label.pack()

#Accessing all the fonts
fonts_name=list(font.families())

#Creating combobox of the fonts
frame1=Frame(window)
frame1.pack()
combo_name=Label(frame1,text="Font Style")
combo_name.pack(side=LEFT)

combo_var=StringVar()
combo=ttk.Combobox(frame1,width=23,textvariable=combo_var)
combo.pack(side=LEFT,padx=12,pady=5)
combo["values"]=fonts_name
combo.current(0)

btn=Button(frame1,text="Apply Font Style")
btn.pack(side=LEFT,padx=12)
btn.bind("<Button-1>",style)
#Creating size combobox
frame2=Frame(window)
frame2.pack()

size_name=Label(frame2,text="Size")
size_name.pack(side=LEFT)

combo_sizevar=StringVar()
combo_size=ttk.Combobox(frame2,textvariable=combo_sizevar)
combo_size.pack(side=LEFT,padx=12,pady=2)

btn=Button(frame2,text="Apply Size")
btn.pack(side=LEFT,padx=12)
btn.bind("<Button-1>",style)

numbers=[]
for i in range(1,10001):
    numbers.append(i)
combo_size["values"]=numbers
combo_size.current(0)
#Creating Radio Button
frame3=Frame(window)
frame3.pack()
radio_var=IntVar()
weight_styles=["bold","italic","underline"]
no=0
for i in weight_styles:
    radio_btn=Radiobutton(frame3,text=f"{i}",value=no,variable=radio_var)
    radio_btn.pack(side=LEFT)
    no=no+1
btn1=Button(frame3,text="Apply")
btn1.pack(padx=12)
btn1.bind("<Button-1>",style)
#Creating color
btn=Button(window,text="Choose Color")
btn.pack()
btn.bind("<Button-1>",color)



window.mainloop()
