import sys, os, errno, winreg, psutil, time, pathlib
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from winreg import *
from os.path import join
from pathlib import Path

root = tk.Tk()

SHPATH = os.path.dirname(os.path.realpath(__file__))
DESKTOP = os.path.expanduser("~\Desktop\\")
COMPUTER = str(os.getenv('COMPUTERNAME'))
HOST = str(os.getenv('HOSTNAME'))
HEIGHT = 510
WIDTH = 900 # DONT FORGET TO CHANGE THE root.geometry

# Window Configuration
root.resizable(width=False, height=False)
root.title("Security Diagnostics Utility")
root.geometry('900x510') # This will need to be changed if the above HEIGHT and WIDTH variables change
root.wm_iconbitmap(SHPATH + '\images\icon.ico')

def output_text():
    output.insert(INSERT, stack())

# Background image
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
background = tk.Label(root)
background_image = Image.open(SHPATH + '\images\\bg.jpg')
background.background_image = ImageTk.PhotoImage(background_image)
background['image'] = background.background_image
background.place(relwidth=1, relheight=1)

text_frame = tk.Frame(background)
text_frame.pack(padx=40, pady=20)

scrollb = tk.Scrollbar(text_frame)
scrollb.pack(side = RIGHT, fill = Y)

output = tk.Text(text_frame, yscrollcommand=scrollb.set)
output.config(state="normal", width=870, font=("Arial", 10), wrap="word", padx=5)
output.insert(INSERT, "Welcome to the Security Diagnostics Utility\nThis tool is used to estimate potential issues with a current installation of AV software\nThis will generate an EICAR test detection in your environment. The tool may appear hung for a few seconds, however, this is just it running its processes and tests.\n\n")
output.pack()
scrollb.config(command=output.yview)

start_button = tk.Button(background)
start_button.config(text="Start Diagnostics", pady="10", padx="10", font=("Calibri", 13, "bold"), bg="#242424", fg="#ffffff", bd=0, command=output_text)
start_button.pack()

# When defining a rule to check, it must be passed into this stack to be output to the console
def stack():
    return("%s\n%s\n%s\n%s\n%s\n" % (rule1(),rule2(),rule3(),rule4(),rule5()))
    p1 = Process(target = rule1)
    p1.start()
    p2 = Process(target = rule2)
    p2.start()
    p3 = Process(target = rule3)
    p3.start()
    p4 = Process(target = rule4)
    p4.start()
    p5 = Process(target = rule5)
    p5.start()


##########################################################
##
##       This is the start of the rules scripts
##
##########################################################

def rule1():
    return("Computer Name: " + COMPUTER + "\nHost Name: " + HOST)
    
def checkIfMcShieldRunning():
    processName = "mcshield"
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def rule2():
    if checkIfMcShieldRunning():
        return('McShield is RUNNING')
    else:
        return('McShield is NOT RUNNING')

def rule3():
    cpu_use = str(psutil.cpu_percent())
    return("Total System CPU usage: " + cpu_use)


def rule4():
        path = DESKTOP
        name = 'eicar.txt'  # Name of text file coerced with +.txt

        try:
            file = open(join(path, name),'w')   # Trying to create a new file or open one
            file.write("X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*")
            file.close()
            return("Eicar written sucessfully")
            pass
        except:
            return('Something went wrong writing the eicar! You may need to run the tool again.')
            pass

def rule5():
    time.sleep(5)
    file = Path(DESKTOP + "\eicar.txt")
    if file.is_file():
        return("Eicar file was NOT deleted, possible On-Access Scanner conflict")
    else:
        return("Eicar file not found, this likely indicates that the AV scanner sucessfully detected and removed it.")
        

##########################################################
##
## Draw and create window
##
##########################################################
root.mainloop()