    import sys
    import tkinter
    from tkinter import messagebox
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

    import modificationmainpage_support
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
        top = e_TAX_2019 (root)
        modificationmainpage_support.init(root, top)
        root.mainloop()

    w = None
    def create_e_TAX_2019(root, *args, **kwargs):
        '''Starting point when module is imported by another program.'''
        global w, w_win, rt
        global prog_location
        prog_call = sys.argv[0]
        print ('prog_call = {}'.format(prog_call))
        prog_location = os.path.split(prog_call)[0]
        print ('prog_location = {}'.format(prog_location))
        rt = root
        w = tk.Toplevel (root)
        top = e_TAX_2019 (w)
        modificationmainpage_support.init(w, top, *args, **kwargs)
        return (w, top)

    def destroy_e_TAX_2019():
        global w
        w.destroy()
        w = None





























    def access1():

        import sys
        import tkinter
        import time
        from tkinter import messagebox
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

        import permit_support

        def vp_start_gui():
            '''Starting point when module is the main routine.'''
            global val, w, root
            root = tk.Tk()
            top = e_TAX_2019 (root)
            permit_support.init(root, top)
            root.mainloop()

        w = None
        def create_e_TAX_2019(root, *args, **kwargs):
            '''Starting point when module is imported by another program.'''
            global w, w_win, rt
            rt = root
            w = tk.Toplevel (root)
            top = e_TAX_2019 (w)
            permit_support.init(w, top, *args, **kwargs)
            return (w, top)

        def destroy_e_TAX_2019():
            global w
            w.destroy()
            w = None

        class e_TAX_2019:
            def exits(self):
                msg=tkinter.messagebox.askyesno("e-TAX 2019","Do You Want To EXIT ?")
                if msg :
                    exit()
            def backs(self):
                root.destroy()
                print("nwhcwjjwdj")

            def submits(self):
                p=str(self.txt_productkey.get());
                v=str(self.txt_village.get());
                u=str(self.txt_username.get());
                n=str(self.txt_noofentries.get());
                r=str(self.txt_reason.get());
                t=str(time.asctime(time.localtime(time.time())))


                totcontaint = str("Hi there is a new request for updating e-TAX 2019 database \n\n\n here are DETAILS ::::::\n\n\nproduct key :"+p+"\n village name :"+v+"\n Username :"+u+"\n No. of entries to modify :"+n+"\n Reason to modify data :"+r+"\n\n\n\n\n Requested on :"+t)
                mail= smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login('etaxsupp2019@gmail.com','Pass@123')
                mail.sendmail('etaxsupp2019@gmail.com','kulkarnipranesh1767@gmail.com',totcontaint)
                mail.close()
                messagebox.showinfo("e-TAX 2019","Requested for updating Data. Wait for Confirmation from Administrator. After recieving Confirmation Email From Administrator You can modify database through respective modules")
                root.destroy()



            def __init__(self, top=None):
                '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
                _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
                _fgcolor = '#000000'  # X11 color: 'black'
                _compcolor = '#d9d9d9' # X11 color: 'gray85'
                _ana1color = '#d9d9d9' # X11 color: 'gray85'
                _ana2color = '#ececec' # Closest X11 color: 'gray92'
                font12 = "-family {GoudyHandtooled BT} -size 22"
                font15 = "-family {System} -size 10 -weight bold"
                font16 = "-family {Segoe UI} -size 12"

                top.geometry("990x650+273+127")
                top.title("e-TAX 2019")
                top.configure(background="#727272")
                top.configure(highlightbackground="#d9d9d9")
                top.configure(highlightcolor="black")

                self.Frame1 = tk.Frame(top)
                self.Frame1.place(relx=0.141, rely=0.046, relheight=0.223
                        , relwidth=0.712)
                self.Frame1.configure(relief='ridge')
                self.Frame1.configure(borderwidth="10")
                self.Frame1.configure(relief='ridge')
                self.Frame1.configure(background="#595959")
                self.Frame1.configure(highlightbackground="#d9d9d9")
                self.Frame1.configure(highlightcolor="black")
                self.Frame1.configure(width=705)

                self.Label1 = tk.Label(self.Frame1)
                self.Label1.place(relx=0.043, rely=0.207, height=59, width=196)
                self.Label1.configure(activebackground="#f9f9f9")
                self.Label1.configure(activeforeground="black")
                self.Label1.configure(background="#595959")
                self.Label1.configure(disabledforeground="#a3a3a3")
                self.Label1.configure(font="-family {Rockwell Extra} -size 40 -weight bold")
                self.Label1.configure(foreground="#0d4dff")
                self.Label1.configure(highlightbackground="#d9d9d9")
                self.Label1.configure(highlightcolor="black")
                self.Label1.configure(text='''eTAX''')

                self.Label1_1 = tk.Label(self.Frame1)
                self.Label1_1.place(relx=0.298, rely=0.207, height=59, width=146)
                self.Label1_1.configure(activebackground="#f9f9f9")
                self.Label1_1.configure(activeforeground="black")
                self.Label1_1.configure(background="#595959")
                self.Label1_1.configure(disabledforeground="#a3a3a3")
                self.Label1_1.configure(font="-family {Rockwell Extra} -size 40 -weight bold")
                self.Label1_1.configure(foreground="#ff2b0a")
                self.Label1_1.configure(highlightbackground="#d9d9d9")
                self.Label1_1.configure(highlightcolor="black")
                self.Label1_1.configure(text='''2019''')

                self.Label2 = tk.Label(self.Frame1)
                self.Label2.place(relx=0.156, rely=0.621, height=31, width=184)
                self.Label2.configure(activebackground="#f9f9f9")
                self.Label2.configure(activeforeground="black")
                self.Label2.configure(background="#595959")
                self.Label2.configure(disabledforeground="#a3a3a3")
                self.Label2.configure(font="-family {Rage Italic} -size 19 -slant italic")
                self.Label2.configure(foreground="#f7ff0a")
                self.Label2.configure(highlightbackground="#d9d9d9")
                self.Label2.configure(highlightcolor="black")
                self.Label2.configure(text='''working for you''')

                self.Label1_2 = tk.Label(self.Frame1)
                self.Label1_2.place(relx=0.525, rely=0.207, height=79, width=306)
                self.Label1_2.configure(activebackground="#f9f9f9")
                self.Label1_2.configure(activeforeground="black")
                self.Label1_2.configure(background="#595959")
                self.Label1_2.configure(disabledforeground="#a3a3a3")
                self.Label1_2.configure(font="-family {Rockwell Extra} -size 28 -weight bold")
                self.Label1_2.configure(foreground="#5faa14")
                self.Label1_2.configure(highlightbackground="#d9d9d9")
                self.Label1_2.configure(highlightcolor="black")
                self.Label1_2.configure(text='''PERMISSION''')
                self.Label1_2.configure(width=306)

                self.Frame1_1 = tk.Frame(top)
                self.Frame1_1.place(relx=0.141, rely=0.308, relheight=0.577
                        , relwidth=0.712)
                self.Frame1_1.configure(relief='ridge')
                self.Frame1_1.configure(borderwidth="10")
                self.Frame1_1.configure(relief='ridge')
                self.Frame1_1.configure(background="#595959")
                self.Frame1_1.configure(highlightbackground="#d9d9d9")
                self.Frame1_1.configure(highlightcolor="black")
                self.Frame1_1.configure(width=705)

                self.Label3 = tk.Label(self.Frame1_1)
                self.Label3.place(relx=0.156, rely=0.08, height=41, width=446)
                self.Label3.configure(background="#595959")
                self.Label3.configure(disabledforeground="#a3a3a3")
                self.Label3.configure(font=font12)
                self.Label3.configure(foreground="#fbf2ff")
                self.Label3.configure(text='''FILL YOUR PRODUCT DETAILS''')

                self.Label4 = tk.Label(self.Frame1_1)
                self.Label4.place(relx=0.142, rely=0.24, height=22, width=102)
                self.Label4.configure(background="#595959")
                self.Label4.configure(disabledforeground="#a3a3a3")
                self.Label4.configure(font=font15)
                self.Label4.configure(foreground="AQUA")
                self.Label4.configure(text='''Product Key :''')
                self.Label4.configure(width=102)

                self.Label4_5 = tk.Label(self.Frame1_1)
                self.Label4_5.place(relx=0.142, rely=0.32, height=22, width=102)
                self.Label4_5.configure(activebackground="#f9f9f9")
                self.Label4_5.configure(activeforeground="black")
                self.Label4_5.configure(background="#595959")
                self.Label4_5.configure(disabledforeground="#a3a3a3")
                self.Label4_5.configure(font="-family {System} -size 10 -weight bold")
                self.Label4_5.configure(foreground="AQUA")
                self.Label4_5.configure(highlightbackground="#d9d9d9")
                self.Label4_5.configure(highlightcolor="black")
                self.Label4_5.configure(text='''Village :''')

                self.Label4_6 = tk.Label(self.Frame1_1)
                self.Label4_6.place(relx=0.142, rely=0.4, height=22, width=102)
                self.Label4_6.configure(activebackground="#f9f9f9")
                self.Label4_6.configure(activeforeground="black")
                self.Label4_6.configure(background="#595959")
                self.Label4_6.configure(disabledforeground="#a3a3a3")
                self.Label4_6.configure(font="-family {System} -size 10 -weight bold")
                self.Label4_6.configure(foreground="AQUA")
                self.Label4_6.configure(highlightbackground="#d9d9d9")
                self.Label4_6.configure(highlightcolor="black")
                self.Label4_6.configure(text='''Username :''')

                self.Label4_7 = tk.Label(self.Frame1_1)
                self.Label4_7.place(relx=0.085, rely=0.48, height=22, width=202)
                self.Label4_7.configure(activebackground="#f9f9f9")
                self.Label4_7.configure(activeforeground="black")
                self.Label4_7.configure(background="#595959")
                self.Label4_7.configure(disabledforeground="#a3a3a3")
                self.Label4_7.configure(font="-family {System} -size 10 -weight bold")
                self.Label4_7.configure(foreground="AQUA")
                self.Label4_7.configure(highlightbackground="#d9d9d9")
                self.Label4_7.configure(highlightcolor="black")
                self.Label4_7.configure(text='''No. of entries to update :''')
                self.Label4_7.configure(width=202)

                self.Label4_8 = tk.Label(self.Frame1_1)
                self.Label4_8.place(relx=0.099, rely=0.56, height=22, width=172)
                self.Label4_8.configure(activebackground="#f9f9f9")
                self.Label4_8.configure(activeforeground="black")
                self.Label4_8.configure(background="#595959")
                self.Label4_8.configure(disabledforeground="#a3a3a3")
                self.Label4_8.configure(font="-family {System} -size 10 -weight bold")
                self.Label4_8.configure(foreground="AQUA")
                self.Label4_8.configure(highlightbackground="#d9d9d9")
                self.Label4_8.configure(highlightcolor="black")
                self.Label4_8.configure(text='''Reason to modify data :''')
                self.Label4_8.configure(width=172)

                self.txt_productkey = tk.Entry(self.Frame1_1)
                self.txt_productkey.place(relx=0.397, rely=0.24, height=20
                        , relwidth=0.445)
                self.txt_productkey.configure(background="white")
                self.txt_productkey.configure(disabledforeground="#a3a3a3")
                self.txt_productkey.configure(font="TkFixedFont")
                self.txt_productkey.configure(foreground="#000000")
                self.txt_productkey.configure(insertbackground="black")
                self.txt_productkey.configure(width=314)

                self.txt_reason = tk.Entry(self.Frame1_1)
                self.txt_reason.place(relx=0.397, rely=0.56,height=20, relwidth=0.445)
                self.txt_reason.configure(background="white")
                self.txt_reason.configure(disabledforeground="#a3a3a3")
                self.txt_reason.configure(font="TkFixedFont")
                self.txt_reason.configure(foreground="#000000")
                self.txt_reason.configure(highlightbackground="#d9d9d9")
                self.txt_reason.configure(highlightcolor="black")
                self.txt_reason.configure(insertbackground="black")
                self.txt_reason.configure(selectbackground="#c4c4c4")
                self.txt_reason.configure(selectforeground="black")

                self.txt_noofentries = tk.Entry(self.Frame1_1)
                self.txt_noofentries.place(relx=0.397, rely=0.48, height=20
                        , relwidth=0.445)
                self.txt_noofentries.configure(background="white")
                self.txt_noofentries.configure(disabledforeground="#a3a3a3")
                self.txt_noofentries.configure(font="TkFixedFont")
                self.txt_noofentries.configure(foreground="#000000")
                self.txt_noofentries.configure(highlightbackground="#d9d9d9")
                self.txt_noofentries.configure(highlightcolor="black")
                self.txt_noofentries.configure(insertbackground="black")
                self.txt_noofentries.configure(selectbackground="#c4c4c4")
                self.txt_noofentries.configure(selectforeground="black")

                self.txt_username = tk.Entry(self.Frame1_1)
                self.txt_username.place(relx=0.397, rely=0.4,height=20, relwidth=0.445)
                self.txt_username.configure(background="white")
                self.txt_username.configure(disabledforeground="#a3a3a3")
                self.txt_username.configure(font="TkFixedFont")
                self.txt_username.configure(foreground="#000000")
                self.txt_username.configure(highlightbackground="#d9d9d9")
                self.txt_username.configure(highlightcolor="black")
                self.txt_username.configure(insertbackground="black")
                self.txt_username.configure(selectbackground="#c4c4c4")
                self.txt_username.configure(selectforeground="black")

                self.txt_village = tk.Entry(self.Frame1_1)
                self.txt_village.place(relx=0.397, rely=0.32,height=20, relwidth=0.445)
                self.txt_village.configure(background="white")
                self.txt_village.configure(disabledforeground="#a3a3a3")
                self.txt_village.configure(font="TkFixedFont")
                self.txt_village.configure(foreground="#000000")
                self.txt_village.configure(highlightbackground="#d9d9d9")
                self.txt_village.configure(highlightcolor="black")
                self.txt_village.configure(insertbackground="black")
                self.txt_village.configure(selectbackground="#c4c4c4")
                self.txt_village.configure(selectforeground="black")

                self.btn_submit = tk.Button(self.Frame1_1)
                self.btn_submit.place(relx=0.454, rely=0.667, height=44, width=227)
                self.btn_submit.configure(activebackground="#ececec")
                self.btn_submit.configure(activeforeground="#000000")
                self.btn_submit.configure(background="#3028a0")
                self.btn_submit.configure(borderwidth="10")
                self.btn_submit.configure(disabledforeground="#a3a3a3")
                self.btn_submit.configure(font=font16)
                self.btn_submit.configure(foreground="#ffffff")
                self.btn_submit.configure(highlightbackground="#d9d9d9")
                self.btn_submit.configure(highlightcolor="black")
                self.btn_submit.configure(pady="0")
                self.btn_submit.configure(text='''Ask for permission''',command = self.submits)
                self.btn_submit.configure(width=227)

                self.btn_exit = tk.Button(top)
                self.btn_exit.place(relx=0.879, rely=0.169, height=44, width=107)
                self.btn_exit.configure(activebackground="#ececec")
                self.btn_exit.configure(activeforeground="#000000")
                self.btn_exit.configure(background="#ff002b")
                self.btn_exit.configure(borderwidth="10")
                self.btn_exit.configure(disabledforeground="#a3a3a3")
                self.btn_exit.configure(font="-family {Segoe UI} -size 12")
                self.btn_exit.configure(foreground="#ffffff")
                self.btn_exit.configure(highlightbackground="#d9d9d9")
                self.btn_exit.configure(highlightcolor="black")
                self.btn_exit.configure(pady="0")
                self.btn_exit.configure(text='''EXIT''',command = self.exits)
                self.btn_exit.configure(width=107)

                self.btn_back = tk.Button(top)
                self.btn_back.place(relx=0.879, rely=0.077, height=44, width=107)
                self.btn_back.configure(activebackground="#ececec")
                self.btn_back.configure(activeforeground="#000000")
                self.btn_back.configure(background="#39a324")
                self.btn_back.configure(borderwidth="10")
                self.btn_back.configure(disabledforeground="#a3a3a3")
                self.btn_back.configure(font="-family {Segoe UI} -size 12")
                self.btn_back.configure(foreground="#ffffff")
                self.btn_back.configure(highlightbackground="#d9d9d9")
                self.btn_back.configure(highlightcolor="black")
                self.btn_back.configure(pady="0")
                self.btn_back.configure(text='''BACK''',command = self.backs)

        if __name__ == '__main__':
            vp_start_gui()










































    def modify1():

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

        import modifymod_support

        def vp_start_gui():
            '''Starting point when module is the main routine.'''
            global val, w, root
            root = tk.Tk()
            top = Toplevel1 (root)
            modifymod_support.init(root, top)
            root.mainloop()

        w = None
        def create_Toplevel1(root, *args, **kwargs):
            '''Starting point when module is imported by another program.'''
            global w, w_win, rt
            rt = root
            w = tk.Toplevel (root)
            top = Toplevel1 (w)
            modifymod_support.init(w, top, *args, **kwargs)
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

            def backs(self):
                root.destroy()
                print("skdh")



            def submit4(self):
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
                v=str(self.txt_village.get());



                localtime=str(time.asctime(time.localtime(time.time())))

                t=int(i)
                u=int(o)
                p=str(t-u)


                database = DBConnect(host='localhost',user='root',password='Pass@123',database='etax2019')
                new_user = {'village':v,'idnumber': a,'meternumber': c,'wardnumber': d,'name': b,'housetax': e,'healthtax': f,'lighttax': g,'watertax': h,'total': i,'reciptnumber':j,'housetaxpaid':k,'healthtaxpaid':l,'lighttaxpaid':m,'watertaxpaid':n,'totalpaid':o,'rest':p}
                database.insert(new_user,'updateddata')
                database.commit()

                content1="WARNING   !!!!!! \n\n\n     Hi there is a New request to modify eTAX 2019 database \n Here are details: \n Village Name : "+v+"\n\n"
                content2="\nReciept Number :"+j+"\nName :"+b+"\nID Number :"+a+"\nMeter Number :"+c+"\nWard Number :"+d+"\nHouse Tax :"+e+"\nHealth Tax :"+f+"\nLight Tax :"+g+"\nWater Tax :"+h+"\nTotal Ammount of tax to be paid :"+i+"\nPaid House Tax :"+k+"\nPaid Health Tax :"+l+"\nPaid Light Tax :"+m+"\nPiad Water Tax :"+n+"\nTotal Tax paid  :"+o
                totcontaint=content1+content2 


                mail= smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login('etaxsupp2019@gmail.com','Pass@123')
                mail.sendmail('etaxsupp2019@gmail.com','kulkarnipranesh1767@gmail.com',totcontaint)
                mail.close()
                messagebox.showinfo("etax-2019","Data Deleted Successfully")
                root.destroy()





            def __init__(self, top=None):
                '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
                _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
                _fgcolor = '#000000'  # X11 color: 'black'
                _compcolor = '#d9d9d9' # X11 color: 'gray85'
                _ana1color = '#d9d9d9' # X11 color: 'gray85'
                _ana2color = '#ececec' # Closest X11 color: 'gray92'

                top.geometry("1043x729+179+114")
                top.title("New Toplevel")
                top.configure(background="#515154")
                top.configure(highlightbackground="#d9d9d9")
                top.configure(highlightcolor="black")

                self.Label1 = tk.Label(top)
                self.Label1.place(relx=0.019, rely=0.027, height=81, width=156)
                self.Label1.configure(activebackground="#f9f9f9")
                self.Label1.configure(activeforeground="black")
                self.Label1.configure(background="#515154")
                self.Label1.configure(disabledforeground="#a3a3a3")
                self.Label1.configure(font="-family {Britannic Bold} -size 48 -weight bold")
                self.Label1.configure(foreground="#ff250d")
                self.Label1.configure(highlightbackground="#d9d9d9")
                self.Label1.configure(highlightcolor="black")
                self.Label1.configure(text='''eTAX''')

                self.Label1_1 = tk.Label(top)
                self.Label1_1.place(relx=0.173, rely=0.027, height=81, width=156)
                self.Label1_1.configure(activebackground="#f9f9f9")
                self.Label1_1.configure(activeforeground="black")
                self.Label1_1.configure(background="#515154")
                self.Label1_1.configure(disabledforeground="#a3a3a3")
                self.Label1_1.configure(font="-family {Britannic Bold} -size 48 -weight bold")
                self.Label1_1.configure(foreground="#2212ff")
                self.Label1_1.configure(highlightbackground="#d9d9d9")
                self.Label1_1.configure(highlightcolor="black")
                self.Label1_1.configure(text='''2019''')

                self.Label2 = tk.Label(top)
                self.Label2.place(relx=0.105, rely=0.123, height=31, width=141)
                self.Label2.configure(activebackground="#f9f9f9")
                self.Label2.configure(activeforeground="black")
                self.Label2.configure(background="#515154")
                self.Label2.configure(disabledforeground="#a3a3a3")
                self.Label2.configure(font="-family {Segoe Script} -size 12 -slant italic")
                self.Label2.configure(foreground="#f7ff0d")
                self.Label2.configure(highlightbackground="#d9d9d9")
                self.Label2.configure(highlightcolor="black")
                self.Label2.configure(text='''working for you''')

                self.backbutton = tk.Button(top)
                self.backbutton.place(relx=0.058, rely=0.192, height=44, width=97)
                self.backbutton.configure(activebackground="#ececec")
                self.backbutton.configure(activeforeground="#000000")
                self.backbutton.configure(background="#120bd8")
                self.backbutton.configure(borderwidth="10")
                self.backbutton.configure(disabledforeground="#a3a3a3")
                self.backbutton.configure(font="-family {Rockwell Extra Bold} -size 12 -weight bold")
                self.backbutton.configure(foreground="#fcffff")
                self.backbutton.configure(highlightbackground="#d9d9d9")
                self.backbutton.configure(highlightcolor="black")
                self.backbutton.configure(pady="0")
                self.backbutton.configure(text='''Back''',command = self.backs)

                self.exit = tk.Button(top)
                self.exit.place(relx=0.163, rely=0.192, height=44, width=97)
                self.exit.configure(activebackground="#ececec")
                self.exit.configure(activeforeground="#000000")
                self.exit.configure(background="#120bd8")
                self.exit.configure(borderwidth="10")
                self.exit.configure(disabledforeground="#a3a3a3")
                self.exit.configure(font="-family {Rockwell Extra Bold} -size 12 -weight bold")
                self.exit.configure(foreground="#fcffff")
                self.exit.configure(highlightbackground="#d9d9d9")
                self.exit.configure(highlightcolor="black")
                self.exit.configure(pady="0")
                self.exit.configure(text='''Exit''',command = self.exits)

                self.Label4 = tk.Label(top)
                self.Label4.place(relx=0.326, rely=0.041, height=68, width=699)
                self.Label4.configure(activebackground="#f9f9f9")
                self.Label4.configure(activeforeground="black")
                self.Label4.configure(background="#515154")
                self.Label4.configure(disabledforeground="#36911a")
                self.Label4.configure(font="-family {Rockwell Extra Bold} -size 40 -weight bold")
                self.Label4.configure(foreground="#fff71c")
                self.Label4.configure(highlightbackground="#d9d9d9")
                self.Label4.configure(highlightcolor="black")
                self.Label4.configure(text='''DATA MODIFICATION''')
                self.Label4.configure(width=699)

                self.Frame1 = tk.Frame(top)
                self.Frame1.place(relx=0.24, rely=0.274, relheight=0.569, relwidth=0.292)

                self.Frame1.configure(relief='ridge')
                self.Frame1.configure(borderwidth="10")
                self.Frame1.configure(relief='ridge')
                self.Frame1.configure(background="#50e82a")
                self.Frame1.configure(highlightbackground="#d9d9d9")
                self.Frame1.configure(highlightcolor="black")
                self.Frame1.configure(width=305)

                self.txt_idnumber = tk.Entry(self.Frame1)
                self.txt_idnumber.place(relx=0.426, rely=0.096, height=20
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
                self.Label7_1.place(relx=0.033, rely=0.169, height=39, width=106)
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
                self.Label7_2.place(relx=0.033, rely=0.289, height=29, width=116)
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
                self.Label7_3.place(relx=0.033, rely=0.361, height=39, width=116)
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
                self.Label7_4.place(relx=0.033, rely=0.458, height=39, width=106)
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
                self.Label7_5.place(relx=0.033, rely=0.554, height=39, width=106)
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
                self.Label7_6.place(relx=0.033, rely=0.651, height=39, width=106)
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
                self.Label7_7.place(relx=0.033, rely=0.747, height=39, width=106)
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
                self.Label7_8.place(relx=0.033, rely=0.843, height=39, width=106)
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
                self.txt_name.place(relx=0.426, rely=0.193,height=20, relwidth=0.538)
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
                self.txt_meternumber.place(relx=0.426, rely=0.289, height=20
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
                self.txt_wardnumber.place(relx=0.426, rely=0.361, height=20
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
                self.txt_house.place(relx=0.393, rely=0.482,height=20, relwidth=0.538)
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
                self.txt_total.place(relx=0.393, rely=0.867,height=20, relwidth=0.538)
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
                self.txt_light.place(relx=0.393, rely=0.675,height=20, relwidth=0.538)
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
                self.txt_health.place(relx=0.393, rely=0.578,height=20, relwidth=0.538)
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
                self.txt_water.place(relx=0.393, rely=0.771,height=20, relwidth=0.538)
                self.txt_water.configure(background="white")
                self.txt_water.configure(disabledforeground="#a3a3a3")
                self.txt_water.configure(font="TkFixedFont")
                self.txt_water.configure(foreground="#000000")
                self.txt_water.configure(highlightbackground="#d9d9d9")
                self.txt_water.configure(highlightcolor="black")
                self.txt_water.configure(insertbackground="black")
                self.txt_water.configure(selectbackground="#c4c4c4")
                self.txt_water.configure(selectforeground="black")

                self.Label7 = tk.Label(self.Frame1)
                self.Label7.place(relx=0.066, rely=0.072, height=39, width=106)
                self.Label7.configure(activebackground="#f9f9f9")
                self.Label7.configure(activeforeground="black")
                self.Label7.configure(background="#50e82a")
                self.Label7.configure(disabledforeground="#a3a3a3")
                self.Label7.configure(font="-family {Plantagenet Cherokee} -size 13")
                self.Label7.configure(foreground="#000000")
                self.Label7.configure(highlightbackground="#d9d9d9")
                self.Label7.configure(highlightcolor="black")
                self.Label7.configure(text='''ID Number :''')

                self.Frame1_20 = tk.Frame(top)
                self.Frame1_20.place(relx=0.537, rely=0.37, relheight=0.473
                        , relwidth=0.292)
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

                self.Label7_2 = tk.Label(self.Frame1_20)
                self.Label7_2.place(relx=0.033, rely=0.203, height=39, width=126)
                self.Label7_2.configure(activebackground="#f9f9f9")
                self.Label7_2.configure(activeforeground="black")
                self.Label7_2.configure(background="#50e82a")
                self.Label7_2.configure(disabledforeground="#a3a3a3")
                self.Label7_2.configure(font="-family {Plantagenet Cherokee} -size 13")
                self.Label7_2.configure(foreground="#000000")
                self.Label7_2.configure(highlightbackground="#d9d9d9")
                self.Label7_2.configure(highlightcolor="black")
                self.Label7_2.configure(text='''Housetax(Paid) :''')

                self.Label7_3 = tk.Label(self.Frame1_20)
                self.Label7_3.place(relx=0.033, rely=0.319, height=39, width=126)
                self.Label7_3.configure(activebackground="#f9f9f9")
                self.Label7_3.configure(activeforeground="black")
                self.Label7_3.configure(background="#50e82a")
                self.Label7_3.configure(disabledforeground="#a3a3a3")
                self.Label7_3.configure(font="-family {Plantagenet Cherokee} -size 13")
                self.Label7_3.configure(foreground="#000000")
                self.Label7_3.configure(highlightbackground="#d9d9d9")
                self.Label7_3.configure(highlightcolor="black")
                self.Label7_3.configure(text='''Healthtax (Paid) :''')

                self.Label7_4 = tk.Label(self.Frame1_20)
                self.Label7_4.place(relx=0.066, rely=0.435, height=39, width=116)
                self.Label7_4.configure(activebackground="#f9f9f9")
                self.Label7_4.configure(activeforeground="black")
                self.Label7_4.configure(background="#50e82a")
                self.Label7_4.configure(disabledforeground="#a3a3a3")
                self.Label7_4.configure(font="-family {Plantagenet Cherokee} -size 13")
                self.Label7_4.configure(foreground="#000000")
                self.Label7_4.configure(highlightbackground="#d9d9d9")
                self.Label7_4.configure(highlightcolor="black")
                self.Label7_4.configure(text='''Lighttax(Paid) :''')

                self.Label7_5 = tk.Label(self.Frame1_20)
                self.Label7_5.place(relx=0.033, rely=0.551, height=39, width=116)
                self.Label7_5.configure(activebackground="#f9f9f9")
                self.Label7_5.configure(activeforeground="black")
                self.Label7_5.configure(background="#50e82a")
                self.Label7_5.configure(disabledforeground="#a3a3a3")
                self.Label7_5.configure(font="-family {Plantagenet Cherokee} -size 13")
                self.Label7_5.configure(foreground="#000000")
                self.Label7_5.configure(highlightbackground="#d9d9d9")
                self.Label7_5.configure(highlightcolor="black")
                self.Label7_5.configure(text='''Watertax(Paid) :''')

                self.Label7_6 = tk.Label(self.Frame1_20)
                self.Label7_6.place(relx=0.033, rely=0.667, height=39, width=106)
                self.Label7_6.configure(activebackground="#f9f9f9")
                self.Label7_6.configure(activeforeground="black")
                self.Label7_6.configure(background="#50e82a")
                self.Label7_6.configure(disabledforeground="#a3a3a3")
                self.Label7_6.configure(font="-family {Plantagenet Cherokee} -size 13")
                self.Label7_6.configure(foreground="#000000")
                self.Label7_6.configure(highlightbackground="#d9d9d9")
                self.Label7_6.configure(highlightcolor="black")
                self.Label7_6.configure(text='''Total (Paid) :''')

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
                self.btn_submit.configure(text='''SUBMIT''',command = self.submit4)

                self.Frame1_21 = tk.Frame(top)
                self.Frame1_21.place(relx=0.537, rely=0.274, relheight=0.089
                        , relwidth=0.292)
                self.Frame1_21.configure(relief='ridge')
                self.Frame1_21.configure(borderwidth="10")
                self.Frame1_21.configure(relief='ridge')
                self.Frame1_21.configure(background="#50e82a")
                self.Frame1_21.configure(highlightbackground="#d9d9d9")
                self.Frame1_21.configure(highlightcolor="black")
                self.Frame1_21.configure(width=305)

                self.Label7_22 = tk.Label(self.Frame1_21)
                self.Label7_22.place(relx=0.033, rely=0.154, height=39, width=126)
                self.Label7_22.configure(activebackground="#f9f9f9")
                self.Label7_22.configure(activeforeground="black")
                self.Label7_22.configure(background="#50e82a")
                self.Label7_22.configure(disabledforeground="#a3a3a3")
                self.Label7_22.configure(font="-family {Plantagenet Cherokee} -size 13")
                self.Label7_22.configure(foreground="#000000")
                self.Label7_22.configure(highlightbackground="#d9d9d9")
                self.Label7_22.configure(highlightcolor="black")
                self.Label7_22.configure(text='''Village Name :''')

                self.txt_village = tk.Entry(self.Frame1_21)
                self.txt_village.place(relx=0.492, rely=0.308, height=20, relwidth=0.439)

                self.txt_village.configure(background="white")
                self.txt_village.configure(disabledforeground="#a3a3a3")
                self.txt_village.configure(font="TkFixedFont")
                self.txt_village.configure(foreground="#000000")
                self.txt_village.configure(highlightbackground="#d9d9d9")
                self.txt_village.configure(highlightcolor="black")
                self.txt_village.configure(insertbackground="black")
                self.txt_village.configure(selectbackground="#c4c4c4")
                self.txt_village.configure(selectforeground="black")

        if __name__ == '__main__':
            vp_start_gui()























































    def delete1():
    	    #! /usr/bin/env python
        #  -*- coding: utf-8 -*-
        #
        # GUI module generated by PAGE version 4.21
        #  in conjunction with Tcl version 8.6
        #    Apr 22, 2019 04:53:59 PM +0530  platform: Windows NT

        import sys
        import tkinter
        from tkinter import messagebox
        import mysql.connector
        import time
        import dbConnect
        from dbConnect import DBConnect
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

        import deletedata_support
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
            top = e_TAX_2019 (root)
            deletedata_support.init(root, top)
            root.mainloop()

        w = None
        def create_e_TAX_2019(root, *args, **kwargs):
            '''Starting point when module is imported by another program.'''
            global w, w_win, rt
            global prog_location
            prog_call = sys.argv[0]
            print ('prog_call = {}'.format(prog_call))
            prog_location = os.path.split(prog_call)[0]
            print ('prog_location = {}'.format(prog_location))
            rt = root
            w = tk.Toplevel (root)
            top = e_TAX_2019 (w)
            deletedata_support.init(w, top, *args, **kwargs)
            return (w, top)

        def destroy_e_TAX_2019():
            global w
            w.destroy()
            w = None

        class e_TAX_2019:
            def exits(self):
                msg=tkinter.messagebox.askyesno("e-TAX 2019","Do You Want To EXIT ?")
                if msg :
                    exit()


            def backs(self):
                root.destroy()
                print("nwhcwjjwdj")


            def submit2(self):
                v=str(self.txt_villagename.get());
                n=str(self.txt_name.get());
                u=str(self.txt_uidnumber.get());

                t=str(time.asctime(time.localtime(time.time())))

                mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
                mycursor=mydb.cursor()
                query=("INSERT INTO deleteddata (village, uidnumber, name)VALUES(%s,%s,%s)")
                datac=(v,u,n)
                mycursor.execute(query,datac)
                mydb.commit()

                totcontaint=str("Warning !!!!! \n\n New Request To Delete Entry \n\n Some Entries has been changed \n\n Here are the details : \n\n\n Village Name :"+v+"\n UID Number :"+u+"\n Name Of individual"+n+"\n Data deleted on :"+t)
                mail= smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login('etaxsupp2019@gmail.com','Pass@123')
                mail.sendmail('etaxsupp2019@gmail.com','kulkarnipranesh1767@gmail.com',totcontaint)
                mail.close()
                messagebox.showinfo("e-TAX 2019","Successfully deleted The Entry")
                root.destroy()


            def __init__(self, top=None):
                '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
                _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
                _fgcolor = '#000000'  # X11 color: 'black'
                _compcolor = '#d9d9d9' # X11 color: 'gray85'
                _ana1color = '#d9d9d9' # X11 color: 'gray85'
                _ana2color = '#ececec' # Closest X11 color: 'gray92'
                font12 = "-family {Swatch it} -size 16"
                font13 = "-family {Segoe UI Black} -size 13 -weight bold"
                font14 = "-family {Shonar Bangla} -size 22"

                top.geometry("843x469+274+133")
                top.title("e-TAX 2019")
                top.configure(background="#727272")
                top.configure(highlightbackground="#d9d9d9")
                top.configure(highlightcolor="black")

                self.Frame1 = tk.Frame(top)
                self.Frame1.place(relx=0.012, rely=0.021, relheight=0.309
                        , relwidth=0.836)
                self.Frame1.configure(relief='ridge')
                self.Frame1.configure(borderwidth="10")
                self.Frame1.configure(relief='ridge')
                self.Frame1.configure(background="#595959")
                self.Frame1.configure(highlightbackground="#d9d9d9")
                self.Frame1.configure(highlightcolor="black")
                self.Frame1.configure(width=705)

                self.Label1 = tk.Label(self.Frame1)
                self.Label1.place(relx=0.043, rely=0.207, height=59, width=196)
                self.Label1.configure(activebackground="#f9f9f9")
                self.Label1.configure(activeforeground="black")
                self.Label1.configure(background="#595959")
                self.Label1.configure(disabledforeground="#a3a3a3")
                self.Label1.configure(font="-family {Rockwell Extra} -size 40 -weight bold")
                self.Label1.configure(foreground="#0d4dff")
                self.Label1.configure(highlightbackground="#d9d9d9")
                self.Label1.configure(highlightcolor="black")
                self.Label1.configure(text='''eTAX''')

                self.Label1_1 = tk.Label(self.Frame1)
                self.Label1_1.place(relx=0.298, rely=0.207, height=59, width=146)
                self.Label1_1.configure(activebackground="#f9f9f9")
                self.Label1_1.configure(activeforeground="black")
                self.Label1_1.configure(background="#595959")
                self.Label1_1.configure(disabledforeground="#a3a3a3")
                self.Label1_1.configure(font="-family {Rockwell Extra} -size 40 -weight bold")
                self.Label1_1.configure(foreground="#ff2b0a")
                self.Label1_1.configure(highlightbackground="#d9d9d9")
                self.Label1_1.configure(highlightcolor="black")
                self.Label1_1.configure(text='''2019''')

                self.Label2 = tk.Label(self.Frame1)
                self.Label2.place(relx=0.156, rely=0.621, height=31, width=184)
                self.Label2.configure(activebackground="#f9f9f9")
                self.Label2.configure(activeforeground="black")
                self.Label2.configure(background="#595959")
                self.Label2.configure(disabledforeground="#a3a3a3")
                self.Label2.configure(font="-family {Rage Italic} -size 19 -slant italic")
                self.Label2.configure(foreground="#f7ff0a")
                self.Label2.configure(highlightbackground="#d9d9d9")
                self.Label2.configure(highlightcolor="black")
                self.Label2.configure(text='''working for you''')

                self.Label1_2 = tk.Label(self.Frame1)
                self.Label1_2.place(relx=0.525, rely=0.207, height=69, width=306)
                self.Label1_2.configure(activebackground="#f9f9f9")
                self.Label1_2.configure(activeforeground="black")
                self.Label1_2.configure(background="#595959")
                self.Label1_2.configure(disabledforeground="#a3a3a3")
                self.Label1_2.configure(font="-family {Rockwell Extra} -size 28 -weight bold")
                self.Label1_2.configure(foreground="#5faa14")
                self.Label1_2.configure(highlightbackground="#d9d9d9")
                self.Label1_2.configure(highlightcolor="black")
                self.Label1_2.configure(text='''delete DATA''')
                self.Label1_2.configure(width=306)

                self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
                top.configure(menu = self.menubar)

                self.Label3 = tk.Label(top)
                self.Label3.place(relx=0.107, rely=0.448, height=39, width=186)
                self.Label3.configure(background="#727272")
                self.Label3.configure(disabledforeground="#a3a3a3")
                self.Label3.configure(font=font12)
                self.Label3.configure(foreground="#f7ff1c")
                self.Label3.configure(text='''Village Name :''')
                self.Label3.configure(width=186)

                self.Label3_1 = tk.Label(top)
                self.Label3_1.place(relx=0.107, rely=0.554, height=29, width=186)
                self.Label3_1.configure(activebackground="#f9f9f9")
                self.Label3_1.configure(activeforeground="black")
                self.Label3_1.configure(background="#727272")
                self.Label3_1.configure(disabledforeground="#a3a3a3")
                self.Label3_1.configure(font="-family {Swatch it} -size 16")
                self.Label3_1.configure(foreground="#f7ff1c")
                self.Label3_1.configure(highlightbackground="#d9d9d9")
                self.Label3_1.configure(highlightcolor="black")
                self.Label3_1.configure(text='''UID Number :''')

                self.Label3_2 = tk.Label(top)
                self.Label3_2.place(relx=0.142, rely=0.64, height=39, width=116)
                self.Label3_2.configure(activebackground="#f9f9f9")
                self.Label3_2.configure(activeforeground="black")
                self.Label3_2.configure(background="#727272")
                self.Label3_2.configure(disabledforeground="#a3a3a3")
                self.Label3_2.configure(font="-family {Swatch it} -size 16")
                self.Label3_2.configure(foreground="#f7ff1c")
                self.Label3_2.configure(highlightbackground="#d9d9d9")
                self.Label3_2.configure(highlightcolor="black")
                self.Label3_2.configure(text='''Name  :''')
                self.Label3_2.configure(width=116)

                self.txt_villagename = tk.Entry(top)
                self.txt_villagename.place(relx=0.368, rely=0.469, height=20
                        , relwidth=0.361)
                self.txt_villagename.configure(background="white")
                self.txt_villagename.configure(disabledforeground="#a3a3a3")
                self.txt_villagename.configure(font="TkFixedFont")
                self.txt_villagename.configure(foreground="#000000")
                self.txt_villagename.configure(insertbackground="black")
                self.txt_villagename.configure(width=304)

                self.txt_uidnumber = tk.Entry(top)
                self.txt_uidnumber.place(relx=0.368, rely=0.576, height=20
                        , relwidth=0.361)
                self.txt_uidnumber.configure(background="white")
                self.txt_uidnumber.configure(disabledforeground="#a3a3a3")
                self.txt_uidnumber.configure(font="TkFixedFont")
                self.txt_uidnumber.configure(foreground="#000000")
                self.txt_uidnumber.configure(highlightbackground="#d9d9d9")
                self.txt_uidnumber.configure(highlightcolor="black")
                self.txt_uidnumber.configure(insertbackground="black")
                self.txt_uidnumber.configure(selectbackground="#c4c4c4")
                self.txt_uidnumber.configure(selectforeground="black")

                self.txt_name = tk.Entry(top)
                self.txt_name.place(relx=0.368, rely=0.661,height=20, relwidth=0.361)
                self.txt_name.configure(background="white")
                self.txt_name.configure(disabledforeground="#a3a3a3")
                self.txt_name.configure(font="TkFixedFont")
                self.txt_name.configure(foreground="#000000")
                self.txt_name.configure(highlightbackground="#d9d9d9")
                self.txt_name.configure(highlightcolor="black")
                self.txt_name.configure(insertbackground="black")
                self.txt_name.configure(selectbackground="#c4c4c4")
                self.txt_name.configure(selectforeground="black")

                self.Label4 = tk.Label(top)
                self.Label4.place(relx=0.771, rely=0.49, height=100, width=174)
                self.Label4.configure(background="#d9d9d9")
                self.Label4.configure(borderwidth="10")
                self.Label4.configure(disabledforeground="#a3a3a3")
                self.Label4.configure(foreground="#000000")
                photo_location = os.path.join(prog_location,"./delete1.png")
                self._img0 = tk.PhotoImage(file=photo_location)
                self.Label4.configure(image=self._img0)
                self.Label4.configure(relief='raised')
                self.Label4.configure(text='''Label''')
                self.Label4.configure(width=174)

                self.btn_submit = tk.Button(top)
                self.btn_submit.place(relx=0.427, rely=0.832, height=54, width=194)
                self.btn_submit.configure(activebackground="#ececec")
                self.btn_submit.configure(activeforeground="#000000")
                self.btn_submit.configure(background="#3920d8")
                self.btn_submit.configure(borderwidth="10")
                self.btn_submit.configure(disabledforeground="#a3a3a3")
                self.btn_submit.configure(font=font13)
                self.btn_submit.configure(foreground="#ffffff")
                self.btn_submit.configure(highlightbackground="#d9d9d9")
                self.btn_submit.configure(highlightcolor="black")
                self.btn_submit.configure(pady="0")
                self.btn_submit.configure(text='''I Wish To Continue''',command = self.submit2)

                self.Label5 = tk.Label(top)
                self.Label5.place(relx=0.095, rely=0.725, height=43, width=560)
                self.Label5.configure(background="#727272")
                self.Label5.configure(disabledforeground="#a3a3a3")
                self.Label5.configure(font=font14)
                self.Label5.configure(foreground="#5bff3b")
                self.Label5.configure(text='''Disclaimer :  You Can Not recover the data once deleted''')

                self.btn_exit = tk.Button(top)
                self.btn_exit.place(relx=0.866, rely=0.192, height=44, width=104)
                self.btn_exit.configure(activebackground="#ececec")
                self.btn_exit.configure(activeforeground="#000000")
                self.btn_exit.configure(background="#ff3f0f")
                self.btn_exit.configure(borderwidth="10")
                self.btn_exit.configure(disabledforeground="#a3a3a3")
                self.btn_exit.configure(font="-family {Segoe UI Black} -size 13 -weight bold")
                self.btn_exit.configure(foreground="#ffffff")
                self.btn_exit.configure(highlightbackground="#d9d9d9")
                self.btn_exit.configure(highlightcolor="black")
                self.btn_exit.configure(pady="0")
                self.btn_exit.configure(text='''EXIT''',command = self.exits)
                self.btn_exit.configure(width=104)

                self.btn_back = tk.Button(top)
                self.btn_back.place(relx=0.866, rely=0.064, height=44, width=104)
                self.btn_back.configure(activebackground="#ececec")
                self.btn_back.configure(activeforeground="#000000")
                self.btn_back.configure(background="#3ba825")
                self.btn_back.configure(borderwidth="10")
                self.btn_back.configure(disabledforeground="#a3a3a3")
                self.btn_back.configure(font="-family {Segoe UI Black} -size 13 -weight bold")
                self.btn_back.configure(foreground="#ffffff")
                self.btn_back.configure(highlightbackground="#d9d9d9")
                self.btn_back.configure(highlightcolor="black")
                self.btn_back.configure(pady="0")
                self.btn_back.configure(text='''BACK''',command = self.backs)

        if __name__ == '__main__':
            vp_start_gui()



















































    class e_TAX_2019:


        def backs(self):
            root.destroy()
            print("duchdhci")

        def exits(self):
            msg=tkinter.messagebox.askyesno("eTAX 2019","Do you want to exit")
            if msg :
                exit()

        def accesss(self):
            root.destroy()
            access1()


        def deletes(self):
            root.destroy()
            delete1()

        def modifys(self):
            root.destroy()
            modify1()

        def __init__(self, top=None):
            '''This class configures and populates the toplevel window.
               top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9' # X11 color: 'gray85'
            _ana1color = '#d9d9d9' # X11 color: 'gray85'
            _ana2color = '#ececec' # Closest X11 color: 'gray92'
            font10 = "-family {Rockwell Extra} -size 40 -weight bold"
            font11 = "-family {Rage Italic} -size 19 -slant italic"
            font12 = "-family {Rockwell Extra} -size 28 -weight bold"
            font15 = "-family {Segoe UI Black} -size 23 -weight bold"
            font16 = "-family {Postmaster} -size 13"

            top.geometry("990x650+274+133")
            top.title("e-TAX 2019")
            top.configure(background="#727272")

            self.Frame1 = tk.Frame(top)
            self.Frame1.place(relx=0.091, rely=0.046, relheight=0.223
                    , relwidth=0.843)
            self.Frame1.configure(relief='ridge')
            self.Frame1.configure(borderwidth="10")
            self.Frame1.configure(relief='ridge')
            self.Frame1.configure(background="#595959")
            self.Frame1.configure(width=835)

            self.Label1 = tk.Label(self.Frame1)
            self.Label1.place(relx=0.036, rely=0.207, height=59, width=196)
            self.Label1.configure(background="#595959")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font=font10)
            self.Label1.configure(foreground="#0d4dff")
            self.Label1.configure(text='''eTAX''')
            self.Label1.configure(width=196)

            self.Label1_1 = tk.Label(self.Frame1)
            self.Label1_1.place(relx=0.251, rely=0.207, height=59, width=146)
            self.Label1_1.configure(activebackground="#f9f9f9")
            self.Label1_1.configure(activeforeground="black")
            self.Label1_1.configure(background="#595959")
            self.Label1_1.configure(disabledforeground="#a3a3a3")
            self.Label1_1.configure(font="-family {Rockwell Extra} -size 40 -weight bold")
            self.Label1_1.configure(foreground="#ff2b0a")
            self.Label1_1.configure(highlightbackground="#d9d9d9")
            self.Label1_1.configure(highlightcolor="black")
            self.Label1_1.configure(text='''2019''')
            self.Label1_1.configure(width=146)

            self.Label2 = tk.Label(self.Frame1)
            self.Label2.place(relx=0.132, rely=0.621, height=31, width=184)
            self.Label2.configure(background="#595959")
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(font=font11)
            self.Label2.configure(foreground="#f7ff0a")
            self.Label2.configure(text='''working for you''')
            self.Label2.configure(width=184)

            self.Label1_2 = tk.Label(self.Frame1)
            self.Label1_2.place(relx=0.431, rely=0.207, height=69, width=446)
            self.Label1_2.configure(activebackground="#f9f9f9")
            self.Label1_2.configure(activeforeground="black")
            self.Label1_2.configure(background="#595959")
            self.Label1_2.configure(disabledforeground="#a3a3a3")
            self.Label1_2.configure(font=font12)
            self.Label1_2.configure(foreground="#5faa14")
            self.Label1_2.configure(highlightbackground="#d9d9d9")
            self.Label1_2.configure(highlightcolor="black")
            self.Label1_2.configure(text='''UPDATE DATABASE''')
            self.Label1_2.configure(width=446)

            self.Frame2 = tk.Frame(top)
            self.Frame2.place(relx=0.01, rely=0.369, relheight=0.531, relwidth=0.328)

            self.Frame2.configure(relief='ridge')
            self.Frame2.configure(borderwidth="10")
            self.Frame2.configure(relief='ridge')
            self.Frame2.configure(background="#595959")
            self.Frame2.configure(width=325)

            self.Label3 = tk.Label(self.Frame2)
            self.Label3.place(relx=0.123, rely=0.638, height=45, width=234)
            self.Label3.configure(background="#595959")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(font=font15)
            self.Label3.configure(foreground="#efff0f")
            self.Label3.configure(text='''MODIFY DATA''')
            self.Label3.configure(width=234)

            self.Label4 = tk.Label(self.Frame2)
            self.Label4.place(relx=0.154, rely=0.783, height=22, width=213)
            self.Label4.configure(background="#595959")
            self.Label4.configure(disabledforeground="#a3a3a3")
            self.Label4.configure(font=font16)
            self.Label4.configure(foreground="#4cad1c")
            self.Label4.configure(text='''CLICK HERE TO UPDATE''')

            self.Label4_3 = tk.Label(self.Frame2)
            self.Label4_3.place(relx=0.338, rely=0.841, height=32, width=83)
            self.Label4_3.configure(activebackground="#f9f9f9")
            self.Label4_3.configure(activeforeground="black")
            self.Label4_3.configure(background="#595959")
            self.Label4_3.configure(disabledforeground="#a3a3a3")
            self.Label4_3.configure(font="-family {Postmaster} -size 13")
            self.Label4_3.configure(foreground="#4cad1c")
            self.Label4_3.configure(highlightbackground="#d9d9d9")
            self.Label4_3.configure(highlightcolor="black")
            self.Label4_3.configure(text='''DATA''')
            self.Label4_3.configure(width=83)

            self.btn_modify = tk.Button(self.Frame2)
            self.btn_modify.place(relx=0.215, rely=0.058, height=186, width=186)
            self.btn_modify.configure(activebackground="#ececec")
            self.btn_modify.configure(activeforeground="#000000")
            self.btn_modify.configure(background="#d9d9d9")
            self.btn_modify.configure(disabledforeground="#a3a3a3")
            self.btn_modify.configure(foreground="#000000")
            self.btn_modify.configure(highlightbackground="#d9d9d9")
            self.btn_modify.configure(highlightcolor="black")
            photo_location = os.path.join(prog_location,"./updatepic1.png")
            self._img0 = tk.PhotoImage(file=photo_location)
            self.btn_modify.configure(image=self._img0)
            self.btn_modify.configure(pady="0")
            self.btn_modify.configure(text='''Button''',command= self.modifys)
            self.btn_modify.configure(width=186)

            self.Frame2_4 = tk.Frame(top)
            self.Frame2_4.place(relx=0.333, rely=0.369, relheight=0.531
                    , relwidth=0.328)
            self.Frame2_4.configure(relief='ridge')
            self.Frame2_4.configure(borderwidth="10")
            self.Frame2_4.configure(relief='ridge')
            self.Frame2_4.configure(background="#595959")
            self.Frame2_4.configure(highlightbackground="#d9d9d9")
            self.Frame2_4.configure(highlightcolor="black")
            self.Frame2_4.configure(width=325)

            self.Label3_5 = tk.Label(self.Frame2_4)
            self.Label3_5.place(relx=0.123, rely=0.638, height=45, width=234)
            self.Label3_5.configure(activebackground="#f9f9f9")
            self.Label3_5.configure(activeforeground="black")
            self.Label3_5.configure(background="#595959")
            self.Label3_5.configure(disabledforeground="#a3a3a3")
            self.Label3_5.configure(font="-family {Segoe UI Black} -size 23 -weight bold")
            self.Label3_5.configure(foreground="#efff0f")
            self.Label3_5.configure(highlightbackground="#d9d9d9")
            self.Label3_5.configure(highlightcolor="black")
            self.Label3_5.configure(text='''DELETE DATA''')

            self.Label4_6 = tk.Label(self.Frame2_4)
            self.Label4_6.place(relx=0.154, rely=0.783, height=22, width=209)
            self.Label4_6.configure(activebackground="#f9f9f9")
            self.Label4_6.configure(activeforeground="black")
            self.Label4_6.configure(background="#595959")
            self.Label4_6.configure(disabledforeground="#a3a3a3")
            self.Label4_6.configure(font="-family {Postmaster} -size 13")
            self.Label4_6.configure(foreground="#4cad1c")
            self.Label4_6.configure(highlightbackground="#d9d9d9")
            self.Label4_6.configure(highlightcolor="black")
            self.Label4_6.configure(text='''CLICK HERE TO DELETE''')

            self.Label4_4 = tk.Label(self.Frame2_4)
            self.Label4_4.place(relx=0.338, rely=0.841, height=32, width=83)
            self.Label4_4.configure(activebackground="#f9f9f9")
            self.Label4_4.configure(activeforeground="black")
            self.Label4_4.configure(background="#595959")
            self.Label4_4.configure(disabledforeground="#a3a3a3")
            self.Label4_4.configure(font="-family {Postmaster} -size 13")
            self.Label4_4.configure(foreground="#4cad1c")
            self.Label4_4.configure(highlightbackground="#d9d9d9")
            self.Label4_4.configure(highlightcolor="black")
            self.Label4_4.configure(text='''DATA''')

            self.btn_delete = tk.Button(self.Frame2_4)
            self.btn_delete.place(relx=0.185, rely=0.174, height=122, width=206)
            self.btn_delete.configure(activebackground="#ececec")
            self.btn_delete.configure(activeforeground="#000000")
            self.btn_delete.configure(background="#d9d9d9")
            self.btn_delete.configure(disabledforeground="#a3a3a3")
            self.btn_delete.configure(foreground="#000000")
            self.btn_delete.configure(highlightbackground="#d9d9d9")
            self.btn_delete.configure(highlightcolor="black")
            photo_location = os.path.join(prog_location,"./delete1.png")
            self._img1 = tk.PhotoImage(file=photo_location)
            self.btn_delete.configure(image=self._img1)
            self.btn_delete.configure(pady="0")
            self.btn_delete.configure(text='''Button''',command= self.deletes)

            self.Frame2_5 = tk.Frame(top)
            self.Frame2_5.place(relx=0.657, rely=0.369, relheight=0.531
                    , relwidth=0.328)
            self.Frame2_5.configure(relief='ridge')
            self.Frame2_5.configure(borderwidth="10")
            self.Frame2_5.configure(relief='ridge')
            self.Frame2_5.configure(background="#595959")
            self.Frame2_5.configure(highlightbackground="#d9d9d9")
            self.Frame2_5.configure(highlightcolor="black")
            self.Frame2_5.configure(width=325)

            self.Label3_6 = tk.Label(self.Frame2_5)
            self.Label3_6.place(relx=0.123, rely=0.638, height=45, width=234)
            self.Label3_6.configure(activebackground="#f9f9f9")
            self.Label3_6.configure(activeforeground="black")
            self.Label3_6.configure(background="#595959")
            self.Label3_6.configure(disabledforeground="#a3a3a3")
            self.Label3_6.configure(font="-family {Segoe UI Black} -size 23 -weight bold")
            self.Label3_6.configure(foreground="#efff0f")
            self.Label3_6.configure(highlightbackground="#d9d9d9")
            self.Label3_6.configure(highlightcolor="black")
            self.Label3_6.configure(text='''PERMISSION''')

            self.Label4_7 = tk.Label(self.Frame2_5)
            self.Label4_7.place(relx=0.154, rely=0.783, height=22, width=219)
            self.Label4_7.configure(activebackground="#f9f9f9")
            self.Label4_7.configure(activeforeground="black")
            self.Label4_7.configure(background="#595959")
            self.Label4_7.configure(disabledforeground="#a3a3a3")
            self.Label4_7.configure(font="-family {Postmaster} -size 13")
            self.Label4_7.configure(foreground="#4cad1c")
            self.Label4_7.configure(highlightbackground="#d9d9d9")
            self.Label4_7.configure(highlightcolor="black")
            self.Label4_7.configure(text='''CLICK HERE TO ASK FOR''')

            self.Label4_4 = tk.Label(self.Frame2_5)
            self.Label4_4.place(relx=0.338, rely=0.841, height=32, width=103)
            self.Label4_4.configure(activebackground="#f9f9f9")
            self.Label4_4.configure(activeforeground="black")
            self.Label4_4.configure(background="#595959")
            self.Label4_4.configure(disabledforeground="#a3a3a3")
            self.Label4_4.configure(font="-family {Postmaster} -size 13")
            self.Label4_4.configure(foreground="#4cad1c")
            self.Label4_4.configure(highlightbackground="#d9d9d9")
            self.Label4_4.configure(highlightcolor="black")
            self.Label4_4.configure(text='''PERMISSION''')
            self.Label4_4.configure(width=103)

            self.btn_access = tk.Button(self.Frame2_5)
            self.btn_access.place(relx=0.185, rely=0.174, height=139, width=206)
            self.btn_access.configure(activebackground="#ececec")
            self.btn_access.configure(activeforeground="#000000")
            self.btn_access.configure(background="#d9d9d9")
            self.btn_access.configure(disabledforeground="#a3a3a3")
            self.btn_access.configure(foreground="#000000")
            self.btn_access.configure(highlightbackground="#d9d9d9")
            self.btn_access.configure(highlightcolor="black")
            photo_location = os.path.join(prog_location,"./access.png")
            self._img2 = tk.PhotoImage(file=photo_location)
            self.btn_access.configure(image=self._img2)
            self.btn_access.configure(pady="0")
            self.btn_access.configure(text='''Button''',command= self.accesss)

            self.btn_exit = tk.Button(top)
            self.btn_exit.place(relx=0.869, rely=0.292, height=40, width=90)
            self.btn_exit.configure(activebackground="#ececec")
            self.btn_exit.configure(activeforeground="#000000")
            self.btn_exit.configure(background="#264aff")
            self.btn_exit.configure(borderwidth="10")
            self.btn_exit.configure(disabledforeground="#a3a3a3")
            self.btn_exit.configure(foreground="#ffffff")
            self.btn_exit.configure(highlightbackground="#d9d9d9")
            self.btn_exit.configure(highlightcolor="black")
            self.btn_exit.configure(pady="0")
            self.btn_exit.configure(text='''EXIT''')
            self.btn_exit.configure(width=90,command= self.exits)

            self.btn_back = tk.Button(top)
            self.btn_back.place(relx=0.747, rely=0.292, height=40, width=90)
            self.btn_back.configure(activebackground="#ececec")
            self.btn_back.configure(activeforeground="#000000")
            self.btn_back.configure(background="#264aff")
            self.btn_back.configure(borderwidth="10")
            self.btn_back.configure(disabledforeground="#a3a3a3")
            self.btn_back.configure(foreground="#ffffff")
            self.btn_back.configure(highlightbackground="#d9d9d9")
            self.btn_back.configure(highlightcolor="black")
            self.btn_back.configure(pady="0")
            self.btn_back.configure(text='''BACK''',command= self.backs)

    if __name__ == '__main__':
        vp_start_gui()





