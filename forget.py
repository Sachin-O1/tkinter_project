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

Email=StringVar()
q=StringVar()
a=StringVar()
password = StringVar()
cpassword = StringVar()

def database():
    email=Email.get()
    ques=q.get()
    ans = a.get()
    passwo=password.get()
    cursor.execute("SELECT * FROM user_information WHERE email = '%s'" %email)
    catch1 = cursor.fetchone()
    print(catch1)
    if catch1 == None:
        messagebox.showerror("error","Email id not Found")
    else:
        print(ques,ans)
        cursor.execute("SELECT * FROM user_information WHERE question = '%s' and answer = '%s'" %(ques,ans))
        catch2 = cursor.fetchone()
        if catch2 == None:
            messagebox.showerror("error","Wrong Security Answer try Again")
        else:
            try:
                print(passwo,email)
                cursor.execute("UPDATE user_information set passwrd = '%s' WHERE email = '%s'" %(passwo,email))
                messagebox.showinfo("success","Password updated successfully")
                login()
            except exception as err1:
                messagebox.showerror("error",f"Error due to {str(err1)} ")
    con.commit()
            
def login():
    root.destroy()
    import login
    
label_1 = Label(root, text="Login",width=20,font=("bold", 20))
label_1.place(x=80,y=10)

label_2 = Label(root, text="Email",width=15,anchor=W,font=("bold", 10))
label_2.place(x=30,y=80)
entry_0 = Entry(root,textvar=Email,width=40)
entry_0.place(x=230,y=80,)

label_3 = Label(root, text="Security Question",width=15,anchor=W,font=("bold", 10))
label_3.place(x=30,y=120)

list1 = ['What is your date of birth?','What was your favorite  car?','What is your astrological sign?','What city were you born in?','What’s your favorite movie?','What was your childhood nickname?'];

droplist=OptionMenu(root,q, *list1)
droplist.config(width=34)
q.set('select your question') 
droplist.place(x=226.5,y=120)

label_4 = Label(root, text="Answer",width=15,anchor=W,font=("bold", 10))
label_4.place(x=30,y=160)
entry_1 = Entry(root,textvar=a,width=40)
entry_1.place(x=230,y=160)

label_5 = Label(root, text="Password",width=15,anchor=W,font=("bold", 10))
label_5.place(x=30,y=200)
entry_2 = Entry(root,textvar=password,width=40)
entry_2.place(x=230,y=200)
label_6 = Label(root, text="Confirm Password",width=15,anchor=W,font=("bold", 10))
label_6.place(x=30,y=240)
entry_3 = Entry(root,textvar=cpassword,width=40)
entry_3.place(x=230,y=240)

def fieldcheck():
    if Email.get() == "" or q.get() == "" or a.get() == "" or password.get() == "" :
        messagebox.showerror("error", "All Fields are Required")
    elif '@' not in Email.get():
    	messagebox.showerror("error","Invalid Email")
    elif password.get() != cpassword.get() :
        messagebox.showerror("error","Password & Confirm Password Must Be Same")
    else:
        database()

Button(root, text='Submit',width=15,bg='brown',fg='white',command=fieldcheck).place(x=200,y=300)
Button(root, text='Login',width=15,bg='brown',fg='white',command=login).place(x=200,y=340)


root.mainloop()