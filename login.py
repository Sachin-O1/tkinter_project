from logging import exception
import re
from tkinter import *
import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database ="tk_projectdb2"
       )
cursor=con.cursor()

root = Tk()
root.geometry('510x400')
root.title("Login Form")
root.configure(background='#FBF6EB')


img1 = PhotoImage(file="bulba_edit.png")
labebg1 = Label(
    root,
    image=img1,
    bg='#FBF6EB',
)
labebg1.place(x=5, y=180 )
img2 = PhotoImage(file="pikapikaedit.png")
labebg2 = Label(
    root,
    image=img2,
    bg='#FBF6EB',
)
labebg2.place(x=285, y=180 )


Email=StringVar()
password=StringVar()

def database():
    email=Email.get()
    passwo=password.get()
    try:
        cursor.execute("SELECT * FROM user_information WHERE email = '%s' and passwrd = '%s'" %(email,passwo))
        catch1 = cursor.fetchone()
        print(catch1)
        if catch1 == None:
            messagebox.showerror("error","Invalid Email id or Password")
        else:
            messagebox.showinfo("success","Welcome")
            dictionary()
    except exception as err1:
        messagebox.showerror("error",f"Error due to {str(err1)}")
        
        
def register():
    root.destroy()
    import registation

def dictionary():
    root.destroy()
    import Dictionary
    
def forgot():
    root.destroy()
    import forget
    
label_1 = Label(root, text="Login",width=20,bg='#FBF6EB',font=("bold", 20))
label_1.place(x=95,y=10)

label_2 = Label(root, text="Email",width=15,anchor=W,bg='#FBF6EB',font=("bold", 10))
label_2.place(x=30,y=80)
entry_0 = Entry(root,textvar=Email,width=40)
entry_0.place(x=230,y=80,)

label_3 = Label(root, text="Password",width=15,anchor=W,bg='#FBF6EB',font=("bold", 10))
label_3.place(x=30,y=130)
entry_1 = Entry(root,textvar=password,width=40)
entry_1.place(x=230,y=130)

def fieldcheck():
    if Email.get() == "" or password.get() == "" :
        messagebox.showerror("error", "All Fields are Required")
    else:
        database()
        
button = Button(root, text='Register', width=15, command=register)
button.place(x=360,y=160)
Button(root, text='Forgot Password',width=15,bg='brown',fg='white',command=forgot).place(x=360,y=190)
Button(root, text='Submit',width=15,bg='brown',fg='white',command=fieldcheck).place(x=200,y=300)

con.commit()
root.mainloop()