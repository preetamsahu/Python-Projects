from tkinter import *
window=Tk()
window.geometry("600x200")

def resize():
    width_value=int(width_var.get())
    height_value=int(width_var.get())
    window.geometry(f"{width_value}x{height_value}")
width=Label(window,text="Enter the new Width of the window",font="comicsansms 15 bold",fg="red")
height=Label(window,text="Enter the new height of the window",font="comicsansms 15 bold",fg="red",pady=16)

width.grid(row=0,column=0)
height.grid(row=1,column=0)

width_var=StringVar()
height_var=StringVar()
width_entry=Entry(window,textvariable=width_var)
height_entry=Entry(window,textvariable=height_var)
width_entry.grid(row=0 , column=1)
height_entry.grid(row=1 , column=1)

Button(window,text="Resize Widow",command=resize).grid(row=3,column=1)

window.mainloop()
