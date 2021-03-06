#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Mar 14, 2019 01:02:38 PM IST  platform: Windows NT

'''

Copyright (c) 2019 Pranesh Kulkarni

'''

import sys
import tkinter
from tkinter import messagebox
import mysql.connector
import dbConnect
import mysql.connector
from dbConnect import DBConnect

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
    unknown_support.set_Tk_var()
    top = Toplevel1 (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    unknown_support.set_Tk_var()
    top = Toplevel1 (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def exits(self):
      msg=tkinter.messagebox.askyesno('etax-2019','Do You Want To Exit ?');
      if(msg):
        exit()


    def continues(self):
      a=str(self.txtid.get());
      b=str(self.txtname.get());
      c=str(self.txtmeter.get());
      d=str(self.txtward.get());
      e=str(self.txthousetax.get());
      f=str(self.txthealthtax.get());
      g=str(self.txtlighttax.get());
      h=str(self.txtwatertax.get());
      i=str(self.txttotal.get());
      

      database = DBConnect(host='localhost',user='root',password='Pass@123',database='etax2019')
      new_user = {'idnumber': a,'meternumber': c,'wardnumber': d,'name': b,'housetax': e,'healthtax': f,'lighttax': g,'watertax': h,'total': i}
      database.insert(new_user,'kalamwadiinfo')
      tkinter.messagebox.showinfo('etax-2019','Data was entered successfully')
      

    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font10 = "-family {Segoe Script} -size 12 -weight normal "  \
            "-slant italic -underline 0 -overstrike 0"
        font11 = "-family {Rockwell Extra Bold} -size 12 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font12 = "-family {Sakkal Majalla} -size 17 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI Semibold} -size 14 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font14 = "-family {Bookman Old Style} -size 17 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI Semibold} -size 12 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Britannic Bold} -size 48 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1538x878+-109+36")
        top.title("New Toplevel")
        top.configure(background="#ffff24")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.013, rely=0.023, height=81, width=156)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffff24")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#ff250d")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''eTAX''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.072, rely=0.103, height=31, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffff24")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#13c12a")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''working for you''')

        self.backbutton = tk.Button(top)
        self.backbutton.place(relx=0.033, rely=0.194, height=44, width=97)
        self.backbutton.configure(activebackground="#ececec")
        self.backbutton.configure(activeforeground="#000000")
        self.backbutton.configure(background="#120bd8")
        self.backbutton.configure(disabledforeground="#a3a3a3")
        self.backbutton.configure(font=font11)
        self.backbutton.configure(foreground="#fcffff")
        self.backbutton.configure(highlightbackground="#d9d9d9")
        self.backbutton.configure(highlightcolor="black")
        self.backbutton.configure(pady="0")
        self.backbutton.configure(text='''Back''')

        self.exit = tk.Button(top)
        self.exit.place(relx=0.033, rely=0.285, height=44, width=97)
        self.exit.configure(activebackground="#ececec")
        self.exit.configure(activeforeground="#000000")
        self.exit.configure(background="#120bd8")
        self.exit.configure(disabledforeground="#a3a3a3")
        self.exit.configure(font=font11)
        self.exit.configure(foreground="#fcffff")
        self.exit.configure(highlightbackground="#d9d9d9")
        self.exit.configure(highlightcolor="black")
        self.exit.configure(pady="0")
        self.exit.configure(command = self.exits, text='''Exit''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.013, rely=0.9, height=21, width=56)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffff24")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''etax-2019''')

        self.Label3_3 = tk.Label(top)
        self.Label3_3.place(relx=0.013, rely=0.923, height=21, width=34)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#ffff24")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(foreground="#000000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''v 1.0.2''')

        self.Label3_4 = tk.Label(top)
        self.Label3_4.place(relx=0.007, rely=0.968, height=21, width=134)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#ffff24")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(foreground="#000000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Working On Windows''')

        self.Label3_1 = tk.Label(top)
        self.Label3_1.place(relx=0.013, rely=0.945, height=21, width=164)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#ffff24")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Connected to MySQL server 8.0''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.293, rely=0.216, relheight=0.655
                , relwidth=0.452)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#68ff3b")
        self.Frame1.configure(width=695)

        self.txtward = tk.Entry(self.Frame1)
        self.txtward.place(relx=0.504, rely=0.243,height=30, relwidth=0.437)
        self.txtward.configure(background="white")
        self.txtward.configure(disabledforeground="#a3a3a3")
        self.txtward.configure(font="TkFixedFont")
        self.txtward.configure(foreground="#000000")
        self.txtward.configure(insertbackground="black")
        self.txtward.configure(width=304)

        self.txtname = tk.Entry(self.Frame1)
        self.txtname.place(relx=0.504, rely=0.157,height=30, relwidth=0.437)
        self.txtname.configure(background="white")
        self.txtname.configure(disabledforeground="#a3a3a3")
        self.txtname.configure(font="TkFixedFont")
        self.txtname.configure(foreground="#000000")
        self.txtname.configure(insertbackground="black")
        self.txtname.configure(width=304)

        self.txtmeter = tk.Entry(self.Frame1)
        self.txtmeter.place(relx=0.504, rely=0.33,height=30, relwidth=0.437)
        self.txtmeter.configure(background="white")
        self.txtmeter.configure(disabledforeground="#a3a3a3")
        self.txtmeter.configure(font="TkFixedFont")
        self.txtmeter.configure(foreground="#000000")
        self.txtmeter.configure(insertbackground="black")
        self.txtmeter.configure(width=304)

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.23, rely=0.07, height=37, width=107)
        self.Label5.configure(background="#68ff3b")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#4124b5")
        self.Label5.configure(text='''UID Number :''')
        self.Label5.configure(width=107)

        self.Label5_2 = tk.Label(self.Frame1)
        self.Label5_2.place(relx=0.216, rely=0.313, height=47, width=127)
        self.Label5_2.configure(activebackground="#f9f9f9")
        self.Label5_2.configure(activeforeground="black")
        self.Label5_2.configure(background="#68ff3b")
        self.Label5_2.configure(disabledforeground="#a3a3a3")
        self.Label5_2.configure(font=font12)
        self.Label5_2.configure(foreground="#4124b5")
        self.Label5_2.configure(highlightbackground="#d9d9d9")
        self.Label5_2.configure(highlightcolor="black")
        self.Label5_2.configure(text='''Meter Number :''')
        self.Label5_2.configure(width=127)

        self.Label5_3 = tk.Label(self.Frame1)
        self.Label5_3.place(relx=0.23, rely=0.243, height=37, width=117)
        self.Label5_3.configure(activebackground="#f9f9f9")
        self.Label5_3.configure(activeforeground="black")
        self.Label5_3.configure(background="#68ff3b")
        self.Label5_3.configure(disabledforeground="#a3a3a3")
        self.Label5_3.configure(font=font12)
        self.Label5_3.configure(foreground="#4124b5")
        self.Label5_3.configure(highlightbackground="#d9d9d9")
        self.Label5_3.configure(highlightcolor="black")
        self.Label5_3.configure(text='''Ward Number :''')
        self.Label5_3.configure(width=117)

        self.Label5_4 = tk.Label(self.Frame1)
        self.Label5_4.place(relx=0.245, rely=0.417, height=37, width=97)
        self.Label5_4.configure(activebackground="#f9f9f9")
        self.Label5_4.configure(activeforeground="black")
        self.Label5_4.configure(background="#68ff3b")
        self.Label5_4.configure(disabledforeground="#a3a3a3")
        self.Label5_4.configure(font=font12)
        self.Label5_4.configure(foreground="#4124b5")
        self.Label5_4.configure(highlightbackground="#d9d9d9")
        self.Label5_4.configure(highlightcolor="black")
        self.Label5_4.configure(text='''Housetax :''')
        self.Label5_4.configure(width=97)

        self.Label5_5 = tk.Label(self.Frame1)
        self.Label5_5.place(relx=0.23, rely=0.157, height=37, width=107)
        self.Label5_5.configure(activebackground="#f9f9f9")
        self.Label5_5.configure(activeforeground="black")
        self.Label5_5.configure(background="#68ff3b")
        self.Label5_5.configure(disabledforeground="#a3a3a3")
        self.Label5_5.configure(font=font12)
        self.Label5_5.configure(foreground="#4124b5")
        self.Label5_5.configure(highlightbackground="#d9d9d9")
        self.Label5_5.configure(highlightcolor="black")
        self.Label5_5.configure(text='''Name :''')
        self.Label5_5.configure(width=107)

        self.Label5_6 = tk.Label(self.Frame1)
        self.Label5_6.place(relx=0.23, rely=0.504, height=37, width=107)
        self.Label5_6.configure(activebackground="#f9f9f9")
        self.Label5_6.configure(activeforeground="black")
        self.Label5_6.configure(background="#68ff3b")
        self.Label5_6.configure(disabledforeground="#a3a3a3")
        self.Label5_6.configure(font=font12)
        self.Label5_6.configure(foreground="#4124b5")
        self.Label5_6.configure(highlightbackground="#d9d9d9")
        self.Label5_6.configure(highlightcolor="black")
        self.Label5_6.configure(text='''Healthtax :''')
        self.Label5_6.configure(width=107)

        self.Label5_7 = tk.Label(self.Frame1)
        self.Label5_7.place(relx=0.23, rely=0.574, height=47, width=107)
        self.Label5_7.configure(activebackground="#f9f9f9")
        self.Label5_7.configure(activeforeground="black")
        self.Label5_7.configure(background="#68ff3b")
        self.Label5_7.configure(disabledforeground="#a3a3a3")
        self.Label5_7.configure(font=font12)
        self.Label5_7.configure(foreground="#4124b5")
        self.Label5_7.configure(highlightbackground="#d9d9d9")
        self.Label5_7.configure(highlightcolor="black")
        self.Label5_7.configure(text='''Lighttax :''')
        self.Label5_7.configure(width=107)

        self.Label5_8 = tk.Label(self.Frame1)
        self.Label5_8.place(relx=0.23, rely=0.661, height=47, width=107)
        self.Label5_8.configure(activebackground="#f9f9f9")
        self.Label5_8.configure(activeforeground="black")
        self.Label5_8.configure(background="#68ff3b")
        self.Label5_8.configure(disabledforeground="#a3a3a3")
        self.Label5_8.configure(font=font12)
        self.Label5_8.configure(foreground="#4124b5")
        self.Label5_8.configure(highlightbackground="#d9d9d9")
        self.Label5_8.configure(highlightcolor="black")
        self.Label5_8.configure(text='''Watertax :''')
        self.Label5_8.configure(width=107)

        self.Label5_9 = tk.Label(self.Frame1)
        self.Label5_9.place(relx=0.23, rely=0.748, height=57, width=107)
        self.Label5_9.configure(activebackground="#f9f9f9")
        self.Label5_9.configure(activeforeground="black")
        self.Label5_9.configure(background="#68ff3b")
        self.Label5_9.configure(disabledforeground="#a3a3a3")
        self.Label5_9.configure(font=font12)
        self.Label5_9.configure(foreground="#4124b5")
        self.Label5_9.configure(highlightbackground="#d9d9d9")
        self.Label5_9.configure(highlightcolor="black")
        self.Label5_9.configure(text='''Total :''')
        self.Label5_9.configure(width=107)

        self.buttncontinue = tk.Button(self.Frame1)
        self.buttncontinue.place(relx=0.763, rely=0.887, height=42, width=115)
        self.buttncontinue.configure(activebackground="#ececec")
        self.buttncontinue.configure(activeforeground="#000000")
        self.buttncontinue.configure(background="#5a54ff")
        self.buttncontinue.configure(disabledforeground="#a3a3a3")
        self.buttncontinue.configure(font=font13)
        self.buttncontinue.configure(foreground="#fafffc")
        self.buttncontinue.configure(highlightbackground="#d9d9d9")
        self.buttncontinue.configure(highlightcolor="black")
        self.buttncontinue.configure(pady="0")
        self.buttncontinue.configure(command = self.continues, text='''CONTINUE''')
        self.buttncontinue.configure(width=115)

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.checkbox = ttk.Checkbutton(self.Frame1)
        self.checkbox.place(relx=0.216, rely=0.835, relwidth=0.706, relheight=0.0
                , height=21)
        self.checkbox.configure(variable=unknown_support.tch66)
        self.checkbox.configure(takefocus="")
        self.checkbox.configure(text='''All the data filled is correct I Wish To Continue''')
        self.checkbox.configure(width=491)

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.377, rely=0.057, height=101, width=444)
        self.Label4.configure(background="#ffff24")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#35a025")
        self.Label4.configure(text='''New Entry''')
        self.Label4.configure(width=444)

        self.txtid = tk.Entry(top)
        self.txtid.place(relx=0.52, rely=0.262,height=30, relwidth=0.198)
        self.txtid.configure(background="white")
        self.txtid.configure(disabledforeground="#a3a3a3")
        self.txtid.configure(font="TkFixedFont")
        self.txtid.configure(foreground="#000000")
        self.txtid.configure(insertbackground="black")
        self.txtid.configure(width=304)

        self.txtwatertax = tk.Entry(top)
        self.txtwatertax.place(relx=0.52, rely=0.661,height=30, relwidth=0.198)
        self.txtwatertax.configure(background="white")
        self.txtwatertax.configure(disabledforeground="#a3a3a3")
        self.txtwatertax.configure(font="TkFixedFont")
        self.txtwatertax.configure(foreground="#000000")
        self.txtwatertax.configure(insertbackground="black")
        self.txtwatertax.configure(width=304)

        self.txttotal = tk.Entry(top)
        self.txttotal.place(relx=0.52, rely=0.718,height=30, relwidth=0.198)
        self.txttotal.configure(background="white")
        self.txttotal.configure(disabledforeground="#a3a3a3")
        self.txttotal.configure(font="TkFixedFont")
        self.txttotal.configure(foreground="#000000")
        self.txttotal.configure(insertbackground="black")
        self.txttotal.configure(width=304)

        self.txthousetax = tk.Entry(top)
        self.txthousetax.place(relx=0.52, rely=0.49,height=30, relwidth=0.198)
        self.txthousetax.configure(background="white")
        self.txthousetax.configure(disabledforeground="#a3a3a3")
        self.txthousetax.configure(font="TkFixedFont")
        self.txthousetax.configure(foreground="#000000")
        self.txthousetax.configure(insertbackground="black")
        self.txthousetax.configure(width=304)

        self.txthealthtax = tk.Entry(top)
        self.txthealthtax.place(relx=0.52, rely=0.547, height=30, relwidth=0.198)

        self.txthealthtax.configure(background="white")
        self.txthealthtax.configure(disabledforeground="#a3a3a3")
        self.txthealthtax.configure(font="TkFixedFont")
        self.txthealthtax.configure(foreground="#000000")
        self.txthealthtax.configure(insertbackground="black")
        self.txthealthtax.configure(width=304)

        self.txtlighttax = tk.Entry(top)
        self.txtlighttax.place(relx=0.52, rely=0.604,height=30, relwidth=0.198)
        self.txtlighttax.configure(background="white")
        self.txtlighttax.configure(disabledforeground="#a3a3a3")
        self.txtlighttax.configure(font="TkFixedFont")
        self.txtlighttax.configure(foreground="#000000")
        self.txtlighttax.configure(insertbackground="black")
        self.txtlighttax.configure(width=304)

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.117, rely=0.023, height=81, width=156)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#ffff24")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font=font9)
        self.Label1_1.configure(foreground="#2212ff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''2019''')

        self.Label1_11 = tk.Label(top)
        self.Label1_11.place(relx=0.826, rely=0.182, height=81, width=246)
        self.Label1_11.configure(activebackground="#f9f9f9")
        self.Label1_11.configure(activeforeground="black")
        self.Label1_11.configure(background="#ffff24")
        self.Label1_11.configure(disabledforeground="#a3a3a3")
        self.Label1_11.configure(font=font14)
        self.Label1_11.configure(foreground="#268930")
        self.Label1_11.configure(highlightbackground="#d9d9d9")
        self.Label1_11.configure(highlightcolor="black")
        self.Label1_11.configure(text='''Village : Kalamwadi''')
        self.Label1_11.configure(width=246)

        self.Label1_12 = tk.Label(top)
        self.Label1_12.place(relx=0.826, rely=0.251, height=41, width=246)
        self.Label1_12.configure(activebackground="#f9f9f9")
        self.Label1_12.configure(activeforeground="black")
        self.Label1_12.configure(background="#ffff24")
        self.Label1_12.configure(disabledforeground="#a3a3a3")
        self.Label1_12.configure(font=font14)
        self.Label1_12.configure(foreground="#268930")
        self.Label1_12.configure(highlightbackground="#d9d9d9")
        self.Label1_12.configure(highlightcolor="black")
        self.Label1_12.configure(text='''Dist. : Sangli''')
        self.Label1_12.configure(width=246)

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.904, rely=0.125, height=27, width=78)
        self.Label6.configure(background="#ffff24")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font15)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Hi User !!!''')

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.904, rely=0.034, height=74, width=74)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self._img1 = tk.PhotoImage(file="./login3.png")
        self.Label7.configure(image=self._img1)
        self.Label7.configure(text='''Label''')
        self.Label7.configure(width=74)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.826, rely=0.171, relwidth=0.176)

        self.TSeparator1_13 = ttk.Separator(top)
        self.TSeparator1_13.place(relx=0.829, rely=0.33, relwidth=0.202)

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.026, rely=0.513, height=222, width=318)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self._img2 = tk.PhotoImage(file="./login1.png")
        self.Label8.configure(image=self._img2)
        self.Label8.configure(text='''Label''')

        self.Label9 = tk.Label(top)
        self.Label9.place(relx=0.891, rely=0.945, height=21, width=117)
        self.Label9.configure(background="#ffff24")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Server Status : Online''')

        self.Label9_15 = tk.Label(top)
        self.Label9_15.place(relx=0.884, rely=0.968, height=21, width=147)
        self.Label9_15.configure(activebackground="#f9f9f9")
        self.Label9_15.configure(activeforeground="black")
        self.Label9_15.configure(background="#ffff24")
        self.Label9_15.configure(disabledforeground="#a3a3a3")
        self.Label9_15.configure(foreground="#000000")
        self.Label9_15.configure(highlightbackground="#d9d9d9")
        self.Label9_15.configure(highlightcolor="black")
        self.Label9_15.configure(text='''Connected To Local Host''')
        self.Label9_15.configure(width=147)

if __name__ == '__main__':
    vp_start_gui()





