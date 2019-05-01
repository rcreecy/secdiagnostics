import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
root = tk.Tk()

HEIGHT = 510
WIDTH = 900 # DONT FORGET TO CHANGE THE root.geometry

# Window Configuration
root.resizable(width=False, height=False)
root.title("Security Diagnostics Utility")
root.geometry('900x510') # This will need to be changed if the above HEIGHT and WIDTH variables change
root.wm_iconbitmap(r'C:\users\rcree\Documents\Python\Diagnoser\images\icon.ico')

def output_text():
    output.insert(INSERT, stack())

# Background image
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
background = tk.Label(root)
background_image = Image.open(r'C:\users\rcree\Documents\Python\Diagnoser\images\bg.jpg')
background.background_image = ImageTk.PhotoImage(background_image)
background['image'] = background.background_image
background.place(relwidth=1, relheight=1)

text_frame = tk.Frame(background)
text_frame.pack(padx=40, pady=20)

scrollb = tk.Scrollbar(text_frame)
scrollb.pack(side = RIGHT, fill = Y)

output = tk.Text(text_frame, yscrollcommand=scrollb.set)
output.config(state="normal", width=870)
output.insert(INSERT, "Welcome to the Security Diagnostics Utility\nThis tool is used to estimate potential issues with a current installation of AV software\n\n")
output.pack()
scrollb.config(command=output.yview)

start_button = tk.Button(background)
start_button.config(text="Start Diagnostics", pady="10", padx="10", font=("Calibri", 13, "bold"), bg="#242424", fg="#ffffff", bd=0, command=output_text)
start_button.pack()

# When defining a rule to check, it must be passed into this stack to be output to the console
def stack():
    return("%s\n%s\n" % (rule1(),rule2()))
    p1 = Process(target = rule1)
    p1.start()
    p2 = Process(target = rule2)
    p2.start()

##########################################################
##
##       This is the start of the rules scripts
##
##########################################################

def rule1():
    return("This is a test of rule1")

def rule2():
    return("This is a test of rule2")


##########################################################
##
## Draw and create window
##
##########################################################
root.mainloop()