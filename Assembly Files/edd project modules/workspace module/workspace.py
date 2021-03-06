import sys
import tkinter
from tkinter import messagebox
import mysql.connector
import dbConnect
import mysql.connector
from dbConnect import DBConnect
import time
import smtplib

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

import workspace_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    print ('prog_call = {}'.format(prog_call))
    prog_location = os.path.split(prog_call)[0]
    print ('prog_location = {}'.format(prog_location))
    sys.stdout.flush()
    root = tk.Tk()
    top = Toplevel1 (root)
    workspace_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    print ('prog_call = {}'.format(prog_call))
    prog_location = os.path.split(prog_call)[0]
    print ('prog_location = {}'.format(prog_location))
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    workspace_support.init(w, top, *args, **kwargs)
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

    def viewnames(self):
        try :
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
        except :
            tkinter.messagebox.showerror('etax-2019','Failed to connect server, Please contact your administrator')
        
        mycursor=mydb.cursor()
        query = ("SELECT idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total FROM kalamwadiinfo")
        mycursor.execute(query)
        for(idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total) in mycursor:
            s="{}   {}".format(idnumber, name)
            self.namebox.insert(0,s)


    def viewalls(self):
        try :
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
        except :
            tkinter.messagebox.showerror('etax-2019','Failed to connect server, Please contact your administrator')
        
        mycursor=mydb.cursor()
        query = ("SELECT idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total FROM kalamwadiinfo")
        mycursor.execute(query)
        for(idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total) in mycursor:
            s="{}     {}      {}      {}      {}      {}       {}     {}".format(idnumber, meternumber, wardnumber, housetax, healthtax, lighttax, watertax, total)
            self.taxbox.insert(0,s)


    def clear(self):
        self.namebox.delete(0,tk.END)
        self.taxbox.delete(0,tk.END)





    def submits(self):
        a=str(self.txt_idnumber.get());
        b=str(self.txt_name.get());
        c=str(self.txt_meternumber.get());
        d=str(self.txt_wardnumber.get());
        e=str(self.txt_house.get());
        f=str(self.txt_health.get());
        g=str(self.txt_light.get());
        h=str(self.txt_water.get());
        i=str(self.txt_total.get());
        j=str(self.txt_reciept.get());
        k=str(self.txt_housepaid.get());
        l=str(self.txt_healthpaid.get());
        m=str(self.txt_lightpaid.get());
        n=str(self.txt_waterpaid.get());
        o=str(self.txt_totalpaid.get());
        email=str(self.txt_findid_10.get());
        if (email==""):
            email="kulkarnipranesh1767@gmail.com"

        localtime=str(time.asctime(time.localtime(time.time())))


        t=int(i)
        u=int(o)
        p=str(t-u)
        print(p)

        if (a=="") or (b=="") or (c=="") or (d=="") or (e=="") or (f=="") or (g=="") or (h=="") or (i=="") or (j=="") or (k=="") or (l=="") or (m=="") or (n=="") or (o=="") :
            tkinter.messagebox.showerror("eTAX-2019","Kindly Fill All Details")
        else :
            database = DBConnect(host='localhost',user='root',password='Pass@123',database='etax2019')
            new_user = {'idnumber': a,'meternumber': c,'wardnumber': d,'name': b,'housetax': e,'healthtax': f,'lighttax': g,'watertax': h,'total': i,'reciptnumber':j,'housetaxpaid':k,'healthtaxpaid':l,'lighttaxpaid':m,'watertaxpaid':n,'totalpaid':o,'rest':p}
            database.insert(new_user,'kalamwadi')
            tkinter.messagebox.showinfo('etax-2019','Data entered to the database successfully')

            content1="-------------Grampanchayat Kalamwadi----------------\n\t\tTal. : Walava\n\t\tDist. : Sangli\n\tDate :"+localtime+"\n-----------Tax Collection 2019---------\nIncharge Officer : XYZ\nDetails :\n"
            content2="\nReciept Number :"+j+"\nName :"+b+"\nID Number :"+a+"\nMeter Number :"+c+"\nWard Number :"+d+"\nHouse Tax :"+e+"\nHealth Tax :"+f+"\nLight Tax :"+g+"\nWater Tax :"+h+"\nTotal Ammount of tax to be paid :"+i+"\nPaid House Tax :"+k+"\nPaid Health Tax :"+l+"\nPaid Light Tax :"+m+"\nPiad Water Tax :"+n+"\nTotal Tax paid  :"+o+"\n\n\nThank You..........."
            totcontaint=content1+content2 


            mail= smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login('etaxsupp2019@gmail.com','Pass@123')
            mail.sendmail('etaxsupp2019@gmail.com',email,totcontaint)
            mail.close()
            messagebox.showinfo("etax-2019","Reciept Delivered successfully...............")




    def finds(self):
        id=str(self.txt_findid.get());
        if id=="":
            tkinter.messagebox.showerror('eTAX-2019','Please Enter id number')
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
        mycursor=mydb.cursor()
        query = ("SELECT idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total FROM kalamwadiinfo WHERE idnumber = "+id)
        mycursor.execute(query)
        for(idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total) in mycursor:
            s="{}     {}      {}      {}      {}      {}       {}     {}".format(idnumber, meternumber, wardnumber, housetax, healthtax, lighttax, watertax, total)
            self.taxbox.insert(0,s)


        mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
        mycursor=mydb.cursor()
        query = ("SELECT idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total FROM kalamwadiinfo WHERE idnumber = "+id)
        mycursor.execute(query)
        for(idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total) in mycursor:
            s="{}   {}".format(idnumber, name)
            self.namebox.insert(0,s)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1538x862+-22+0")
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
        self.Label1.configure(font="-family {Britannic Bold} -size 48 -weight bold")
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
        self.Label1_1.configure(font="-family {Britannic Bold} -size 48 -weight bold")
        self.Label1_1.configure(foreground="#2212ff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''2019''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.072, rely=0.104, height=31, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffff24")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe Script} -size 12 -slant italic")
        self.Label2.configure(foreground="#13c12a")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''working for you''')

        self.backbutton = tk.Button(top)
        self.backbutton.place(relx=0.013, rely=0.162, height=44, width=97)
        self.backbutton.configure(activebackground="#ececec")
        self.backbutton.configure(activeforeground="#000000")
        self.backbutton.configure(background="#120bd8")
        self.backbutton.configure(disabledforeground="#a3a3a3")
        self.backbutton.configure(font="-family {Rockwell Extra Bold} -size 12 -weight bold")
        self.backbutton.configure(foreground="#fcffff")
        self.backbutton.configure(highlightbackground="#d9d9d9")
        self.backbutton.configure(highlightcolor="black")
        self.backbutton.configure(pady="0")
        self.backbutton.configure(text='''Back''')

        self.exit = tk.Button(top)
        self.exit.place(relx=0.104, rely=0.162, height=44, width=97)
        self.exit.configure(activebackground="#ececec")
        self.exit.configure(activeforeground="#000000")
        self.exit.configure(background="#120bd8")
        self.exit.configure(disabledforeground="#a3a3a3")
        self.exit.configure(font="-family {Rockwell Extra Bold} -size 12 -weight bold")
        self.exit.configure(foreground="#fcffff")
        self.exit.configure(highlightbackground="#d9d9d9")
        self.exit.configure(highlightcolor="black")
        self.exit.configure(pady="0")
        self.exit.configure(text='''Exit''',command= self.exits)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.013, rely=0.916, height=21, width=56)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffff24")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''etax-2019''')

        self.Label3_3 = tk.Label(top)
        self.Label3_3.place(relx=0.013, rely=0.94, height=21, width=34)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#ffff24")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(foreground="#000000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''v 1.0.2''')

        self.Label3_4 = tk.Label(top)
        self.Label3_4.place(relx=0.007, rely=0.986, height=21, width=134)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#ffff24")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(foreground="#000000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Working On Windows''')

        self.Label3_1 = tk.Label(top)
        self.Label3_1.place(relx=0.013, rely=0.963, height=21, width=164)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#ffff24")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Connected to MySQL server 8.0''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.39, rely=0.023, height=68, width=361)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ffff24")
        self.Label4.configure(disabledforeground="#36911a")
        self.Label4.configure(font="-family {Rockwell Extra Bold} -size 40 -weight bold")
        self.Label4.configure(foreground="#36911a")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Workspace''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.793, rely=0.035, height=28, width=192)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#ffff24")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Rockwell} -size 15")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Village : Kalamwadi''')

        self.Label5_2 = tk.Label(top)
        self.Label5_2.place(relx=0.813, rely=0.07, height=28, width=172)
        self.Label5_2.configure(activebackground="#f9f9f9")
        self.Label5_2.configure(activeforeground="black")
        self.Label5_2.configure(background="#ffff24")
        self.Label5_2.configure(disabledforeground="#a3a3a3")
        self.Label5_2.configure(font="-family {Rockwell} -size 15")
        self.Label5_2.configure(foreground="#000000")
        self.Label5_2.configure(highlightbackground="#d9d9d9")
        self.Label5_2.configure(highlightcolor="black")
        self.Label5_2.configure(text='''District : Sangli''')

        self.Label5_3 = tk.Label(top)
        self.Label5_3.place(relx=0.897, rely=0.94, height=28, width=172)
        self.Label5_3.configure(activebackground="#f9f9f9")
        self.Label5_3.configure(activeforeground="black")
        self.Label5_3.configure(background="#ffff24")
        self.Label5_3.configure(disabledforeground="#a3a3a3")
        self.Label5_3.configure(font="-family {Rockwell} -size 9")
        self.Label5_3.configure(foreground="#000000")
        self.Label5_3.configure(highlightbackground="#d9d9d9")
        self.Label5_3.configure(highlightcolor="black")
        self.Label5_3.configure(text='''Server  Status : Online''')

        self.Label5_4 = tk.Label(top)
        self.Label5_4.place(relx=0.904, rely=0.963, height=28, width=172)
        self.Label5_4.configure(activebackground="#f9f9f9")
        self.Label5_4.configure(activeforeground="black")
        self.Label5_4.configure(background="#ffff24")
        self.Label5_4.configure(disabledforeground="#a3a3a3")
        self.Label5_4.configure(font="-family {Rockwell} -size 9")
        self.Label5_4.configure(foreground="#000000")
        self.Label5_4.configure(highlightbackground="#d9d9d9")
        self.Label5_4.configure(highlightcolor="black")
        self.Label5_4.configure(text='''Host : localhost''')

        self.Label5_5 = tk.Label(top)
        self.Label5_5.place(relx=0.904, rely=0.986, height=28, width=172)
        self.Label5_5.configure(activebackground="#f9f9f9")
        self.Label5_5.configure(activeforeground="black")
        self.Label5_5.configure(background="#ffff24")
        self.Label5_5.configure(disabledforeground="#a3a3a3")
        self.Label5_5.configure(font="-family {Rockwell} -size 9")
        self.Label5_5.configure(foreground="#000000")
        self.Label5_5.configure(highlightbackground="#d9d9d9")
        self.Label5_5.configure(highlightcolor="black")
        self.Label5_5.configure(text='''Port : 3306''')

        self.Label5_1 = tk.Label(top)
        self.Label5_1.place(relx=0.91, rely=0.093, height=28, width=172)
        self.Label5_1.configure(activebackground="#f9f9f9")
        self.Label5_1.configure(activeforeground="black")
        self.Label5_1.configure(background="#ffff24")
        self.Label5_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1.configure(font="-family {Rockwell} -size 12")
        self.Label5_1.configure(foreground="#000000")
        self.Label5_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1.configure(highlightcolor="black")
        self.Label5_1.configure(text='''User : user''')

        self.namebox = ScrolledListBox(top)
        self.namebox.place(relx=0.403, rely=0.278, relheight=0.621
                , relwidth=0.248)
        self.namebox.configure(background="white")
        self.namebox.configure(disabledforeground="#a3a3a3")
        self.namebox.configure(font="TkFixedFont")
        self.namebox.configure(foreground="black")
        self.namebox.configure(highlightbackground="#d9d9d9")
        self.namebox.configure(highlightcolor="#d9d9d9")
        self.namebox.configure(selectbackground="#c4c4c4")
        self.namebox.configure(selectforeground="black")
        self.namebox.configure(width=10)

        self.taxbox = ScrolledListBox(top)
        self.taxbox.place(relx=0.65, rely=0.278, relheight=0.621, relwidth=0.339)

        self.taxbox.configure(background="white")
        self.taxbox.configure(disabledforeground="#a3a3a3")
        self.taxbox.configure(font="TkFixedFont")
        self.taxbox.configure(foreground="black")
        self.taxbox.configure(highlightbackground="#d9d9d9")
        self.taxbox.configure(highlightcolor="#d9d9d9")
        self.taxbox.configure(selectbackground="#c4c4c4")
        self.taxbox.configure(selectforeground="black")
        self.taxbox.configure(width=10)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.923, rely=0.012, relheight=0.116)
        self.TSeparator1.configure(orient="vertical")

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.013, rely=0.139, relwidth=0.202)

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.013, rely=0.232, relwidth=0.975)

        self.TSeparator3_6 = ttk.Separator(top)
        self.TSeparator3_6.place(relx=0.013, rely=0.911, relwidth=0.975)

        self.viewbutton = tk.Button(top)
        self.viewbutton.place(relx=0.494, rely=0.94, height=33, width=148)
        self.viewbutton.configure(activebackground="#ececec")
        self.viewbutton.configure(activeforeground="#000000")
        self.viewbutton.configure(background="#2020d8")
        self.viewbutton.configure(disabledforeground="#a3a3a3")
        self.viewbutton.configure(font="-family {Rockwell} -size 13 -weight bold")
        self.viewbutton.configure(foreground="#ffffff")
        self.viewbutton.configure(highlightbackground="#d9d9d9")
        self.viewbutton.configure(highlightcolor="black")
        self.viewbutton.configure(pady="0")
        self.viewbutton.configure(takefocus="0")
        self.viewbutton.configure(text='''View all Names''',command=self.viewnames)

        self.viewallbutton = tk.Button(top)
        self.viewallbutton.place(relx=0.683, rely=0.94, height=33, width=148)
        self.viewallbutton.configure(activebackground="#ececec")
        self.viewallbutton.configure(activeforeground="#000000")
        self.viewallbutton.configure(background="#2020d8")
        self.viewallbutton.configure(disabledforeground="#a3a3a3")
        self.viewallbutton.configure(font="-family {Rockwell} -size 13 -weight bold")
        self.viewallbutton.configure(foreground="#ffffff")
        self.viewallbutton.configure(highlightbackground="#d9d9d9")
        self.viewallbutton.configure(highlightcolor="black")
        self.viewallbutton.configure(pady="0")
        self.viewallbutton.configure(takefocus="0")
        self.viewallbutton.configure(text='''View all Data''',command=self.viewalls)

        self.clearall_button = tk.Button(top)
        self.clearall_button.place(relx=0.8, rely=0.94, height=33, width=108)
        self.clearall_button.configure(activebackground="#ececec")
        self.clearall_button.configure(activeforeground="#000000")
        self.clearall_button.configure(background="#2020d8")
        self.clearall_button.configure(disabledforeground="#a3a3a3")
        self.clearall_button.configure(font="-family {Rockwell} -size 13 -weight bold")
        self.clearall_button.configure(foreground="#ffffff")
        self.clearall_button.configure(highlightbackground="#d9d9d9")
        self.clearall_button.configure(highlightcolor="black")
        self.clearall_button.configure(pady="0")
        self.clearall_button.configure(takefocus="0")
        self.clearall_button.configure(text='''Clear all''',command=self.clear)

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.949, rely=0.035, height=44, width=44)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../view database/original/login3.png")
        self._img0 = tk.PhotoImage(file=photo_location)
        self.Label6.configure(image=self._img0)
        self.Label6.configure(text='''Label''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.325, relheight=0.493, relwidth=0.198)
        self.Frame1.configure(relief='ridge')
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief='ridge')
        self.Frame1.configure(background="#50e82a")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.066, rely=0.071, height=39, width=106)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#50e82a")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''ID Number :''')

        self.txt_idnumber = tk.Entry(self.Frame1)
        self.txt_idnumber.place(relx=0.426, rely=0.094, height=20
                , relwidth=0.538)
        self.txt_idnumber.configure(background="white")
        self.txt_idnumber.configure(disabledforeground="#a3a3a3")
        self.txt_idnumber.configure(font="TkFixedFont")
        self.txt_idnumber.configure(foreground="#000000")
        self.txt_idnumber.configure(highlightbackground="#d9d9d9")
        self.txt_idnumber.configure(highlightcolor="black")
        self.txt_idnumber.configure(insertbackground="black")
        self.txt_idnumber.configure(selectbackground="#c4c4c4")
        self.txt_idnumber.configure(selectforeground="black")

        self.Label7_1 = tk.Label(self.Frame1)
        self.Label7_1.place(relx=0.033, rely=0.165, height=39, width=106)
        self.Label7_1.configure(activebackground="#f9f9f9")
        self.Label7_1.configure(activeforeground="black")
        self.Label7_1.configure(background="#50e82a")
        self.Label7_1.configure(disabledforeground="#a3a3a3")
        self.Label7_1.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_1.configure(foreground="#000000")
        self.Label7_1.configure(highlightbackground="#d9d9d9")
        self.Label7_1.configure(highlightcolor="black")
        self.Label7_1.configure(text='''Name :''')

        self.Label7_2 = tk.Label(self.Frame1)
        self.Label7_2.place(relx=0.033, rely=0.282, height=29, width=116)
        self.Label7_2.configure(activebackground="#f9f9f9")
        self.Label7_2.configure(activeforeground="black")
        self.Label7_2.configure(background="#50e82a")
        self.Label7_2.configure(disabledforeground="#a3a3a3")
        self.Label7_2.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_2.configure(foreground="#000000")
        self.Label7_2.configure(highlightbackground="#d9d9d9")
        self.Label7_2.configure(highlightcolor="black")
        self.Label7_2.configure(text='''Meter Number :''')

        self.Label7_3 = tk.Label(self.Frame1)
        self.Label7_3.place(relx=0.033, rely=0.353, height=39, width=116)
        self.Label7_3.configure(activebackground="#f9f9f9")
        self.Label7_3.configure(activeforeground="black")
        self.Label7_3.configure(background="#50e82a")
        self.Label7_3.configure(disabledforeground="#a3a3a3")
        self.Label7_3.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_3.configure(foreground="#000000")
        self.Label7_3.configure(highlightbackground="#d9d9d9")
        self.Label7_3.configure(highlightcolor="black")
        self.Label7_3.configure(text='''Ward Number :''')

        self.Label7_4 = tk.Label(self.Frame1)
        self.Label7_4.place(relx=0.033, rely=0.447, height=39, width=106)
        self.Label7_4.configure(activebackground="#f9f9f9")
        self.Label7_4.configure(activeforeground="black")
        self.Label7_4.configure(background="#50e82a")
        self.Label7_4.configure(disabledforeground="#a3a3a3")
        self.Label7_4.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_4.configure(foreground="#000000")
        self.Label7_4.configure(highlightbackground="#d9d9d9")
        self.Label7_4.configure(highlightcolor="black")
        self.Label7_4.configure(text='''House Tax :''')

        self.Label7_5 = tk.Label(self.Frame1)
        self.Label7_5.place(relx=0.033, rely=0.541, height=39, width=106)
        self.Label7_5.configure(activebackground="#f9f9f9")
        self.Label7_5.configure(activeforeground="black")
        self.Label7_5.configure(background="#50e82a")
        self.Label7_5.configure(disabledforeground="#a3a3a3")
        self.Label7_5.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_5.configure(foreground="#000000")
        self.Label7_5.configure(highlightbackground="#d9d9d9")
        self.Label7_5.configure(highlightcolor="black")
        self.Label7_5.configure(text='''Health Tax :''')

        self.Label7_6 = tk.Label(self.Frame1)
        self.Label7_6.place(relx=0.033, rely=0.635, height=39, width=106)
        self.Label7_6.configure(activebackground="#f9f9f9")
        self.Label7_6.configure(activeforeground="black")
        self.Label7_6.configure(background="#50e82a")
        self.Label7_6.configure(disabledforeground="#a3a3a3")
        self.Label7_6.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_6.configure(foreground="#000000")
        self.Label7_6.configure(highlightbackground="#d9d9d9")
        self.Label7_6.configure(highlightcolor="black")
        self.Label7_6.configure(text='''Light Tax :''')

        self.Label7_7 = tk.Label(self.Frame1)
        self.Label7_7.place(relx=0.033, rely=0.729, height=39, width=106)
        self.Label7_7.configure(activebackground="#f9f9f9")
        self.Label7_7.configure(activeforeground="black")
        self.Label7_7.configure(background="#50e82a")
        self.Label7_7.configure(disabledforeground="#a3a3a3")
        self.Label7_7.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_7.configure(foreground="#000000")
        self.Label7_7.configure(highlightbackground="#d9d9d9")
        self.Label7_7.configure(highlightcolor="black")
        self.Label7_7.configure(text='''Water Tax :''')

        self.Label7_8 = tk.Label(self.Frame1)
        self.Label7_8.place(relx=0.033, rely=0.824, height=39, width=106)
        self.Label7_8.configure(activebackground="#f9f9f9")
        self.Label7_8.configure(activeforeground="black")
        self.Label7_8.configure(background="#50e82a")
        self.Label7_8.configure(disabledforeground="#a3a3a3")
        self.Label7_8.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_8.configure(foreground="#000000")
        self.Label7_8.configure(highlightbackground="#d9d9d9")
        self.Label7_8.configure(highlightcolor="black")
        self.Label7_8.configure(text='''Total :''')

        self.txt_name = tk.Entry(self.Frame1)
        self.txt_name.place(relx=0.426, rely=0.188,height=20, relwidth=0.538)
        self.txt_name.configure(background="white")
        self.txt_name.configure(disabledforeground="#a3a3a3")
        self.txt_name.configure(font="TkFixedFont")
        self.txt_name.configure(foreground="#000000")
        self.txt_name.configure(highlightbackground="#d9d9d9")
        self.txt_name.configure(highlightcolor="black")
        self.txt_name.configure(insertbackground="black")
        self.txt_name.configure(selectbackground="#c4c4c4")
        self.txt_name.configure(selectforeground="black")

        self.txt_meternumber = tk.Entry(self.Frame1)
        self.txt_meternumber.place(relx=0.426, rely=0.282, height=20
                , relwidth=0.505)
        self.txt_meternumber.configure(background="white")
        self.txt_meternumber.configure(disabledforeground="#a3a3a3")
        self.txt_meternumber.configure(font="TkFixedFont")
        self.txt_meternumber.configure(foreground="#000000")
        self.txt_meternumber.configure(highlightbackground="#d9d9d9")
        self.txt_meternumber.configure(highlightcolor="black")
        self.txt_meternumber.configure(insertbackground="black")
        self.txt_meternumber.configure(selectbackground="#c4c4c4")
        self.txt_meternumber.configure(selectforeground="black")

        self.txt_wardnumber = tk.Entry(self.Frame1)
        self.txt_wardnumber.place(relx=0.426, rely=0.353, height=20
                , relwidth=0.505)
        self.txt_wardnumber.configure(background="white")
        self.txt_wardnumber.configure(disabledforeground="#a3a3a3")
        self.txt_wardnumber.configure(font="TkFixedFont")
        self.txt_wardnumber.configure(foreground="#000000")
        self.txt_wardnumber.configure(highlightbackground="#d9d9d9")
        self.txt_wardnumber.configure(highlightcolor="black")
        self.txt_wardnumber.configure(insertbackground="black")
        self.txt_wardnumber.configure(selectbackground="#c4c4c4")
        self.txt_wardnumber.configure(selectforeground="black")

        self.txt_house = tk.Entry(self.Frame1)
        self.txt_house.place(relx=0.393, rely=0.471,height=20, relwidth=0.538)
        self.txt_house.configure(background="white")
        self.txt_house.configure(disabledforeground="#a3a3a3")
        self.txt_house.configure(font="TkFixedFont")
        self.txt_house.configure(foreground="#000000")
        self.txt_house.configure(highlightbackground="#d9d9d9")
        self.txt_house.configure(highlightcolor="black")
        self.txt_house.configure(insertbackground="black")
        self.txt_house.configure(selectbackground="#c4c4c4")
        self.txt_house.configure(selectforeground="black")

        self.txt_total = tk.Entry(self.Frame1)
        self.txt_total.place(relx=0.393, rely=0.847,height=20, relwidth=0.538)
        self.txt_total.configure(background="white")
        self.txt_total.configure(disabledforeground="#a3a3a3")
        self.txt_total.configure(font="TkFixedFont")
        self.txt_total.configure(foreground="#000000")
        self.txt_total.configure(highlightbackground="#d9d9d9")
        self.txt_total.configure(highlightcolor="black")
        self.txt_total.configure(insertbackground="black")
        self.txt_total.configure(selectbackground="#c4c4c4")
        self.txt_total.configure(selectforeground="black")

        self.txt_light = tk.Entry(self.Frame1)
        self.txt_light.place(relx=0.393, rely=0.659,height=20, relwidth=0.538)
        self.txt_light.configure(background="white")
        self.txt_light.configure(disabledforeground="#a3a3a3")
        self.txt_light.configure(font="TkFixedFont")
        self.txt_light.configure(foreground="#000000")
        self.txt_light.configure(highlightbackground="#d9d9d9")
        self.txt_light.configure(highlightcolor="black")
        self.txt_light.configure(insertbackground="black")
        self.txt_light.configure(selectbackground="#c4c4c4")
        self.txt_light.configure(selectforeground="black")

        self.txt_health = tk.Entry(self.Frame1)
        self.txt_health.place(relx=0.393, rely=0.565,height=20, relwidth=0.538)
        self.txt_health.configure(background="white")
        self.txt_health.configure(disabledforeground="#a3a3a3")
        self.txt_health.configure(font="TkFixedFont")
        self.txt_health.configure(foreground="#000000")
        self.txt_health.configure(highlightbackground="#d9d9d9")
        self.txt_health.configure(highlightcolor="black")
        self.txt_health.configure(insertbackground="black")
        self.txt_health.configure(selectbackground="#c4c4c4")
        self.txt_health.configure(selectforeground="black")

        self.txt_water = tk.Entry(self.Frame1)
        self.txt_water.place(relx=0.393, rely=0.753,height=20, relwidth=0.538)
        self.txt_water.configure(background="white")
        self.txt_water.configure(disabledforeground="#a3a3a3")
        self.txt_water.configure(font="TkFixedFont")
        self.txt_water.configure(foreground="#000000")
        self.txt_water.configure(highlightbackground="#d9d9d9")
        self.txt_water.configure(highlightcolor="black")
        self.txt_water.configure(insertbackground="black")
        self.txt_water.configure(selectbackground="#c4c4c4")
        self.txt_water.configure(selectforeground="black")

        self.Frame1_20 = tk.Frame(top)
        self.Frame1_20.place(relx=0.202, rely=0.267, relheight=0.4
                , relwidth=0.198)
        self.Frame1_20.configure(relief='ridge')
        self.Frame1_20.configure(borderwidth="10")
        self.Frame1_20.configure(relief='ridge')
        self.Frame1_20.configure(background="#50e82a")
        self.Frame1_20.configure(highlightbackground="#d9d9d9")
        self.Frame1_20.configure(highlightcolor="black")

        self.Label7_21 = tk.Label(self.Frame1_20)
        self.Label7_21.place(relx=0.033, rely=0.087, height=39, width=126)
        self.Label7_21.configure(activebackground="#f9f9f9")
        self.Label7_21.configure(activeforeground="black")
        self.Label7_21.configure(background="#50e82a")
        self.Label7_21.configure(disabledforeground="#a3a3a3")
        self.Label7_21.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_21.configure(foreground="#000000")
        self.Label7_21.configure(highlightbackground="#d9d9d9")
        self.Label7_21.configure(highlightcolor="black")
        self.Label7_21.configure(text='''Reciept Number :''')

        self.txt_reciept = tk.Entry(self.Frame1_20)
        self.txt_reciept.place(relx=0.492, rely=0.116, height=20, relwidth=0.439)

        self.txt_reciept.configure(background="white")
        self.txt_reciept.configure(disabledforeground="#a3a3a3")
        self.txt_reciept.configure(font="TkFixedFont")
        self.txt_reciept.configure(foreground="#000000")
        self.txt_reciept.configure(highlightbackground="#d9d9d9")
        self.txt_reciept.configure(highlightcolor="black")
        self.txt_reciept.configure(insertbackground="black")
        self.txt_reciept.configure(selectbackground="#c4c4c4")
        self.txt_reciept.configure(selectforeground="black")

        self.Label7_1 = tk.Label(self.Frame1_20)
        self.Label7_1.place(relx=0.033, rely=0.203, height=39, width=126)
        self.Label7_1.configure(activebackground="#f9f9f9")
        self.Label7_1.configure(activeforeground="black")
        self.Label7_1.configure(background="#50e82a")
        self.Label7_1.configure(disabledforeground="#a3a3a3")
        self.Label7_1.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_1.configure(foreground="#000000")
        self.Label7_1.configure(highlightbackground="#d9d9d9")
        self.Label7_1.configure(highlightcolor="black")
        self.Label7_1.configure(text='''Housetax(Paid) :''')

        self.Label7_2 = tk.Label(self.Frame1_20)
        self.Label7_2.place(relx=0.033, rely=0.319, height=39, width=126)
        self.Label7_2.configure(activebackground="#f9f9f9")
        self.Label7_2.configure(activeforeground="black")
        self.Label7_2.configure(background="#50e82a")
        self.Label7_2.configure(disabledforeground="#a3a3a3")
        self.Label7_2.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_2.configure(foreground="#000000")
        self.Label7_2.configure(highlightbackground="#d9d9d9")
        self.Label7_2.configure(highlightcolor="black")
        self.Label7_2.configure(text='''Healthtax (Paid) :''')

        self.Label7_3 = tk.Label(self.Frame1_20)
        self.Label7_3.place(relx=0.066, rely=0.435, height=39, width=116)
        self.Label7_3.configure(activebackground="#f9f9f9")
        self.Label7_3.configure(activeforeground="black")
        self.Label7_3.configure(background="#50e82a")
        self.Label7_3.configure(disabledforeground="#a3a3a3")
        self.Label7_3.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_3.configure(foreground="#000000")
        self.Label7_3.configure(highlightbackground="#d9d9d9")
        self.Label7_3.configure(highlightcolor="black")
        self.Label7_3.configure(text='''Lighttax(Paid) :''')

        self.Label7_4 = tk.Label(self.Frame1_20)
        self.Label7_4.place(relx=0.033, rely=0.551, height=39, width=116)
        self.Label7_4.configure(activebackground="#f9f9f9")
        self.Label7_4.configure(activeforeground="black")
        self.Label7_4.configure(background="#50e82a")
        self.Label7_4.configure(disabledforeground="#a3a3a3")
        self.Label7_4.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_4.configure(foreground="#000000")
        self.Label7_4.configure(highlightbackground="#d9d9d9")
        self.Label7_4.configure(highlightcolor="black")
        self.Label7_4.configure(text='''Watertax(Paid) :''')

        self.Label7_5 = tk.Label(self.Frame1_20)
        self.Label7_5.place(relx=0.033, rely=0.667, height=39, width=106)
        self.Label7_5.configure(activebackground="#f9f9f9")
        self.Label7_5.configure(activeforeground="black")
        self.Label7_5.configure(background="#50e82a")
        self.Label7_5.configure(disabledforeground="#a3a3a3")
        self.Label7_5.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_5.configure(foreground="#000000")
        self.Label7_5.configure(highlightbackground="#d9d9d9")
        self.Label7_5.configure(highlightcolor="black")
        self.Label7_5.configure(text='''Total (Paid) :''')

        self.txt_housepaid = tk.Entry(self.Frame1_20)
        self.txt_housepaid.place(relx=0.492, rely=0.232, height=20
                , relwidth=0.439)
        self.txt_housepaid.configure(background="white")
        self.txt_housepaid.configure(disabledforeground="#a3a3a3")
        self.txt_housepaid.configure(font="TkFixedFont")
        self.txt_housepaid.configure(foreground="#000000")
        self.txt_housepaid.configure(highlightbackground="#d9d9d9")
        self.txt_housepaid.configure(highlightcolor="black")
        self.txt_housepaid.configure(insertbackground="black")
        self.txt_housepaid.configure(selectbackground="#c4c4c4")
        self.txt_housepaid.configure(selectforeground="black")

        self.txt_healthpaid = tk.Entry(self.Frame1_20)
        self.txt_healthpaid.place(relx=0.492, rely=0.348, height=20
                , relwidth=0.439)
        self.txt_healthpaid.configure(background="white")
        self.txt_healthpaid.configure(disabledforeground="#a3a3a3")
        self.txt_healthpaid.configure(font="TkFixedFont")
        self.txt_healthpaid.configure(foreground="#000000")
        self.txt_healthpaid.configure(highlightbackground="#d9d9d9")
        self.txt_healthpaid.configure(highlightcolor="black")
        self.txt_healthpaid.configure(insertbackground="black")
        self.txt_healthpaid.configure(selectbackground="#c4c4c4")
        self.txt_healthpaid.configure(selectforeground="black")

        self.txt_lightpaid = tk.Entry(self.Frame1_20)
        self.txt_lightpaid.place(relx=0.492, rely=0.464, height=20
                , relwidth=0.439)
        self.txt_lightpaid.configure(background="white")
        self.txt_lightpaid.configure(disabledforeground="#a3a3a3")
        self.txt_lightpaid.configure(font="TkFixedFont")
        self.txt_lightpaid.configure(foreground="#000000")
        self.txt_lightpaid.configure(highlightbackground="#d9d9d9")
        self.txt_lightpaid.configure(highlightcolor="black")
        self.txt_lightpaid.configure(insertbackground="black")
        self.txt_lightpaid.configure(selectbackground="#c4c4c4")
        self.txt_lightpaid.configure(selectforeground="black")

        self.txt_waterpaid = tk.Entry(self.Frame1_20)
        self.txt_waterpaid.place(relx=0.492, rely=0.58, height=20
                , relwidth=0.439)
        self.txt_waterpaid.configure(background="white")
        self.txt_waterpaid.configure(disabledforeground="#a3a3a3")
        self.txt_waterpaid.configure(font="TkFixedFont")
        self.txt_waterpaid.configure(foreground="#000000")
        self.txt_waterpaid.configure(highlightbackground="#d9d9d9")
        self.txt_waterpaid.configure(highlightcolor="black")
        self.txt_waterpaid.configure(insertbackground="black")
        self.txt_waterpaid.configure(selectbackground="#c4c4c4")
        self.txt_waterpaid.configure(selectforeground="black")

        self.txt_totalpaid = tk.Entry(self.Frame1_20)
        self.txt_totalpaid.place(relx=0.492, rely=0.696, height=20
                , relwidth=0.439)
        self.txt_totalpaid.configure(background="white")
        self.txt_totalpaid.configure(disabledforeground="#a3a3a3")
        self.txt_totalpaid.configure(font="TkFixedFont")
        self.txt_totalpaid.configure(foreground="#000000")
        self.txt_totalpaid.configure(highlightbackground="#d9d9d9")
        self.txt_totalpaid.configure(highlightcolor="black")
        self.txt_totalpaid.configure(insertbackground="black")
        self.txt_totalpaid.configure(selectbackground="#c4c4c4")
        self.txt_totalpaid.configure(selectforeground="black")

        self.btn_submit = tk.Button(self.Frame1_20)
        self.btn_submit.place(relx=0.328, rely=0.812, height=44, width=97)
        self.btn_submit.configure(activebackground="#ececec")
        self.btn_submit.configure(activeforeground="#000000")
        self.btn_submit.configure(background="#ff350d")
        self.btn_submit.configure(disabledforeground="#a3a3a3")
        self.btn_submit.configure(font="-family {Segoe UI} -size 13")
        self.btn_submit.configure(foreground="#ffffff")
        self.btn_submit.configure(highlightbackground="#d9d9d9")
        self.btn_submit.configure(highlightcolor="black")
        self.btn_submit.configure(pady="0")
        self.btn_submit.configure(text='''SUBMIT''',command= self.submits)

        self.Frame1_18 = tk.Frame(top)
        self.Frame1_18.place(relx=0.202, rely=0.673, relheight=0.226
                , relwidth=0.198)
        self.Frame1_18.configure(relief='ridge')
        self.Frame1_18.configure(borderwidth="10")
        self.Frame1_18.configure(relief='ridge')
        self.Frame1_18.configure(background="#50e82a")
        self.Frame1_18.configure(highlightbackground="#d9d9d9")
        self.Frame1_18.configure(highlightcolor="black")

        self.Label7_19 = tk.Label(self.Frame1_18)
        self.Label7_19.place(relx=0.098, rely=0.359, height=29, width=256)
        self.Label7_19.configure(activebackground="#f9f9f9")
        self.Label7_19.configure(activeforeground="black")
        self.Label7_19.configure(background="#50e82a")
        self.Label7_19.configure(disabledforeground="#a3a3a3")
        self.Label7_19.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_19.configure(foreground="#000000")
        self.Label7_19.configure(highlightbackground="#d9d9d9")
        self.Label7_19.configure(highlightcolor="black")
        self.Label7_19.configure(text='''Enter The ID Number Here :''')

        self.txt_findid = tk.Entry(self.Frame1_18)
        self.txt_findid.place(relx=0.098, rely=0.513,height=20, relwidth=0.833)
        self.txt_findid.configure(background="white")
        self.txt_findid.configure(disabledforeground="#a3a3a3")
        self.txt_findid.configure(font="TkFixedFont")
        self.txt_findid.configure(foreground="#000000")
        self.txt_findid.configure(highlightbackground="#d9d9d9")
        self.txt_findid.configure(highlightcolor="black")
        self.txt_findid.configure(insertbackground="black")
        self.txt_findid.configure(selectbackground="#c4c4c4")
        self.txt_findid.configure(selectforeground="black")

        self.Label8 = tk.Label(self.Frame1_18)
        self.Label8.place(relx=0.23, rely=0.103, height=27, width=168)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#50e82a")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Rockwell} -size 14")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''-----Find Entry-----''')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.0, rely=0.752, relheight=0.131, relwidth=0.198)
        self.Frame2.configure(relief='ridge')
        self.Frame2.configure(borderwidth="10")
        self.Frame2.configure(relief='ridge')
        self.Frame2.configure(background="#50e82a")
        self.Frame2.configure(width=305)

        self.Label8_8 = tk.Label(self.Frame2)
        self.Label8_8.place(relx=0.23, rely=0.087, height=27, width=168)
        self.Label8_8.configure(activebackground="#f9f9f9")
        self.Label8_8.configure(activeforeground="black")
        self.Label8_8.configure(background="#50e82a")
        self.Label8_8.configure(disabledforeground="#a3a3a3")
        self.Label8_8.configure(font="-family {Rockwell} -size 14")
        self.Label8_8.configure(foreground="#000000")
        self.Label8_8.configure(highlightbackground="#d9d9d9")
        self.Label8_8.configure(highlightcolor="black")
        self.Label8_8.configure(text='''-----Email-----''')

        self.Label7_9 = tk.Label(self.Frame2)
        self.Label7_9.place(relx=0.033, rely=0.261, height=29, width=286)
        self.Label7_9.configure(activebackground="#f9f9f9")
        self.Label7_9.configure(activeforeground="black")
        self.Label7_9.configure(background="#50e82a")
        self.Label7_9.configure(disabledforeground="#a3a3a3")
        self.Label7_9.configure(font="-family {Plantagenet Cherokee} -size 13")
        self.Label7_9.configure(foreground="#000000")
        self.Label7_9.configure(highlightbackground="#d9d9d9")
        self.Label7_9.configure(highlightcolor="black")
        self.Label7_9.configure(text='''Enter The Email  Here :''')
        self.Label7_9.configure(width=286)

        self.txt_findid_10 = tk.Entry(self.Frame2)
        self.txt_findid_10.place(relx=0.066, rely=0.609, height=20
                , relwidth=0.866)
        self.txt_findid_10.configure(background="white")
        self.txt_findid_10.configure(disabledforeground="#a3a3a3")
        self.txt_findid_10.configure(font="TkFixedFont")
        self.txt_findid_10.configure(foreground="#000000")
        self.txt_findid_10.configure(highlightbackground="#d9d9d9")
        self.txt_findid_10.configure(highlightcolor="black")
        self.txt_findid_10.configure(insertbackground="black")
        self.txt_findid_10.configure(selectbackground="#c4c4c4")
        self.txt_findid_10.configure(selectforeground="black")
        self.txt_findid_10.configure(width=264)

        self.Label9_11 = tk.Label(top)
        self.Label9_11.place(relx=0.475, rely=0.239, height=21, width=64)
        self.Label9_11.configure(activebackground="#f9f9f9")
        self.Label9_11.configure(activeforeground="black")
        self.Label9_11.configure(background="#ffff24")
        self.Label9_11.configure(disabledforeground="#a3a3a3")
        self.Label9_11.configure(foreground="#000000")
        self.Label9_11.configure(highlightbackground="#d9d9d9")
        self.Label9_11.configure(highlightcolor="black")
        self.Label9_11.configure(text='''Name''')

        self.Label9_12 = tk.Label(top)
        self.Label9_12.place(relx=0.65, rely=0.251, height=11, width=54)
        self.Label9_12.configure(activebackground="#f9f9f9")
        self.Label9_12.configure(activeforeground="black")
        self.Label9_12.configure(background="#ffff24")
        self.Label9_12.configure(disabledforeground="#a3a3a3")
        self.Label9_12.configure(foreground="#000000")
        self.Label9_12.configure(highlightbackground="#d9d9d9")
        self.Label9_12.configure(highlightcolor="black")
        self.Label9_12.configure(text='''ID No.''')
        self.Label9_12.configure(width=54)

        self.Label9_13 = tk.Label(top)
        self.Label9_13.place(relx=0.696, rely=0.251, height=11, width=54)
        self.Label9_13.configure(activebackground="#f9f9f9")
        self.Label9_13.configure(activeforeground="black")
        self.Label9_13.configure(background="#ffff24")
        self.Label9_13.configure(disabledforeground="#a3a3a3")
        self.Label9_13.configure(foreground="#000000")
        self.Label9_13.configure(highlightbackground="#d9d9d9")
        self.Label9_13.configure(highlightcolor="black")
        self.Label9_13.configure(text='''Meter No.''')

        self.Label9_13 = tk.Label(top)
        self.Label9_13.place(relx=0.741, rely=0.251, height=11, width=54)
        self.Label9_13.configure(activebackground="#f9f9f9")
        self.Label9_13.configure(activeforeground="black")
        self.Label9_13.configure(background="#ffff24")
        self.Label9_13.configure(disabledforeground="#a3a3a3")
        self.Label9_13.configure(foreground="#000000")
        self.Label9_13.configure(highlightbackground="#d9d9d9")
        self.Label9_13.configure(highlightcolor="black")
        self.Label9_13.configure(text='''Ward No.''')
        self.Label9_13.configure(width=54)

        self.Label9_13 = tk.Label(top)
        self.Label9_13.place(relx=0.78, rely=0.251, height=11, width=64)
        self.Label9_13.configure(activebackground="#f9f9f9")
        self.Label9_13.configure(activeforeground="black")
        self.Label9_13.configure(background="#ffff24")
        self.Label9_13.configure(disabledforeground="#a3a3a3")
        self.Label9_13.configure(foreground="#000000")
        self.Label9_13.configure(highlightbackground="#d9d9d9")
        self.Label9_13.configure(highlightcolor="black")
        self.Label9_13.configure(text='''Houseatax''')
        self.Label9_13.configure(width=64)

        self.Label9_14 = tk.Label(top)
        self.Label9_14.place(relx=0.826, rely=0.251, height=11, width=64)
        self.Label9_14.configure(activebackground="#f9f9f9")
        self.Label9_14.configure(activeforeground="black")
        self.Label9_14.configure(background="#ffff24")
        self.Label9_14.configure(disabledforeground="#a3a3a3")
        self.Label9_14.configure(foreground="#000000")
        self.Label9_14.configure(highlightbackground="#d9d9d9")
        self.Label9_14.configure(highlightcolor="black")
        self.Label9_14.configure(text='''Healthtaxtax''')

        self.Label9_14 = tk.Label(top)
        self.Label9_14.place(relx=0.871, rely=0.251, height=11, width=54)
        self.Label9_14.configure(activebackground="#f9f9f9")
        self.Label9_14.configure(activeforeground="black")
        self.Label9_14.configure(background="#ffff24")
        self.Label9_14.configure(disabledforeground="#a3a3a3")
        self.Label9_14.configure(foreground="#000000")
        self.Label9_14.configure(highlightbackground="#d9d9d9")
        self.Label9_14.configure(highlightcolor="black")
        self.Label9_14.configure(text='''Lighttax''')
        self.Label9_14.configure(width=54)

        self.Label9_14 = tk.Label(top)
        self.Label9_14.place(relx=0.91, rely=0.251, height=11, width=64)
        self.Label9_14.configure(activebackground="#f9f9f9")
        self.Label9_14.configure(activeforeground="black")
        self.Label9_14.configure(background="#ffff24")
        self.Label9_14.configure(disabledforeground="#a3a3a3")
        self.Label9_14.configure(foreground="#000000")
        self.Label9_14.configure(highlightbackground="#d9d9d9")
        self.Label9_14.configure(highlightcolor="black")
        self.Label9_14.configure(text='''Watertax''')

        self.Label9_14 = tk.Label(top)
        self.Label9_14.place(relx=0.949, rely=0.251, height=11, width=64)
        self.Label9_14.configure(activebackground="#f9f9f9")
        self.Label9_14.configure(activeforeground="black")
        self.Label9_14.configure(background="#ffff24")
        self.Label9_14.configure(disabledforeground="#a3a3a3")
        self.Label9_14.configure(foreground="#000000")
        self.Label9_14.configure(highlightbackground="#d9d9d9")
        self.Label9_14.configure(highlightcolor="black")
        self.Label9_14.configure(text='''Total''')

        self.btn_find = tk.Button(self.Frame1_18)
        self.btn_find.place(relx=0.328, rely=0.718, height=34, width=97)
        self.btn_find.configure(activebackground="#ececec")
        self.btn_find.configure(activeforeground="#000000")
        self.btn_find.configure(background="#252ce8")
        self.btn_find.configure(disabledforeground="#a3a3a3")
        self.btn_find.configure(foreground="#ffffff")
        self.btn_find.configure(highlightbackground="#d9d9d9")
        self.btn_find.configure(highlightcolor="black")
        self.btn_find.configure(pady="0")
        self.btn_find.configure(text='''FIND''',command=self.finds)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

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





