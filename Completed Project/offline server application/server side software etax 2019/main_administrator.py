def view():
    import sys
    import mysql.connector

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
        top = Toplevel1 (root)
        unknown_support.init(root, top)
        root.mainloop()

    w = None
    def create_Toplevel1(root, *args, **kwargs):
        '''Starting point when module is imported by another program.'''
        global w, w_win, rt
        rt = root
        w = tk.Toplevel (root)
        top = Toplevel1 (w)
        unknown_support.init(w, top, *args, **kwargs)
        return (w, top)

    def destroy_Toplevel1():
        global w
        w.destroy()
        w = None

    class Toplevel1:
        def delets(self):
            try :
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
            except :
                tkinter.messagebox.showerror('etax-2019','Failed to connect server, Please contact your administrator')
            
            mycursor=mydb.cursor()
            query = ("SELECT village, uidnumber, name FROM deleteddata")
            mycursor.execute(query)
            for(village, uidnumber, name) in mycursor:
                s="{}            {}          {}".format(village, uidnumber, name)
                self.box2o1.insert(0,s)

        def updates(self):
            try :
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
            except :
                tkinter.messagebox.showerror('etax-2019','Failed to connect server, Please contact your administrator')
            
            mycursor=mydb.cursor()
            query = ("SELECT village,idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest FROM updateddata")
            mycursor.execute(query)
            for(village,idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest) in mycursor:
                s="{}        {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}     {}     {}".format(village,idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest)
                self.box2o1.insert(0,s)
        def clears(self):
            self.box2o1.delete(0,tk.END)





        def exits(self):
            exit()
        def backs(self):
            root.destroy()
            main()
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

            top.geometry("1516x821+37+31")
            top.title("New Toplevel")
            top.configure(background="#ffff24")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")

            self.Label1 = tk.Label(top)
            self.Label1.place(relx=0.013, rely=0.024, height=81, width=156)
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
            self.Label1_1.place(relx=0.119, rely=0.024, height=81, width=156)
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
            self.Label2.place(relx=0.073, rely=0.11, height=31, width=141)
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
            self.backbutton.place(relx=0.046, rely=0.171, height=44, width=97)
            self.backbutton.configure(activebackground="#ececec")
            self.backbutton.configure(activeforeground="#000000")
            self.backbutton.configure(background="#120bd8")
            self.backbutton.configure(disabledforeground="#a3a3a3")
            self.backbutton.configure(font="-family {Rockwell Extra Bold} -size 12 -weight bold")
            self.backbutton.configure(foreground="#fcffff")
            self.backbutton.configure(highlightbackground="#d9d9d9")
            self.backbutton.configure(highlightcolor="black")
            self.backbutton.configure(pady="0")
            self.backbutton.configure(text='''Back''',command=self.backs)

            self.exit = tk.Button(top)
            self.exit.place(relx=0.132, rely=0.171, height=44, width=97)
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
            self.Label3.place(relx=0.013, rely=0.962, height=21, width=56)
            self.Label3.configure(activebackground="#f9f9f9")
            self.Label3.configure(activeforeground="black")
            self.Label3.configure(background="#ffff24")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(foreground="#000000")
            self.Label3.configure(highlightbackground="#d9d9d9")
            self.Label3.configure(highlightcolor="black")
            self.Label3.configure(text='''etax-2019''')

            self.Label3_3 = tk.Label(top)
            self.Label3_3.place(relx=0.013, rely=0.987, height=21, width=34)
            self.Label3_3.configure(activebackground="#f9f9f9")
            self.Label3_3.configure(activeforeground="black")
            self.Label3_3.configure(background="#ffff24")
            self.Label3_3.configure(disabledforeground="#a3a3a3")
            self.Label3_3.configure(foreground="#000000")
            self.Label3_3.configure(highlightbackground="#d9d9d9")
            self.Label3_3.configure(highlightcolor="black")
            self.Label3_3.configure(text='''v 1.0.2''')

            self.Label3_4 = tk.Label(top)
            self.Label3_4.place(relx=0.007, rely=1.035, height=21, width=134)
            self.Label3_4.configure(activebackground="#f9f9f9")
            self.Label3_4.configure(activeforeground="black")
            self.Label3_4.configure(background="#ffff24")
            self.Label3_4.configure(disabledforeground="#a3a3a3")
            self.Label3_4.configure(foreground="#000000")
            self.Label3_4.configure(highlightbackground="#d9d9d9")
            self.Label3_4.configure(highlightcolor="black")
            self.Label3_4.configure(text='''Working On Windows''')

            self.Label3_1 = tk.Label(top)
            self.Label3_1.place(relx=0.013, rely=1.011, height=21, width=164)
            self.Label3_1.configure(activebackground="#f9f9f9")
            self.Label3_1.configure(activeforeground="black")
            self.Label3_1.configure(background="#ffff24")
            self.Label3_1.configure(disabledforeground="#a3a3a3")
            self.Label3_1.configure(foreground="#000000")
            self.Label3_1.configure(highlightbackground="#d9d9d9")
            self.Label3_1.configure(highlightcolor="black")
            self.Label3_1.configure(text='''Connected to MySQL server 8.0''')

            self.Label4 = tk.Label(top)
            self.Label4.place(relx=0.277, rely=0.037, height=68, width=968)
            self.Label4.configure(activebackground="#f9f9f9")
            self.Label4.configure(activeforeground="black")
            self.Label4.configure(background="#ffff24")
            self.Label4.configure(disabledforeground="#36911a")
            self.Label4.configure(font="-family {Rockwell Extra Bold} -size 40 -weight bold")
            self.Label4.configure(foreground="#36911a")
            self.Label4.configure(highlightbackground="#d9d9d9")
            self.Label4.configure(highlightcolor="black")
            self.Label4.configure(text='''DATA MODIFICATION REQUEST''')

            self.Label5_3 = tk.Label(top)
            self.Label5_3.place(relx=0.91, rely=0.95, height=28, width=172)
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
            self.Label5_4.place(relx=0.917, rely=1.011, height=28, width=172)
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
            self.Label5_5.place(relx=0.917, rely=1.035, height=28, width=172)
            self.Label5_5.configure(activebackground="#f9f9f9")
            self.Label5_5.configure(activeforeground="black")
            self.Label5_5.configure(background="#ffff24")
            self.Label5_5.configure(disabledforeground="#a3a3a3")
            self.Label5_5.configure(font="-family {Rockwell} -size 9")
            self.Label5_5.configure(foreground="#000000")
            self.Label5_5.configure(highlightbackground="#d9d9d9")
            self.Label5_5.configure(highlightcolor="black")
            self.Label5_5.configure(text='''Port : 3306''')

            self.box2o1 = ScrolledListBox(top)
            self.box2o1.place(relx=0.033, rely=0.268, relheight=0.652, relwidth=0.99)

            self.box2o1.configure(background="white")
            self.box2o1.configure(disabledforeground="#a3a3a3")
            self.box2o1.configure(font="TkFixedFont")
            self.box2o1.configure(foreground="black")
            self.box2o1.configure(highlightbackground="#d9d9d9")
            self.box2o1.configure(highlightcolor="#d9d9d9")
            self.box2o1.configure(selectbackground="#c4c4c4")
            self.box2o1.configure(selectforeground="black")
            self.box2o1.configure(width=10)

            self.TSeparator2 = ttk.Separator(top)
            self.TSeparator2.place(relx=0.013, rely=0.146, relwidth=0.204)

            self.TSeparator3 = ttk.Separator(top)
            self.TSeparator3.place(relx=0.013, rely=0.244, relwidth=0.989)

            self.deleted = tk.Button(top)
            self.deleted.place(relx=0.343, rely=0.938, height=33, width=148)
            self.deleted.configure(activebackground="#ececec")
            self.deleted.configure(activeforeground="#000000")
            self.deleted.configure(background="#2020d8")
            self.deleted.configure(disabledforeground="#a3a3a3")
            self.deleted.configure(font="-family {Rockwell} -size 13 -weight bold")
            self.deleted.configure(foreground="#ffffff")
            self.deleted.configure(highlightbackground="#d9d9d9")
            self.deleted.configure(highlightcolor="black")
            self.deleted.configure(pady="0")
            self.deleted.configure(takefocus="0")
            self.deleted.configure(text='''Deleted Data''',command= self.delets)

            self.viewbutton_9 = tk.Button(top)
            self.viewbutton_9.place(relx=0.594, rely=0.938, height=33, width=108)
            self.viewbutton_9.configure(activebackground="#ececec")
            self.viewbutton_9.configure(activeforeground="#000000")
            self.viewbutton_9.configure(background="#2020d8")
            self.viewbutton_9.configure(disabledforeground="#a3a3a3")
            self.viewbutton_9.configure(font="-family {Rockwell} -size 13 -weight bold")
            self.viewbutton_9.configure(foreground="#ffffff")
            self.viewbutton_9.configure(highlightbackground="#d9d9d9")
            self.viewbutton_9.configure(highlightcolor="black")
            self.viewbutton_9.configure(pady="0")
            self.viewbutton_9.configure(takefocus="0")
            self.viewbutton_9.configure(text='''Clear all''',command= self.clears)

            self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
            top.configure(menu = self.menubar)

            self.viewbutton_1 = tk.Button(top)
            self.viewbutton_1.place(relx=0.475, rely=0.938, height=33, width=148)
            self.viewbutton_1.configure(activebackground="#ececec")
            self.viewbutton_1.configure(activeforeground="#000000")
            self.viewbutton_1.configure(background="#2020d8")
            self.viewbutton_1.configure(disabledforeground="#a3a3a3")
            self.viewbutton_1.configure(font="-family {Rockwell} -size 13 -weight bold")
            self.viewbutton_1.configure(foreground="#ffffff")
            self.viewbutton_1.configure(highlightbackground="#d9d9d9")
            self.viewbutton_1.configure(highlightcolor="black")
            self.viewbutton_1.configure(pady="0")
            self.viewbutton_1.configure(takefocus="0")
            self.viewbutton_1.configure(text='''Updated Data''',command= self.updates)

            self.Label1_2 = tk.Label(top)
            self.Label1_2.place(relx=0.429, rely=0.122, height=81, width=516)
            self.Label1_2.configure(activebackground="#f9f9f9")
            self.Label1_2.configure(activeforeground="black")
            self.Label1_2.configure(background="#ffff24")
            self.Label1_2.configure(disabledforeground="#a3a3a3")
            self.Label1_2.configure(font="-family {Britannic Bold} -size 48 -weight bold")
            self.Label1_2.configure(foreground="#ff250d")
            self.Label1_2.configure(highlightbackground="#d9d9d9")
            self.Label1_2.configure(highlightcolor="black")
            self.Label1_2.configure(text='''ADMINISTRATOR''')
            self.Label1_2.configure(width=516)

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
























