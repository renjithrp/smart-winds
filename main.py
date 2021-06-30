import tkinter as tk
from tkinter import * 
import config as c
import actions as act
from db import (
    update,
    fetch
)

def validateInput(v,obj):
    try:
        int(v) # check the value enterd is intiger 
        obj.config(highlightbackground="white")
        return 0
    except:
        obj.config(highlightbackground="red")
        return 1

def notify(message):
    Label(root, text=message, bg=c.BG_COLOR, font=c.LABEL_FONT).place(x=20, y=460)

# Get All input and radio butten values in a map
def getAllValues():
    val = {}
    err = 0
    val["spool_width"] = SpoolWidth.get() # Spool Widtth
    err = err + validateInput(val["spool_width"],SpoolWidth)

    val["spool_diaz"] = SpoolDiaz.get() # Spool Diaz
    err = err + validateInput(val["spool_diaz"],SpoolDiaz)

    val["wire_guage"] = WireGuage.get() # Wire Guage
    err = err + validateInput(val["wire_guage"],WireGuage)

    val["no_of_turns"] = NoOfTurns.get() # Number of Turns
    err = err + validateInput(val["no_of_turns"],NoOfTurns)

    val["int_position"] = IntPosition.get() # Int Position
    err = err + validateInput(val["int_position"],IntPosition)

    val["turns_count"] = TurnsCount.get() # Turns Count
    err = err + validateInput(val["turns_count"],TurnsCount)

    val["pos_reach"] = PosReach.get() # Pos Reach
    err = err + validateInput(val["pos_reach"],PosReach)

    val["rpm"] = Rpm.get() # RPM
    err = err + validateInput(val["rpm"],Rpm)

    val["mode"] = Mode.get() # Mode
    if err == 0:
        return val
    return None

def set_text(text,obj):
    obj.delete(0,END)
    obj.insert(0,text)
    return

# Forward buttton action 
def Forward():
    values = getAllValues()
    if values:
        act.Forward(values)
    else:
        print("Forward:  values error")


# Reverse buttton action 
def Reverse():
    values = getAllValues()
    if values:
        act.Reverse(values)
    else:
        print("Reverse: values error")


# Start buttton action
def Start():
    values = getAllValues()
    if values:
        act.Start(values)
    else:
        print("Start: values error")


# Start buttton action
def Stop():
    values = getAllValues()
    if values:
        act.Stop(values)
    else:
        print("Stop: values error")

# Pause buttton action
def Pause():
    values = getAllValues()
    if values:
        act.Pause(values)
    else:
        print("Pause: values error")

def Save():
    values = getAllValues()
    if values:
        res = update(values)
        if res == True:
            notify("Data successfully saved..")
            return
    notify("Error while saving data")

def Load():
    values = fetch()
    set_text(values["spool_width"],SpoolWidth)
    set_text(values["spool_diaz"],SpoolDiaz)
    set_text(values["wire_guage"],WireGuage)
    set_text(values["no_of_turns"],NoOfTurns)
    set_text(values["rpm"],Rpm)
    set_text(values["int_position"],IntPosition)
    set_text(values["turns_count"],TurnsCount)
    set_text(values["pos_reach"],PosReach)
    Mode.set(values["mode"])
    notify("Data successfully loaded..")

def createLabels(lables,x,y,padding):
  
    i = 0
    for text in lables:
        Label(root, text=text, bg=c.BG_COLOR, font=c.LABEL_FONT).place(x=x, y=(y + i))
        i = i + padding
    return

root = Tk()
Mode = tk.StringVar()
Mode.set(0) # Set default mode as Manual (for automatic change to 1)

root.geometry(c.WINDOW_SIZE)
root.configure(background=c.BG_COLOR)
root.title(c.HEADER_TEXT)

Label(root, text=c.HEADER_TEXT,  bg=c.BG_COLOR, fg="white", font="none 26").pack(side=TOP)

column1_labels = ["Spool Width","Spool Diaz","Wire Guage","No Of Turns","RPM"]
createLabels(column1_labels,15,85,60)

SpoolWidth=Entry(root)
SpoolWidth.place(height=30, width=50,x=100, y=80)

SpoolDiaz=Entry(root)
SpoolDiaz.place(height=30, width=50,x=100, y=140)

WireGuage=Entry(root)
WireGuage.place(height=30, width=50,x=100, y=200)

NoOfTurns=Entry(root)
NoOfTurns.place(height=30, width=50,x=100, y=260)

Rpm=Entry(root)
Rpm.place(height=30, width=50,x=100, y=320)

Label(root, text='Mode', bg=c.BG_COLOR, font=c.LABEL_FONT).place(x=200, y=85)

frame=Frame(root, width=0, height=0, bg=c.BG_COLOR)
frame.place(x=250, y=85)
ARBEES=[
('Manual', '0'), 
('Auto', '1'), 
]
for text, mode in ARBEES:
	Radiobutton(frame, text=text, variable=Mode, value=mode, bg=c.BG_COLOR, font=c.LABEL_FONT).pack(side='left', anchor = 'w')

column2_labels = ["Int Position","Turns Count","Pos Reach"]
createLabels(column2_labels,200,205,60)


IntPosition=Entry(root)
IntPosition.place(height=30, width=50,x=275, y=200)

TurnsCount=Entry(root)
TurnsCount.place(height=30, width=50,x=275, y=260)

PosReach=Entry(root)
PosReach.place(height=30, width=50,x=275, y=320)


# Direction Buttons
Label(root, padx = 25,pady = 10,text='Direction', bg=c.BG_COLOR, font=c.LABEL_FONT).place(x=485, y=60)

Button(root, padx = 25,pady = 10,text='Forward', bg=c.BUTTON_COLOR, font=c.LABEL_FONT, command=Forward).place(x=400, y=100)
Button(root, padx = 25,pady = 10,text='Reverse', bg=c.BUTTON_COLOR, font=c.LABEL_FONT, command=Reverse).place(x=550, y=100)

Button(root, padx = 35,pady = 10,text='Start', bg=c.BUTTON_COLOR, font=c.LABEL_FONT, command=Start).place(x=400, y=160)
Button(root,padx = 35,pady = 10, text='Stop', bg=c.BUTTON_COLOR, font=c.LABEL_FONT, command=Stop).place(x=550, y=160)

Button(root, padx = 35,pady = 10,text='Pause', bg=c.BUTTON_COLOR, font=c.LABEL_FONT, command=Pause).place(x=465, y=220)



# Save and load button 
Button(root, padx = 25,pady = 10,text='Save', bg=c.BUTTON_COLOR, font=c.LABEL_FONT, command=Save).place(x=50, y=400)

Button(root, padx = 25,pady = 10,text='Load', bg=c.BUTTON_COLOR, font=c.LABEL_FONT, command=Load).place(x=200, y=400)

root.mainloop()
