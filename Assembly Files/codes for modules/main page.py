#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Mar 09, 2019 10:14:05 PM IST  platform: Windows NT

'''

Copyright (c) 2019 Pranesh Kulkarni

'''

import sys
import tkinter
from tkinter import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Main (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Main(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Main (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Main():
    global w
    w.destroy()
    w = None

def newdata1():             # fuction to add new entry
    window=Tk()
    window.title("welcome")
    lbl=Label(window,text="hello")
    lbl.pack()






def openworkspace1():       # functtion to fill up the data
    window=Tk()
    window.title("welcome")
    lbl=Label(window,text="hello")
    lbl.pack()






def viewentry1():          # function to view all the data
    window=Tk()
    window.title("welcome")
    lbl=Label(window,text="hello")
    lbl.pack()





def extra1():
    window=Tk()
    window.title("welcome")
    lbl=Label(window,text="hello")
    lbl.pack()
# in this module we have to do some private works only available for administrator also give loginid and password and make
# security patch that email the admin to warn about admin
# this is very imp part of application








class Main:
    def newdatas(self):
        root.destroy()
        newdata1()
    def openworkspaces(self):
        root.destroy()
        openworkspace1()
    def viewentrys(self):
        root.destroy()
        viewentry1()
    def extras(self):
        root.destroy()
        extra1()
    def exits(self):
        root.destroy()
        exit()
    def logouts(self):
        root.destroy()
        return
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font11 = "-family {Arial Black} -size 36 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family Georgia -size 12 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font16 = "-family Cambria -size 11 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font9 = "-family {Tw Cen MT Condensed Extra Bold} -size 22 "  \
            "-weight bold -slant roman -underline 0 -overstrike 0"

        top.geometry("925x601+294+152")
        top.title("Main")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=-0.043, rely=-0.15, relheight=1.186
                , relwidth=1.084)
        self.Canvas1.configure(background="#faff69")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief='ridge')
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=1003)

        self.Frame1 = tk.Frame(self.Canvas1)
        self.Frame1.place(relx=0.15, rely=0.323, relheight=0.259, relwidth=0.314)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#5b63d8")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=315)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.19, rely=0.162, height=40, width=196)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#5b63d8")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''New Data Entry''')

        self.newdata = tk.Button(self.Frame1)
        self.newdata.place(relx=0.381, rely=0.541, height=34, width=77)
        self.newdata.configure(activebackground="#ffffff")
        self.newdata.configure(activeforeground="#000000")
        self.newdata.configure(background="#ffffff")
        self.newdata.configure(disabledforeground="#a3a3a3")
        self.newdata.configure(foreground="#5b63d8")
        self.newdata.configure(highlightbackground="#d9d9d9")
        self.newdata.configure(highlightcolor="black")
        self.newdata.configure(pady="0")
        self.newdata.configure(relief='groove')
        self.newdata.configure(text='''ENTER''')
        self.newdata.configure(command=self.newdatas);

        self.Frame1_3 = tk.Frame(self.Canvas1)
        self.Frame1_3.place(relx=0.568, rely=0.323, relheight=0.259
                , relwidth=0.314)
        self.Frame1_3.configure(relief='groove')
        self.Frame1_3.configure(borderwidth="2")
        self.Frame1_3.configure(relief='groove')
        self.Frame1_3.configure(background="#5b63d8")
        self.Frame1_3.configure(highlightbackground="#d9d9d9")
        self.Frame1_3.configure(highlightcolor="black")
        self.Frame1_3.configure(width=315)

        self.Label1_4 = tk.Label(self.Frame1_3)
        self.Label1_4.place(relx=0.095, rely=0.162, height=40, width=250)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#5b63d8")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(font=font9)
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''Open The Workspace''')

        self.openworkspace = tk.Button(self.Frame1_3)
        self.openworkspace.place(relx=0.381, rely=0.541, height=34, width=77)
        self.openworkspace.configure(activebackground="#ffffff")
        self.openworkspace.configure(activeforeground="#000000")
        self.openworkspace.configure(background="#ffffff")
        self.openworkspace.configure(disabledforeground="#a3a3a3")
        self.openworkspace.configure(foreground="#5b63d8")
        self.openworkspace.configure(highlightbackground="#d9d9d9")
        self.openworkspace.configure(highlightcolor="black")
        self.openworkspace.configure(pady="0")
        self.openworkspace.configure(relief='groove')
        self.openworkspace.configure(text='''ENTER''')
        self.openworkspace.configure(command=self.openworkspaces);


        self.Frame1_6 = tk.Frame(self.Frame1_3)
        self.Frame1_6.place(relx=-0.349, rely=1.676, relheight=1.0, relwidth=1.0)

        self.Frame1_6.configure(relief='groove')
        self.Frame1_6.configure(borderwidth="2")
        self.Frame1_6.configure(relief='groove')
        self.Frame1_6.configure(background="#5b63d8")
        self.Frame1_6.configure(highlightbackground="#d9d9d9")
        self.Frame1_6.configure(highlightcolor="black")
        self.Frame1_6.configure(width=315)

        self.Label1_7 = tk.Label(self.Frame1_6)
        self.Label1_7.place(relx=0.19, rely=0.162, height=40, width=196)
        self.Label1_7.configure(activebackground="#f9f9f9")
        self.Label1_7.configure(activeforeground="black")
        self.Label1_7.configure(background="#5b63d8")
        self.Label1_7.configure(disabledforeground="#a3a3a3")
        self.Label1_7.configure(font=font9)
        self.Label1_7.configure(foreground="#ffffff")
        self.Label1_7.configure(highlightbackground="#d9d9d9")
        self.Label1_7.configure(highlightcolor="black")
        self.Label1_7.configure(text='''New Data Entry''')

        self.Frame1_12 = tk.Frame(self.Canvas1)
        self.Frame1_12.place(relx=0.15, rely=0.659, relheight=0.259
                , relwidth=0.314)
        self.Frame1_12.configure(relief='groove')
        self.Frame1_12.configure(borderwidth="2")
        self.Frame1_12.configure(relief='groove')
        self.Frame1_12.configure(background="#5b63d8")
        self.Frame1_12.configure(highlightbackground="#d9d9d9")
        self.Frame1_12.configure(highlightcolor="black")
        self.Frame1_12.configure(width=315)

        self.Label1_13 = tk.Label(self.Frame1_12)
        self.Label1_13.place(relx=0.19, rely=0.162, height=40, width=191)
        self.Label1_13.configure(activebackground="#f9f9f9")
        self.Label1_13.configure(activeforeground="black")
        self.Label1_13.configure(background="#5b63d8")
        self.Label1_13.configure(disabledforeground="#a3a3a3")
        self.Label1_13.configure(font=font9)
        self.Label1_13.configure(foreground="#ffffff")
        self.Label1_13.configure(highlightbackground="#d9d9d9")
        self.Label1_13.configure(highlightcolor="black")
        self.Label1_13.configure(text='''View All Entries''')

        self.viewentry = tk.Button(self.Frame1_12)
        self.viewentry.place(relx=0.381, rely=0.541, height=34, width=77)
        self.viewentry.configure(activebackground="#ffffff")
        self.viewentry.configure(activeforeground="#000000")
        self.viewentry.configure(background="#ffffff")
        self.viewentry.configure(disabledforeground="#a3a3a3")
        self.viewentry.configure(foreground="#5b63d8")
        self.viewentry.configure(highlightbackground="#d9d9d9")
        self.viewentry.configure(highlightcolor="black")
        self.viewentry.configure(pady="0")
        self.viewentry.configure(relief='groove')
        self.viewentry.configure(text='''ENTER''')
        self.viewentry.configure(command=self.viewentrys);


        self.Frame1_13 = tk.Frame(self.Canvas1)
        self.Frame1_13.place(relx=0.568, rely=0.659, relheight=0.259
                , relwidth=0.314)
        self.Frame1_13.configure(relief='groove')
        self.Frame1_13.configure(borderwidth="2")
        self.Frame1_13.configure(relief='groove')
        self.Frame1_13.configure(background="#5b63d8")
        self.Frame1_13.configure(highlightbackground="#d9d9d9")
        self.Frame1_13.configure(highlightcolor="black")
        self.Frame1_13.configure(width=315)

        self.Label1_14 = tk.Label(self.Frame1_13)
        self.Label1_14.place(relx=0.222, rely=0.162, height=40, width=175)
        self.Label1_14.configure(activebackground="#f9f9f9")
        self.Label1_14.configure(activeforeground="black")
        self.Label1_14.configure(background="#5b63d8")
        self.Label1_14.configure(disabledforeground="#a3a3a3")
        self.Label1_14.configure(font=font9)
        self.Label1_14.configure(foreground="#ffffff")
        self.Label1_14.configure(highlightbackground="#d9d9d9")
        self.Label1_14.configure(highlightcolor="black")
        self.Label1_14.configure(text='''Extra Features''')

        self.extra = tk.Button(self.Frame1_13)
        self.extra.place(relx=0.381, rely=0.541, height=34, width=77)
        self.extra.configure(activebackground="#ffffff")
        self.extra.configure(activeforeground="#000000")
        self.extra.configure(background="#ffffff")
        self.extra.configure(disabledforeground="#a3a3a3")
        self.extra.configure(foreground="#5b63d8")
        self.extra.configure(highlightbackground="#d9d9d9")
        self.extra.configure(highlightcolor="black")
        self.extra.configure(pady="0")
        self.extra.configure(relief='groove')
        self.extra.configure(text='''ENTER''')
        self.extra.configure(command=self.extras);


        self.Label2 = tk.Label(self.Canvas1)
        self.Label2.place(relx=0.349, rely=0.168, height=74, width=170)
        self.Label2.configure(background="#faff69")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#ff351f")
        self.Label2.configure(text='''eTAX''')
        self.Label2.configure(width=170)

        self.Label2_1 = tk.Label(self.Canvas1)
        self.Label2_1.place(relx=0.499, rely=0.168, height=74, width=170)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#faff69")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font11)
        self.Label2_1.configure(foreground="#201ad8")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''2019''')

        self.Label3 = tk.Label(self.Canvas1)
        self.Label3.place(relx=0.877, rely=0.154, height=44, width=44)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self._img1 = tk.PhotoImage(file="./login3.png")
        self.Label3.configure(image=self._img1)
        self.Label3.configure(text='''Label''')

        self.Label4 = tk.Label(self.Canvas1)
        self.Label4.place(relx=0.857, rely=0.224, height=24, width=96)
        self.Label4.configure(background="#faff69")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Hello user !!!''')

        self.Label5 = tk.Label(self.Canvas1)
        self.Label5.place(relx=0.05, rely=0.912, height=21, width=59)
        self.Label5.configure(background="#faff69")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''e-tax 2019''')
        self.Label5.configure(width=59)

        self.Label5_2 = tk.Label(self.Canvas1)
        self.Label5_2.place(relx=0.05, rely=0.94, height=21, width=59)
        self.Label5_2.configure(activebackground="#f9f9f9")
        self.Label5_2.configure(activeforeground="black")
        self.Label5_2.configure(anchor='w')
        self.Label5_2.configure(background="#faff69")
        self.Label5_2.configure(disabledforeground="#a3a3a3")
        self.Label5_2.configure(foreground="#000000")
        self.Label5_2.configure(highlightbackground="#d9d9d9")
        self.Label5_2.configure(highlightcolor="black")
        self.Label5_2.configure(text='''v 1.0.2''')

        self.logout = tk.Button(self.Canvas1)
        self.logout.place(relx=0.07, rely=0.154, height=34, width=77)
        self.logout.configure(activebackground="#ffffff")
        self.logout.configure(activeforeground="#000000")
        self.logout.configure(background="#5b63d8")
        self.logout.configure(disabledforeground="#a3a3a3")
        self.logout.configure(font=font16)
        self.logout.configure(foreground="#ffffff")
        self.logout.configure(highlightbackground="#d9d9d9")
        self.logout.configure(highlightcolor="black")
        self.logout.configure(pady="0")
        self.logout.configure(relief='groove')
        self.logout.configure(text='''LOG OUT''')
        self.logout.configure(command=self.logouts);


        self.exit = tk.Button(self.Canvas1)
        self.exit.place(relx=0.07, rely=0.224, height=34, width=77)
        self.exit.configure(activebackground="#ffffff")
        self.exit.configure(activeforeground="#000000")
        self.exit.configure(background="#5b63d8")
        self.exit.configure(cursor="fleur")
        self.exit.configure(disabledforeground="#a3a3a3")
        self.exit.configure(font=font16)
        self.exit.configure(foreground="#ffffff")
        self.exit.configure(highlightbackground="#d9d9d9")
        self.exit.configure(highlightcolor="black")
        self.exit.configure(pady="0")
        self.exit.configure(relief='groove')
        self.exit.configure(text='''EXIT''')
        self.exit.configure(command=self.exits);


if __name__ == '__main__':
    vp_start_gui()