def delete():


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
            main()

        def submit2(self):
            v=str(self.txt_villagename.get());
            n=str(self.txt_name.get());
            u=str(self.txt_uidnumber.get());

            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
            mycursor=mydb.cursor()
            query=("INSERT INTO deleteddataper (village, uidnumber, name)VALUES(%s,%s,%s)")
            datac=(v,u,n)
            mycursor.execute(query,datac)
            mydb.commit()

            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
            mycursor=mydb.cursor()
            query=("DELETE from deleteddata where uidnumber = %s" %(u))
            mycursor.execute(query)
            mydb.commit()

            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
            mycursor=mydb.cursor()
            query=("DELETE from %s where idnumber = %s" %(v,u))
            mycursor.execute(query)
            mydb.commit()

            tkinter.messagebox.showinfo("etax2019","Data Successfully Deleted")


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
            font15 = "-family {Rockwell Extra} -size 18 -weight bold"

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

            self.Label3_1 = tk.Label(top)
            self.Label3_1.place(relx=0.32, rely=0.341, height=39, width=276)
            self.Label3_1.configure(activebackground="#f9f9f9")
            self.Label3_1.configure(activeforeground="black")
            self.Label3_1.configure(background="#727272")
            self.Label3_1.configure(disabledforeground="#a3a3a3")
            self.Label3_1.configure(font=font15)
            self.Label3_1.configure(foreground="#ff0a12")
            self.Label3_1.configure(highlightbackground="#d9d9d9")
            self.Label3_1.configure(highlightcolor="black")
            self.Label3_1.configure(text='''ADMINISTRATOR''')
            self.Label3_1.configure(width=276)

    if __name__ == '__main__':
        vp_start_gui()











































