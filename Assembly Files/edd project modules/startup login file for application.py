import sys
import tkinter
import tkinter.messagebox
a = input("Enter username : \n")
b = input("Enter Password : \n")
if a!="pranesh67" or b!="Pass@123":
    tkinter.messagebox.showwarning("Login Page","The username or Password is incorrect");
    sys.exit(0)
else:
    print("### write the whole program here with indentation +1###")