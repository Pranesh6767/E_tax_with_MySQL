'''

Copyright (c) 2019 Pranesh Kulkarni

'''
import sys
import tkinter
from tkinter import messagebox
import mysql.connector
import dbConnect
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

import connect_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    connect_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    connect_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def exits(self):
        msg=tkinter.messagebox.showinfo("etax-2019","Do You Want To Exit ?")
        if msg:
            exit()
    def viewnames(self):
        vill=str(self.villagename.get());

        if (vill == ""):
            msg=tkinter.messagebox.showerror("etax2019","Please Enter villagename")

        try :
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
        except :
            tkinter.messagebox.showerror('etax-2019','Failed to connect server, Please contact your administrator')
        
        mycursor=mydb.cursor()
        query = ("SELECT idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest FROM "+vill)
        mycursor.execute(query)
        for(idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest) in mycursor:
            s="{}   {}".format(idnumber, name)
            self.box1o1.insert(0,s)










    def viewalls(self):
        vill=str(self.villagename.get());
        if (vill == ""):
            msg=tkinter.messagebox.showerror("etax2019","Please Enter villagename")
        try :
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
        except :
            tkinter.messagebox.showerror('etax-2019','Failed to connect server, Please contact your administrator')
        mycursor=mydb.cursor()
        query = ("SELECT idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest FROM "+vill)
        mycursor.execute(query)
        for(idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest) in mycursor:
            s="{}        {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}".format(idnumber, meternumber, wardnumber, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest)
            self.box2o1.insert(0,s)
    def clearalls(self):
        self.box2o1.delete(0,tk.END)
        self.box1o1.delete(0,tk.END)

    def findss(self):
        vill=str(self.villagename.get());
        uid=str(self.Entry2.get());


        if (vill == ""):
            msg=tkinter.messagebox.showerror("etax2019","Please Enter villagename")


        try :
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
        except :
            tkinter.messagebox.showerror('etax-2019','Failed to connect server, Please contact your administrator')
        mycursor=mydb.cursor()
        query = ("SELECT idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest FROM %s WHERE idnumber= %s" %(vill,uid))
        mycursor.execute(query)
        for(idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest) in mycursor:
            s="{}        {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}".format(idnumber, meternumber, wardnumber, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest)
            self.box2o1.insert(0,s)

        try :
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
        except :
            tkinter.messagebox.showerror('etax-2019','Failed to connect server, Please contact your administrator')
        mycursor=mydb.cursor()
        query = ("SELECT idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest FROM %s WHERE idnumber= %s" %(vill,uid))
        mycursor.execute(query)
        for(idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest) in mycursor:
            s="{}   {}".format(idnumber, name)
            self.box1o1.insert(0,s)




    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font10 = "-family {Rockwell Extra Bold} -size 12 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {Rockwell Extra Bold} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font12 = "-family Rockwell -size 15 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family Rockwell -size 9 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font14 = "-family Rockwell -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family Rockwell -size 13 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font20 = "-family {Britannic Bold} -size 48 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font16 = "-family {Palatino Linotype} -size 11 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe Script} -size 12 -weight normal -slant"  \
            " italic -underline 0 -overstrike 0"
        font17 = "-family {Berlin Sans FB} -size 15"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1538x878+41+60")
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
        self.Label1.configure(font=font20)
        self.Label1.configure(foreground="#ff250d")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''eTAX''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.117, rely=0.023, height=81, width=156)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#ffff24")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font=font20)
        self.Label1_1.configure(foreground="#2212ff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''2019''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.072, rely=0.103, height=31, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffff24")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#13c12a")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''working for you''')

        self.backbutton = tk.Button(top)
        self.backbutton.place(relx=0.013, rely=0.159, height=44, width=97)
        self.backbutton.configure(activebackground="#ececec")
        self.backbutton.configure(activeforeground="#000000")
        self.backbutton.configure(background="#120bd8")
        self.backbutton.configure(disabledforeground="#a3a3a3")
        self.backbutton.configure(font=font10)
        self.backbutton.configure(foreground="#fcffff")
        self.backbutton.configure(highlightbackground="#d9d9d9")
        self.backbutton.configure(highlightcolor="black")
        self.backbutton.configure(pady="0")
        self.backbutton.configure(text='''Back''')

        self.exit = tk.Button(top)
        self.exit.place(relx=0.104, rely=0.159, height=44, width=97)
        self.exit.configure(activebackground="#ececec")
        self.exit.configure(activeforeground="#000000")
        self.exit.configure(background="#120bd8")
        self.exit.configure(disabledforeground="#a3a3a3")
        self.exit.configure(font=font10)
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

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.316, rely=0.034, height=68, width=651)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ffff24")
        self.Label4.configure(disabledforeground="#36911a")
        self.Label4.configure(font=font11)
        self.Label4.configure(foreground="#36911a")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''CONNECTING WORLD''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.793, rely=0.034, height=28, width=192)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#ffff24")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Village : Kalamwadi''')

        self.Label5_2 = tk.Label(top)
        self.Label5_2.place(relx=0.813, rely=0.068, height=28, width=172)
        self.Label5_2.configure(activebackground="#f9f9f9")
        self.Label5_2.configure(activeforeground="black")
        self.Label5_2.configure(background="#ffff24")
        self.Label5_2.configure(disabledforeground="#a3a3a3")
        self.Label5_2.configure(font=font12)
        self.Label5_2.configure(foreground="#000000")
        self.Label5_2.configure(highlightbackground="#d9d9d9")
        self.Label5_2.configure(highlightcolor="black")
        self.Label5_2.configure(text='''District : Sangli''')

        self.Label5_3 = tk.Label(top)
        self.Label5_3.place(relx=0.897, rely=0.923, height=28, width=172)
        self.Label5_3.configure(activebackground="#f9f9f9")
        self.Label5_3.configure(activeforeground="black")
        self.Label5_3.configure(background="#ffff24")
        self.Label5_3.configure(disabledforeground="#a3a3a3")
        self.Label5_3.configure(font=font13)
        self.Label5_3.configure(foreground="#000000")
        self.Label5_3.configure(highlightbackground="#d9d9d9")
        self.Label5_3.configure(highlightcolor="black")
        self.Label5_3.configure(text='''Server  Status : Online''')

        self.Label5_4 = tk.Label(top)
        self.Label5_4.place(relx=0.904, rely=0.945, height=28, width=172)
        self.Label5_4.configure(activebackground="#f9f9f9")
        self.Label5_4.configure(activeforeground="black")
        self.Label5_4.configure(background="#ffff24")
        self.Label5_4.configure(disabledforeground="#a3a3a3")
        self.Label5_4.configure(font=font13)
        self.Label5_4.configure(foreground="#000000")
        self.Label5_4.configure(highlightbackground="#d9d9d9")
        self.Label5_4.configure(highlightcolor="black")
        self.Label5_4.configure(text='''Host : localhost''')

        self.Label5_5 = tk.Label(top)
        self.Label5_5.place(relx=0.904, rely=0.968, height=28, width=172)
        self.Label5_5.configure(activebackground="#f9f9f9")
        self.Label5_5.configure(activeforeground="black")
        self.Label5_5.configure(background="#ffff24")
        self.Label5_5.configure(disabledforeground="#a3a3a3")
        self.Label5_5.configure(font=font13)
        self.Label5_5.configure(foreground="#000000")
        self.Label5_5.configure(highlightbackground="#d9d9d9")
        self.Label5_5.configure(highlightcolor="black")
        self.Label5_5.configure(text='''Port : 3306''')

        self.Label5_1 = tk.Label(top)
        self.Label5_1.place(relx=0.91, rely=0.091, height=28, width=172)
        self.Label5_1.configure(activebackground="#f9f9f9")
        self.Label5_1.configure(activeforeground="black")
        self.Label5_1.configure(background="#ffff24")
        self.Label5_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1.configure(font=font14)
        self.Label5_1.configure(foreground="#000000")
        self.Label5_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1.configure(highlightcolor="black")
        self.Label5_1.configure(text='''User : user''')

        self.box1o1 = ScrolledListBox(top)
        self.box1o1.place(relx=0.013, rely=0.285, relheight=0.598
                , relwidth=0.274)
        self.box1o1.configure(background="white")
        self.box1o1.configure(disabledforeground="#a3a3a3")
        self.box1o1.configure(font="TkFixedFont")
        self.box1o1.configure(foreground="black")
        self.box1o1.configure(highlightbackground="#d9d9d9")
        self.box1o1.configure(highlightcolor="#d9d9d9")
        self.box1o1.configure(selectbackground="#c4c4c4")
        self.box1o1.configure(selectforeground="black")
        self.box1o1.configure(width=10)

        self.box2o1 = ScrolledListBox(top)
        self.box2o1.place(relx=0.293, rely=0.285, relheight=0.598
                , relwidth=0.703)
        self.box2o1.configure(background="white")
        self.box2o1.configure(disabledforeground="#a3a3a3")
        self.box2o1.configure(font="TkFixedFont")
        self.box2o1.configure(foreground="black")
        self.box2o1.configure(highlightbackground="#d9d9d9")
        self.box2o1.configure(highlightcolor="#d9d9d9")
        self.box2o1.configure(selectbackground="#c4c4c4")
        self.box2o1.configure(selectforeground="black")
        self.box2o1.configure(width=10)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.923, rely=0.011, relheight=0.114)
        self.TSeparator1.configure(orient="vertical")

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.013, rely=0.137, relwidth=0.202)

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.013, rely=0.228, relwidth=0.975)

        self.TSeparator3_6 = ttk.Separator(top)
        self.TSeparator3_6.place(relx=0.013, rely=0.894, relwidth=0.975)

        self.viewbutton = tk.Button(top)
        self.viewbutton.place(relx=0.364, rely=0.923, height=33, width=148)
        self.viewbutton.configure(activebackground="#ececec")
        self.viewbutton.configure(activeforeground="#000000")
        self.viewbutton.configure(background="#2020d8")
        self.viewbutton.configure(disabledforeground="#a3a3a3")
        self.viewbutton.configure(font=font15)
        self.viewbutton.configure(foreground="#ffffff")
        self.viewbutton.configure(highlightbackground="#d9d9d9")
        self.viewbutton.configure(highlightcolor="black")
        self.viewbutton.configure(pady="0")
        self.viewbutton.configure(takefocus="0")
        self.viewbutton.configure(command = self.viewnames , text='''View all Names''')

        self.viewbutton_8 = tk.Button(top)
        self.viewbutton_8.place(relx=0.501, rely=0.923, height=33, width=148)
        self.viewbutton_8.configure(activebackground="#ececec")
        self.viewbutton_8.configure(activeforeground="#000000")
        self.viewbutton_8.configure(background="#2020d8")
        self.viewbutton_8.configure(disabledforeground="#a3a3a3")
        self.viewbutton_8.configure(font=font15)
        self.viewbutton_8.configure(foreground="#ffffff")
        self.viewbutton_8.configure(highlightbackground="#d9d9d9")
        self.viewbutton_8.configure(highlightcolor="black")
        self.viewbutton_8.configure(pady="0")
        self.viewbutton_8.configure(takefocus="0")
        self.viewbutton_8.configure(command = self.viewalls , text='''View all Data''')

        self.viewbutton_9 = tk.Button(top)
        self.viewbutton_9.place(relx=0.637, rely=0.923, height=33, width=108)
        self.viewbutton_9.configure(activebackground="#ececec")
        self.viewbutton_9.configure(activeforeground="#000000")
        self.viewbutton_9.configure(background="#2020d8")
        self.viewbutton_9.configure(disabledforeground="#a3a3a3")
        self.viewbutton_9.configure(font=font15)
        self.viewbutton_9.configure(foreground="#ffffff")
        self.viewbutton_9.configure(highlightbackground="#d9d9d9")
        self.viewbutton_9.configure(highlightcolor="black")
        self.viewbutton_9.configure(pady="0")
        self.viewbutton_9.configure(takefocus="0")
        self.viewbutton_9.configure(command = self.clearalls , text='''Clear all''')


        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.013, rely=0.251, height=26, width=78)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#ffff24")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font16)
        self.Label7.configure(foreground="#1220e0")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Id number''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label7_1 = tk.Label(top)
        self.Label7_1.place(relx=0.104, rely=0.251, height=26, width=78)
        self.Label7_1.configure(activebackground="#f9f9f9")
        self.Label7_1.configure(activeforeground="black")
        self.Label7_1.configure(background="#ffff24")
        self.Label7_1.configure(disabledforeground="#a3a3a3")
        self.Label7_1.configure(font=font16)
        self.Label7_1.configure(foreground="#1220e0")
        self.Label7_1.configure(highlightbackground="#d9d9d9")
        self.Label7_1.configure(highlightcolor="black")
        self.Label7_1.configure(text='''Name''')

        self.Label7_2 = tk.Label(top)
        self.Label7_2.place(relx=0.293, rely=0.251, height=26, width=68)
        self.Label7_2.configure(activebackground="#f9f9f9")
        self.Label7_2.configure(activeforeground="black")
        self.Label7_2.configure(background="#ffff24")
        self.Label7_2.configure(disabledforeground="#a3a3a3")
        self.Label7_2.configure(font=font16)
        self.Label7_2.configure(foreground="#1220e0")
        self.Label7_2.configure(highlightbackground="#d9d9d9")
        self.Label7_2.configure(highlightcolor="black")
        self.Label7_2.configure(text='''Id number''')

        self.Label7_3 = tk.Label(top)
        self.Label7_3.place(relx=0.345, rely=0.251, height=26, width=68)
        self.Label7_3.configure(activebackground="#f9f9f9")
        self.Label7_3.configure(activeforeground="black")
        self.Label7_3.configure(background="#ffff24")
        self.Label7_3.configure(disabledforeground="#a3a3a3")
        self.Label7_3.configure(font=font16)
        self.Label7_3.configure(foreground="#1220e0")
        self.Label7_3.configure(highlightbackground="#d9d9d9")
        self.Label7_3.configure(highlightcolor="black")
        self.Label7_3.configure(text='''Meter No.''')

        self.Label7_4 = tk.Label(top)
        self.Label7_4.place(relx=0.397, rely=0.251, height=26, width=68)
        self.Label7_4.configure(activebackground="#f9f9f9")
        self.Label7_4.configure(activeforeground="black")
        self.Label7_4.configure(background="#ffff24")
        self.Label7_4.configure(disabledforeground="#a3a3a3")
        self.Label7_4.configure(font=font16)
        self.Label7_4.configure(foreground="#1220e0")
        self.Label7_4.configure(highlightbackground="#d9d9d9")
        self.Label7_4.configure(highlightcolor="black")
        self.Label7_4.configure(text='''Ward No.''')

        self.Label7_1 = tk.Label(top)
        self.Label7_1.place(relx=0.449, rely=0.251, height=26, width=58)
        self.Label7_1.configure(activebackground="#f9f9f9")
        self.Label7_1.configure(activeforeground="black")
        self.Label7_1.configure(background="#ffff24")
        self.Label7_1.configure(disabledforeground="#a3a3a3")
        self.Label7_1.configure(font=font16)
        self.Label7_1.configure(foreground="#1220e0")
        self.Label7_1.configure(highlightbackground="#d9d9d9")
        self.Label7_1.configure(highlightcolor="black")
        self.Label7_1.configure(text='''Housetax''')

        self.Label7_2 = tk.Label(top)
        self.Label7_2.place(relx=0.494, rely=0.251, height=26, width=68)
        self.Label7_2.configure(activebackground="#f9f9f9")
        self.Label7_2.configure(activeforeground="black")
        self.Label7_2.configure(background="#ffff24")
        self.Label7_2.configure(disabledforeground="#a3a3a3")
        self.Label7_2.configure(font=font16)
        self.Label7_2.configure(foreground="#1220e0")
        self.Label7_2.configure(highlightbackground="#d9d9d9")
        self.Label7_2.configure(highlightcolor="black")
        self.Label7_2.configure(text='''Healthtax''')

        self.Label7_3 = tk.Label(top)
        self.Label7_3.place(relx=0.54, rely=0.251, height=26, width=58)
        self.Label7_3.configure(activebackground="#f9f9f9")
        self.Label7_3.configure(activeforeground="black")
        self.Label7_3.configure(background="#ffff24")
        self.Label7_3.configure(disabledforeground="#a3a3a3")
        self.Label7_3.configure(font=font16)
        self.Label7_3.configure(foreground="#1220e0")
        self.Label7_3.configure(highlightbackground="#d9d9d9")
        self.Label7_3.configure(highlightcolor="black")
        self.Label7_3.configure(text='''Lighttax''')

        self.Label7_5 = tk.Label(top)
        self.Label7_5.place(relx=0.579, rely=0.251, height=26, width=68)
        self.Label7_5.configure(activebackground="#f9f9f9")
        self.Label7_5.configure(activeforeground="black")
        self.Label7_5.configure(background="#ffff24")
        self.Label7_5.configure(disabledforeground="#a3a3a3")
        self.Label7_5.configure(font=font16)
        self.Label7_5.configure(foreground="#1220e0")
        self.Label7_5.configure(highlightbackground="#d9d9d9")
        self.Label7_5.configure(highlightcolor="black")
        self.Label7_5.configure(text='''Watertax''')

        self.Label7_5 = tk.Label(top)
        self.Label7_5.place(relx=0.624, rely=0.251, height=26, width=48)
        self.Label7_5.configure(activebackground="#f9f9f9")
        self.Label7_5.configure(activeforeground="black")
        self.Label7_5.configure(background="#ffff24")
        self.Label7_5.configure(disabledforeground="#a3a3a3")
        self.Label7_5.configure(font=font16)
        self.Label7_5.configure(foreground="#1220e0")
        self.Label7_5.configure(highlightbackground="#d9d9d9")
        self.Label7_5.configure(highlightcolor="black")
        self.Label7_5.configure(text='''Total''')

        self.Label7_5 = tk.Label(top)
        self.Label7_5.place(relx=0.663, rely=0.251, height=26, width=78)
        self.Label7_5.configure(activebackground="#f9f9f9")
        self.Label7_5.configure(activeforeground="black")
        self.Label7_5.configure(background="#ffff24")
        self.Label7_5.configure(disabledforeground="#a3a3a3")
        self.Label7_5.configure(font=font16)
        self.Label7_5.configure(foreground="#1220e0")
        self.Label7_5.configure(highlightbackground="#d9d9d9")
        self.Label7_5.configure(highlightcolor="black")
        self.Label7_5.configure(text='''Reciept No.''')

        self.Label7_6 = tk.Label(top)
        self.Label7_6.place(relx=0.722, rely=0.251, height=26, width=68)
        self.Label7_6.configure(activebackground="#f9f9f9")
        self.Label7_6.configure(activeforeground="black")
        self.Label7_6.configure(background="#ffff24")
        self.Label7_6.configure(disabledforeground="#a3a3a3")
        self.Label7_6.configure(font=font16)
        self.Label7_6.configure(foreground="#1220e0")
        self.Label7_6.configure(highlightbackground="#d9d9d9")
        self.Label7_6.configure(highlightcolor="black")
        self.Label7_6.configure(text='''Housetax''')
        self.Label7_6.configure(width=68)

        self.Label7_6 = tk.Label(top)
        self.Label7_6.place(relx=0.767, rely=0.251, height=26, width=68)
        self.Label7_6.configure(activebackground="#f9f9f9")
        self.Label7_6.configure(activeforeground="black")
        self.Label7_6.configure(background="#ffff24")
        self.Label7_6.configure(disabledforeground="#a3a3a3")
        self.Label7_6.configure(font=font16)
        self.Label7_6.configure(foreground="#1220e0")
        self.Label7_6.configure(highlightbackground="#d9d9d9")
        self.Label7_6.configure(highlightcolor="black")
        self.Label7_6.configure(text='''Lighttax''')

        self.Label7_6 = tk.Label(top)
        self.Label7_6.place(relx=0.813, rely=0.251, height=26, width=68)
        self.Label7_6.configure(activebackground="#f9f9f9")
        self.Label7_6.configure(activeforeground="black")
        self.Label7_6.configure(background="#ffff24")
        self.Label7_6.configure(disabledforeground="#a3a3a3")
        self.Label7_6.configure(font=font16)
        self.Label7_6.configure(foreground="#1220e0")
        self.Label7_6.configure(highlightbackground="#d9d9d9")
        self.Label7_6.configure(highlightcolor="black")
        self.Label7_6.configure(text='''Watertax''')

        self.Label7_6 = tk.Label(top)
        self.Label7_6.place(relx=0.904, rely=0.251, height=26, width=48)
        self.Label7_6.configure(activebackground="#f9f9f9")
        self.Label7_6.configure(activeforeground="black")
        self.Label7_6.configure(background="#ffff24")
        self.Label7_6.configure(disabledforeground="#a3a3a3")
        self.Label7_6.configure(font=font16)
        self.Label7_6.configure(foreground="#1220e0")
        self.Label7_6.configure(highlightbackground="#d9d9d9")
        self.Label7_6.configure(highlightcolor="black")
        self.Label7_6.configure(text='''Total''')

        self.Label7_3 = tk.Label(top)
        self.Label7_3.place(relx=0.858, rely=0.251, height=26, width=68)
        self.Label7_3.configure(activebackground="#f9f9f9")
        self.Label7_3.configure(activeforeground="black")
        self.Label7_3.configure(background="#ffff24")
        self.Label7_3.configure(disabledforeground="#a3a3a3")
        self.Label7_3.configure(font=font16)
        self.Label7_3.configure(foreground="#1220e0")
        self.Label7_3.configure(highlightbackground="#d9d9d9")
        self.Label7_3.configure(highlightcolor="black")
        self.Label7_3.configure(text='''Healthtax''')

        self.Label7_4 = tk.Label(top)
        self.Label7_4.place(relx=0.943, rely=0.251, height=26, width=48)
        self.Label7_4.configure(activebackground="#f9f9f9")
        self.Label7_4.configure(activeforeground="black")
        self.Label7_4.configure(background="#ffff24")
        self.Label7_4.configure(disabledforeground="#a3a3a3")
        self.Label7_4.configure(font=font16)
        self.Label7_4.configure(foreground="#1220e0")
        self.Label7_4.configure(highlightbackground="#d9d9d9")
        self.Label7_4.configure(highlightcolor="black")
        self.Label7_4.configure(text='''Rest''')

        self.Label7_5 = tk.Label(top)
        self.Label7_5.place(relx=0.806, rely=0.216, height=26, width=68)
        self.Label7_5.configure(activebackground="#f9f9f9")
        self.Label7_5.configure(activeforeground="black")
        self.Label7_5.configure(background="#ffff24")
        self.Label7_5.configure(disabledforeground="#a3a3a3")
        self.Label7_5.configure(font=font16)
        self.Label7_5.configure(foreground="#1220e0")
        self.Label7_5.configure(highlightbackground="#d9d9d9")
        self.Label7_5.configure(highlightcolor="black")
        self.Label7_5.configure(text='''Paid''')

        self.TSeparator4 = ttk.Separator(top)
        self.TSeparator4.place(relx=0.715, rely=0.228, relheight=0.057)
        self.TSeparator4.configure(orient="vertical")

        self.TSeparator4_6 = ttk.Separator(top)
        self.TSeparator4_6.place(relx=0.936, rely=0.228, relheight=0.057)
        self.TSeparator4_6.configure(orient="vertical")


        self.villagename = tk.Entry(top)
        self.villagename.place(relx=0.375, rely=0.179, height=20, relwidth=0.153)
        self.villagename.configure(background="white")
        self.villagename.configure(disabledforeground="#a3a3a3")
        self.villagename.configure(font="TkFixedFont")
        self.villagename.configure(foreground="#1b1391")
        self.villagename.configure(insertbackground="black")
        self.villagename.configure(width=244)

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.675, rely=0.179,height=20, relwidth=0.146)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=234)

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.269, rely=0.179, height=21, width=154)
        self.Label7.configure(background="#ffff24")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font17)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Village Name :''')
        self.Label7.configure(width=154)

        self.Label7_1 = tk.Label(top)
        self.Label7_1.place(relx=0.575, rely=0.179, height=21, width=154)
        self.Label7_1.configure(activebackground="#f9f9f9")
        self.Label7_1.configure(activeforeground="black")
        self.Label7_1.configure(background="#ffff24")
        self.Label7_1.configure(disabledforeground="#a3a3a3")
        self.Label7_1.configure(font="-family {Berlin Sans FB} -size 15")
        self.Label7_1.configure(foreground="#000000")
        self.Label7_1.configure(highlightbackground="#d9d9d9")
        self.Label7_1.configure(highlightcolor="black")
        self.Label7_1.configure(text='''UID Number  :''')
        self.Label7_1.configure(width=154)

        self.btn_find = tk.Button(top)
        self.btn_find.place(relx=0.856, rely=0.167, height=34, width=97)
        self.btn_find.configure(activebackground="#ececec")
        self.btn_find.configure(activeforeground="#000000")
        self.btn_find.configure(background="#ff330a")
        self.btn_find.configure(disabledforeground="#a3a3a3")
        self.btn_find.configure(font="-family {Rockwell Extra Bold} -size 12 -weight bold")
        self.btn_find.configure(foreground="#fcffff")
        self.btn_find.configure(highlightbackground="#d9d9d9")
        self.btn_find.configure(highlightcolor="black")
        self.btn_find.configure(pady="0")
        self.btn_find.configure(text='''FIND''')
        self.btn_find.configure(width=97,command=self.findss)


        """self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.949, rely=0.034, height=44, width=44)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self._img1 = tk.PhotoImage(file="./login3.png")
        self.Label6.configure(image=self._img1)
        self.Label6.configure(text='''Label''')"""

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