def update():

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
            main()



        def submit5(self):
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


            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
            mycursor=mydb.cursor()
            query=("DELETE from updateddata where idnumber = %s" %(a))
            mycursor.execute(query)
            mydb.commit()

            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
            mycursor=mydb.cursor()
            query=("DELETE from %s where idnumber = %s" %(v,a))
            mycursor.execute(query)
            mydb.commit()


            database = DBConnect(host='localhost',user='root',password='Pass@123',database='etax2019')
            new_user = {'village':v,'idnumber': a,'meternumber': c,'wardnumber': d,'name': b,'housetax': e,'healthtax': f,'lighttax': g,'watertax': h,'total': i,'reciptnumber':j,'housetaxpaid':k,'healthtaxpaid':l,'lighttaxpaid':m,'watertaxpaid':n,'totalpaid':o,'rest':p,'datei': localtime}
            database.insert(new_user,'updateddataper')
            mydb.commit()


            database = DBConnect(host='localhost',user='root',password='Pass@123',database='etax2019')
            new_user = {'idnumber': a,'meternumber': c,'wardnumber': d,'name': b,'housetax': e,'healthtax': f,'lighttax': g,'watertax': h,'total': i,'reciptnumber':j,'housetaxpaid':k,'healthtaxpaid':l,'lighttaxpaid':m,'watertaxpaid':n,'totalpaid':o,'rest':p,'datei': localtime}
            database.insert(new_user,v)
            mydb.commit()



            messagebox.showinfo("etax-2019","Data Updated Successfully")





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
            self.backbutton.configure(text='''Back''',command= self.backs)

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
            self.exit.configure(text='''Exit''',command= self.exits)

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
            self.btn_submit.configure(text='''SUBMIT''',command= self.submit5)

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
















def main():
    print("Welcome To E-tax 2019 Administrator Software\n")
    print("*************"*10)
    print("\n\n\n\n")
    a=str(input("Please Enter the Password.................."))
    if a != "Pass@123":
        exit()
    print("Which Action Do You Want To Perform ? \n\n 1.View Requests \n 2.Delete Data  \n 3.Update Data")
    a=int(input())
    if a==1:
        view()
    elif a==2:
        delete()
    elif a==3:
        update()
    else :
        print("Wrong Option")


print("welcome")
main()


