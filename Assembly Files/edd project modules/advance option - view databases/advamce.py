            import sys
            import mysql.connector
            from openpyxl import Workbook
            from reportlab.pdfgen import canvas
            import tkinter
            from tkinter import messagebox

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

            import advamce_support
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
                advamce_support.init(root, top)
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
                advamce_support.init(w, top, *args, **kwargs)
                return (w, top)

            def destroy_Toplevel1():
                global w
                w.destroy()
                w = None

            class Toplevel1:
                def pdfs(self):
                    idd=str(self.Entry1.get());
                    mydb=mysql.connector.connect(host='remotemysql.com',user='NhpDbfVMT3',password='NXWSVJNu55',database='NhpDbfVMT3',port='3306')
                    mycursor=mydb.cursor()
                    query = ("SELECT idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest, datei FROM kalamwadi where idnumber = %s" %(idd))
                    mycursor.execute(query)
                    for(idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest, datei) in mycursor:
                        a="UID Number :                      "+idnumber
                        b="Meter Number :                     "+meternumber
                        z="Ward Number :                      "+wardnumber
                        d="Name :                                  "+name
                        e="Housetax :                             "+housetax
                        f="Healthtax :                            "+healthtax
                        g="Lighttax :                              "+lighttax
                        h="Watertax :                             "+watertax
                        j='Receiptnumber : '+reciptnumber
                        k="Paid Housetax :                     "+housetaxpaid
                        l="Paid Healthtax :                    "+healthtaxpaid
                        m="Paid Lighttax :                      "+lighttaxpaid
                        n="Paid Watertax :                     "+watertaxpaid
                        q="Total Paid Tax :                    "+totalpaid
                        o="Remaining Ammount :                0"+rest
                        p='Date : '+datei
                        x=reciptnumber
                    filename=x+'.pdf'
                    c= canvas.Canvas(filename)
                    c.setFont("Helvetica",25)
                    c.setFillColorRGB(100,0,0)
                    c.drawString(265,800,"eTAX 2019")
                    c.setFont("Helvetica",20)
                    c.setFillColorRGB(0,0,110)
                    c.drawString(165,775,'Village Kalamwadi, District : Sangali')
                    c.setFont("Times-Roman",12)
                    c.setFillColorRGB(0,0,0)
                    c.drawString(385,725,p)
                    c.drawString(385,710,j)
                    c.drawString(385,695,"Incharge Officer : Shridhar Kulkarni")
                    c.line(20,675,600,675)
                    c.drawString(40,655,d)
                    c.drawString(40,640,a)
                    c.drawString(40,625,b)
                    c.drawString(40,610,z)
                    c.drawString(40,595,e)
                    c.drawString(40,580,f)
                    c.drawString(40,565,g)
                    c.drawString(40,550,h)
                    c.line(20,535,600,535)
                    c.drawString(40,520,"---------------PAID AMMOUNT---------------")
                    c.drawString(40,505,k)
                    c.drawString(40,490,l)
                    c.drawString(40,475,m)
                    c.drawString(40,460,n)
                    c.drawString(40,445,q)
                    c.line(20,440,600,440)
                    c.drawString(40,425,o)
                    c.line(20,410,600,410)
                    c.drawString(500,360,"Sign")
                    c.setFont("Helvetica",15)
                    c.line(20,350,600,350)
                    c.drawString(265,320,"Thank You !!!")
                    c.drawImage("image.png",180,80, width=250,height=140,mask=None)
                    c.save()
                    tkinter.messagebox.showinfo('etax-2019','Receipt Created Successfully You Can Get It from directory')


                def getlists(self):
                    mydb=mysql.connector.connect(host='remotemysql.com',user='NhpDbfVMT3',password='NXWSVJNu55',database='NhpDbfVMT3',port='3306')
                    mycursor=mydb.cursor()
                    wb = Workbook()

                    SQL = 'SELECT idnumber,name,total,rest from kalamwadiinfo;'
                    mycursor.execute(SQL)
                    ws = wb.create_sheet(0)
                    ws.title = 'kalamwadi_info'
                    ws.append(mycursor.column_names)
                    for (idnumber,name,total,rest) in mycursor:
                        a=float(rest)
                        b=float(total)
                        if a > b/2:
                            row=(idnumber,rest,total,rest)
                            ws.append(row)

                    workbook_name = "Kalamwadi_blacklist"
                    wb.save(workbook_name + ".xlsx")

                    tkinter.messagebox.showinfo('etax2019','Successfully Created Exel File. You Can Access the file from directory ')
                def backs(self):
                    print("ij")

                def __init__(self, top=None):
                    '''This class configures and populates the toplevel window.
                       top is the toplevel containing window.'''
                    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
                    _fgcolor = '#000000'  # X11 color: 'black'
                    _compcolor = '#d9d9d9' # X11 color: 'gray85'
                    _ana1color = '#d9d9d9' # X11 color: 'gray85'
                    _ana2color = '#ececec' # Closest X11 color: 'gray92'
                    font10 = "-family {Captain Howdy} -size 13"
                    font12 = "-family {Bodoni MT Black} -size 11 -weight bold"
                    font15 = "-family {Rockwell Extra} -size 15 -weight bold"
                    font18 = "-family {Rockwell Condensed} -size 40 -weight bold"
                    font9 = "-family {SI Font} -size 36"

                    top.geometry("935x638+237+119")
                    top.title("New Toplevel")
                    top.configure(background="#7a7a7a")

                    self.Frame1 = tk.Frame(top)
                    self.Frame1.place(relx=0.043, rely=0.047, relheight=0.149
                            , relwidth=0.754)
                    self.Frame1.configure(relief='raised')
                    self.Frame1.configure(borderwidth="10")
                    self.Frame1.configure(relief='raised')
                    self.Frame1.configure(background="#5b5b5b")
                    self.Frame1.configure(width=705)

                    self.Label1 = tk.Label(self.Frame1)
                    self.Label1.place(relx=0.113, rely=0.105, height=58, width=91)
                    self.Label1.configure(background="#5b5b5b")
                    self.Label1.configure(disabledforeground="#a3a3a3")
                    self.Label1.configure(font=font9)
                    self.Label1.configure(foreground="#ff2908")
                    self.Label1.configure(text='''TAX''')
                    self.Label1.configure(width=91)

                    self.Label1_1 = tk.Label(self.Frame1)
                    self.Label1_1.place(relx=0.071, rely=0.105, height=58, width=41)
                    self.Label1_1.configure(activebackground="#f9f9f9")
                    self.Label1_1.configure(activeforeground="black")
                    self.Label1_1.configure(background="#5b5b5b")
                    self.Label1_1.configure(disabledforeground="#a3a3a3")
                    self.Label1_1.configure(font="-family {SI Font} -size 36")
                    self.Label1_1.configure(foreground="#2631d1")
                    self.Label1_1.configure(highlightbackground="#d9d9d9")
                    self.Label1_1.configure(highlightcolor="black")
                    self.Label1_1.configure(text='''e''')
                    self.Label1_1.configure(width=41)

                    self.Label1_2 = tk.Label(self.Frame1)
                    self.Label1_2.place(relx=0.241, rely=0.105, height=58, width=101)
                    self.Label1_2.configure(activebackground="#f9f9f9")
                    self.Label1_2.configure(activeforeground="black")
                    self.Label1_2.configure(background="#5b5b5b")
                    self.Label1_2.configure(disabledforeground="#a3a3a3")
                    self.Label1_2.configure(font="-family {SI Font} -size 36")
                    self.Label1_2.configure(foreground="#fff71c")
                    self.Label1_2.configure(highlightbackground="#d9d9d9")
                    self.Label1_2.configure(highlightcolor="black")
                    self.Label1_2.configure(text='''2019''')
                    self.Label1_2.configure(width=101)

                    self.Label1_3 = tk.Label(self.Frame1)
                    self.Label1_3.place(relx=0.411, rely=0.105, height=58, width=371)
                    self.Label1_3.configure(activebackground="#f9f9f9")
                    self.Label1_3.configure(activeforeground="black")
                    self.Label1_3.configure(background="#5b5b5b")
                    self.Label1_3.configure(disabledforeground="#a3a3a3")
                    self.Label1_3.configure(font="-family {SI Font} -size 36")
                    self.Label1_3.configure(foreground="#33a521")
                    self.Label1_3.configure(highlightbackground="#d9d9d9")
                    self.Label1_3.configure(highlightcolor="black")
                    self.Label1_3.configure(text='''VIEW DATABASE''')
                    self.Label1_3.configure(width=371)

                    self.Frame2 = tk.Frame(top)
                    self.Frame2.place(relx=0.032, rely=0.266, relheight=0.697
                            , relwidth=0.455)
                    self.Frame2.configure(relief='sunken')
                    self.Frame2.configure(borderwidth="10")
                    self.Frame2.configure(relief='sunken')
                    self.Frame2.configure(background="#5b5b5b")
                    self.Frame2.configure(width=425)

                    self.Label1_5 = tk.Label(self.Frame2)
                    self.Label1_5.place(relx=0.259, rely=0.045, height=48, width=201)
                    self.Label1_5.configure(activebackground="#f9f9f9")
                    self.Label1_5.configure(activeforeground="black")
                    self.Label1_5.configure(background="#5b5b5b")
                    self.Label1_5.configure(disabledforeground="#a3a3a3")
                    self.Label1_5.configure(font="-family {SI Font} -size 36")
                    self.Label1_5.configure(foreground="#432eff")
                    self.Label1_5.configure(highlightbackground="#d9d9d9")
                    self.Label1_5.configure(highlightcolor="black")
                    self.Label1_5.configure(text='''Receipt''')
                    self.Label1_5.configure(width=201)

                    self.Label2 = tk.Label(self.Frame2)
                    self.Label2.place(relx=0.212, rely=0.225, height=27, width=244)
                    self.Label2.configure(background="#5b5b5b")
                    self.Label2.configure(disabledforeground="#a3a3a3")
                    self.Label2.configure(font=font10)
                    self.Label2.configure(foreground="#f7ff17")
                    self.Label2.configure(text='''Get PDF copy of Reciept''')

                    self.Label2_8 = tk.Label(self.Frame2)
                    self.Label2_8.place(relx=0.094, rely=0.315, height=27, width=344)
                    self.Label2_8.configure(activebackground="#f9f9f9")
                    self.Label2_8.configure(activeforeground="black")
                    self.Label2_8.configure(background="#5b5b5b")
                    self.Label2_8.configure(disabledforeground="#a3a3a3")
                    self.Label2_8.configure(font="-family {Bodoni MT Black} -size 11 -weight bold")
                    self.Label2_8.configure(foreground="#f7ff17")
                    self.Label2_8.configure(highlightbackground="#d9d9d9")
                    self.Label2_8.configure(highlightcolor="black")
                    self.Label2_8.configure(text='''Enter UID Number Here :''')
                    self.Label2_8.configure(width=344)

                    self.Entry1 = tk.Entry(self.Frame2)
                    self.Entry1.place(relx=0.306, rely=0.404,height=20, relwidth=0.386)
                    self.Entry1.configure(background="white")
                    self.Entry1.configure(disabledforeground="#a3a3a3")
                    self.Entry1.configure(font="TkFixedFont")
                    self.Entry1.configure(foreground="#000000")
                    self.Entry1.configure(insertbackground="black")

                    self.btn_pdf = tk.Button(self.Frame2)
                    self.btn_pdf.place(relx=0.306, rely=0.517, height=56, width=165)
                    self.btn_pdf.configure(activebackground="#ececec")
                    self.btn_pdf.configure(activeforeground="#000000")
                    self.btn_pdf.configure(background="#3f8e36")
                    self.btn_pdf.configure(borderwidth="10")
                    self.btn_pdf.configure(disabledforeground="#a3a3a3")
                    self.btn_pdf.configure(font=font15)
                    self.btn_pdf.configure(foreground="#000000")
                    self.btn_pdf.configure(highlightbackground="#d9d9d9")
                    self.btn_pdf.configure(highlightcolor="black")
                    self.btn_pdf.configure(pady="0")
                    self.btn_pdf.configure(text='''GENERATE''',command=self.pdfs)

                    self.Label3 = tk.Label(self.Frame2)
                    self.Label3.place(relx=0.353, rely=0.674, height=114, width=104)
                    self.Label3.configure(background="#d9d9d9")
                    self.Label3.configure(disabledforeground="#a3a3a3")
                    self.Label3.configure(foreground="#000000")
                    photo_location = os.path.join(prog_location,"./adv1.png")
                    self._img0 = tk.PhotoImage(file=photo_location)
                    self.Label3.configure(image=self._img0)
                    self.Label3.configure(text='''Label''')
                    self.Label3.configure(width=104)

                    self.Frame2_4 = tk.Frame(top)
                    self.Frame2_4.place(relx=0.524, rely=0.266, relheight=0.697
                            , relwidth=0.455)
                    self.Frame2_4.configure(relief='sunken')
                    self.Frame2_4.configure(borderwidth="10")
                    self.Frame2_4.configure(relief='sunken')
                    self.Frame2_4.configure(background="#5b5b5b")
                    self.Frame2_4.configure(highlightbackground="#d9d9d9")
                    self.Frame2_4.configure(highlightcolor="black")
                    self.Frame2_4.configure(width=425)

                    self.Label1_6 = tk.Label(self.Frame2_4)
                    self.Label1_6.place(relx=0.235, rely=0.045, height=58, width=241)
                    self.Label1_6.configure(activebackground="#f9f9f9")
                    self.Label1_6.configure(activeforeground="black")
                    self.Label1_6.configure(background="#5b5b5b")
                    self.Label1_6.configure(disabledforeground="#a3a3a3")
                    self.Label1_6.configure(font="-family {SI Font} -size 36")
                    self.Label1_6.configure(foreground="#432eff")
                    self.Label1_6.configure(highlightbackground="#d9d9d9")
                    self.Label1_6.configure(highlightcolor="black")
                    self.Label1_6.configure(text='''Special List''')
                    self.Label1_6.configure(width=241)

                    self.Label2_7 = tk.Label(self.Frame2_4)
                    self.Label2_7.place(relx=0.047, rely=0.27, height=27, width=384)
                    self.Label2_7.configure(activebackground="#f9f9f9")
                    self.Label2_7.configure(activeforeground="black")
                    self.Label2_7.configure(background="#5b5b5b")
                    self.Label2_7.configure(disabledforeground="#a3a3a3")
                    self.Label2_7.configure(font=font12)
                    self.Label2_7.configure(foreground="#f7ff17")
                    self.Label2_7.configure(highlightbackground="#d9d9d9")
                    self.Label2_7.configure(highlightcolor="black")
                    self.Label2_7.configure(text='''of people who paid less than 50% Ammount of tax''')
                    self.Label2_7.configure(width=384)

                    self.Label2_8 = tk.Label(self.Frame2_4)
                    self.Label2_8.place(relx=0.165, rely=0.202, height=27, width=284)
                    self.Label2_8.configure(activebackground="#f9f9f9")
                    self.Label2_8.configure(activeforeground="black")
                    self.Label2_8.configure(background="#5b5b5b")
                    self.Label2_8.configure(disabledforeground="#a3a3a3")
                    self.Label2_8.configure(font="-family {Captain Howdy} -size 13")
                    self.Label2_8.configure(foreground="#f7ff17")
                    self.Label2_8.configure(highlightbackground="#d9d9d9")
                    self.Label2_8.configure(highlightcolor="black")
                    self.Label2_8.configure(text='''Get Excel sheet''')
                    self.Label2_8.configure(width=284)

                    self.btn_getlist = tk.Button(self.Frame2_4)
                    self.btn_getlist.place(relx=0.212, rely=0.382, height=86, width=265)
                    self.btn_getlist.configure(activebackground="#ececec")
                    self.btn_getlist.configure(activeforeground="#000000")
                    self.btn_getlist.configure(background="#3f8e36")
                    self.btn_getlist.configure(borderwidth="20")
                    self.btn_getlist.configure(disabledforeground="#a3a3a3")
                    self.btn_getlist.configure(font=font18)
                    self.btn_getlist.configure(foreground="#111c7a")
                    self.btn_getlist.configure(highlightbackground="#d9d9d9")
                    self.btn_getlist.configure(highlightcolor="black")
                    self.btn_getlist.configure(pady="0")
                    self.btn_getlist.configure(text='''GET LIST''')
                    self.btn_getlist.configure(width=265,command=self.getlists)

                    self.Label4 = tk.Label(self.Frame2_4)
                    self.Label4.place(relx=0.376, rely=0.629, height=130, width=130)
                    self.Label4.configure(background="#d9d9d9")
                    self.Label4.configure(disabledforeground="#a3a3a3")
                    self.Label4.configure(foreground="#000000")
                    photo_location = os.path.join(prog_location,"./adv2.png")
                    self._img1 = tk.PhotoImage(file=photo_location)
                    self.Label4.configure(image=self._img1)
                    self.Label4.configure(text='''Label''')

                    self.btn_back = tk.Button(top)
                    self.btn_back.place(relx=0.845, rely=0.094, height=46, width=95)
                    self.btn_back.configure(activebackground="#ececec")
                    self.btn_back.configure(activeforeground="#000000")
                    self.btn_back.configure(background="#ff2008")
                    self.btn_back.configure(borderwidth="10")
                    self.btn_back.configure(disabledforeground="#a3a3a3")
                    self.btn_back.configure(font="-family {Rockwell Extra} -size 15 -weight bold")
                    self.btn_back.configure(foreground="#000000")
                    self.btn_back.configure(highlightbackground="#d9d9d9")
                    self.btn_back.configure(highlightcolor="black")
                    self.btn_back.configure(pady="0")
                    self.btn_back.configure(text='''BACK''')
                    self.btn_back.configure(width=95,command=self.backs)

            if __name__ == '__main__':
                vp_start_gui()





