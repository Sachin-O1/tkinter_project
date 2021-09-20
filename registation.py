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
root.geometry('550x600')
root.title("Registration Form")

f_name=StringVar()
l_name=StringVar()
Contact=StringVar()
Email=StringVar()
q=StringVar()
a=StringVar()
password = StringVar()
cpassword = StringVar()

def database():
    name1=f_name.get()
    name2=l_name.get()
    contact = Contact.get()
    email=Email.get()
    question=q.get()
    answer = a.get()
    passwo=password.get()
    
    cursor.execute("SELECT * FROM user_information WHERE email = '%s'" %email)
    catch = cursor.fetchone()
    print(catch)
    if catch != None:
        messagebox.showerror("error","Email already exist try another or try forgetting password")
    else:
        cursor.execute('INSERT INTO user_information (f_name,l_name,contact,email,question,answer,passwrd) VALUES(%s, %s, %s, %s, %s, %s, %s)',(name1,name2,contact,email,question,answer,passwo))
        messagebox.showinfo("success", "You have Registration Successfully")
        login()
    con.commit()

def login():
    root.destroy()
    import login

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=120,y=10)

label = Label(root, text="First Name",width=15,anchor=W,font=("bold", 10))
label.place(x=80,y=80)
entry_0 = Entry(root,textvar=f_name,width=40)
entry_0.place(x=280,y=80,)

label_1 = Label(root, text="Last Name",width=15,anchor=W,font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root,textvar=l_name,width=40)
entry_1.place(x=280,y=130)

label_2 = Label(root, text="Contact",width=15,anchor=W,font=("bold", 10))
label_2.place(x=80,y=180)
entry_2 = Entry(root,textvar=Contact,width=40)
entry_2.place(x=280,y=180)

label_3 = Label(root, text="Email",width=15,anchor=W,font=("bold", 10))
label_3.place(x=80,y=230)
entry_ = Entry(root,textvar=Email,width=40)
entry_.place(x=280,y=230)

label_4 = Label(root, text="Security Question",width=15,anchor=W,font=("bold", 10))
label_4.place(x=80,y=280)

list1 = ['What is your date of birth?','What was your favorite  car?','What is your astrological sign?','What city were you born in?','What’s your favorite movie?','What was your childhood nickname?'];

droplist=OptionMenu(root,q, *list1)
droplist.config(width=33)
q.set('select your question') 
droplist.place(x=280,y=280)

label_4 = Label(root, text="Answer",width=15,anchor=W,font=("bold", 10))
label_4.place(x=80,y=330)
entry_3 = Entry(root,textvar=a,width=40)
entry_3.place(x=280,y=330)

label_5 = Label(root, text="Password",width=15,anchor=W,font=("bold", 10))
label_5.place(x=80,y=380)
entry_4 = Entry(root,textvar=password,width=40)
entry_4.place(x=280,y=380)
label_6 = Label(root, text="Confirm Password",width=15,anchor=W,font=("bold", 10))
label_6.place(x=80,y=430)
entry_5 = Entry(root,textvar=cpassword,width=40)
entry_5.place(x=280,y=430)

def fieldcheck():
    if f_name.get() == "" or l_name.get() == "" or  Contact.get() == "" or Email.get() == "" or q.get() == "" or a.get() == "" or password.get() == "" :
        messagebox.showerror("error", "All Fields are Required")
    elif '@' not in Email.get():
    	messagebox.showerror("error","Invalid Email")
    elif password.get() != cpassword.get() :
        messagebox.showerror("error","Password & Confirm Password Must Be Same")
    else:
        database()

Button(root, text='Submit',width=15,bg='brown',fg='white',command=fieldcheck).place(x=225,y=500)
Button(root, text='login',width=15,bg='brown',fg='white',command=login).place(x=225,y=535)

root.mainloop()