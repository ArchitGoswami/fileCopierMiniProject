import tkinter as tk
from tkinter import *

mywindow = tk.Tk()

mywindow.title("Python Tkinter")
mywindow.minsize(500,400)

def buttonPress():
    print("Button Pressed!!")

def textBox():
    print(textb.get())

def printInput():
    inp = textb.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)

#Label
label = tk.Label(mywindow, text="Label Text: ")
label.place(relx=0.4, rely=0.3, anchor=CENTER)


a = Button(text="Center Button")
a.place(relx=0.58, rely=0.3, anchor=CENTER)

 
#Textbox
textb = tk.Entry(mywindow,text="Entry")
textbutton = tk.Button(mywindow, text="Text Box", command = printInput)
textbutton.place(relx=0.5, rely=0.7, anchor=CENTER)

message ='Hi'

text_box = Text(
    height=5,
    width=20
)
text_box.pack(expand=True)
text_box.insert('end', message)
text_box.config(state='disabled')

lbl = tk.Label(mywindow, text = "")
lbl.pack()

mywindow.mainloop()

