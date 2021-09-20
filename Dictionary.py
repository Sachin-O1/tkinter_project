from tkinter import *
import tkinter.messagebox
import sys
import os

running = True
root=Tk()
root.geometry('750x600')
root.title("Dictionaries")
root.configure(background='#FBF6EB')
#Entry widget object
textin=StringVar()
closecheck = StringVar()

#Dictionaries
import json 
from difflib import get_close_matches
import mysql.connector
from tkinter import *

data = json.load(open("data.json"))

con = mysql.connector.connect(
host="localhost",
user="root",
password="",
database ="tk_projectdb2"
)

cursor = con.cursor()

ent=Entry(root,width=20,font=('none 18 bold'),textvar=textin,bg='white')
ent.place(x=680,y=100,anchor=E)  

output=Text(root,width=40,height=8,font=('Time 20 bold'),fg="black")
output.place(x=105,y=220)
      
def clk():
     word = ent.get() 
     query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %word)
     results = cursor.fetchall()

     def translate(w):
        w = w.lower()
        if w in results:
            return results[w]
        elif w.upper() in results:
            return results[w.upper()]
        elif w.title() in results:
            return results[w.title()]
        elif len(get_close_matches (w, data.keys())) > 0:
             #New window
             top= Toplevel(root)
             top.geometry("750x550")
             top.configure(background='#FBF6EB')
             label= Label(top, text="Did you mean %s instead? Enter y if yes or n if no: " %get_close_matches(w, data.keys())[0],bg='#FBF6EB',font= ('Helvetica 15 bold'))
             label.pack(pady=20)
             #Create an Entry Widget in the Toplevel window
             ent1= Entry(top,width=20,font=('none 18 bold'),textvar=closecheck,bg='white')
             ent1.pack()
             label2=Label(top,text='Results',bg='#FBF6EB',font=('non 18 bold'))
             label2.place(x=10,y=200)
             output1=Text(top,width=40,height=8,font=('Time 20 bold'),fg="black")
             output1.place(x=105,y=230)
             def closecond():
                 chc = ent1.get()
                 if chc == "y":
                      closecheck = data[get_close_matches(w, data.keys())[0]]
                      output1.insert(0.0,closecheck)
                 elif chc == "n":
                      closecheck = "The word doesnt exists, please double check it."
                      output1.insert(0.0,closecheck)
                 else:
                      closecheck = "We didnt understand your entry"
                      output1.insert(0.0,closecheck)
     
             tbtn =Button(top, text="Submit", command=closecond,bg='brown',fg='white',font=('bold'))
             tbtn.place(x=325,y=130)
        else:
            return ("The word doesnt exists, please double check it.")
     if results:
        for result in results:
             textin = result[1]
             output.insert(0.0,textin)

     else:
          put = translate(word)
          if output == list:
               for item in output:  
                    textin = item
                    output.insert(0.0,textin)
          else:
               textin = output
               output.insert(0.0,textin)
               
def exit():
     tkinter.messagebox.showinfo("Program",'Exit')
     exit()   
     
def Contributors():
     tkinter.messagebox.showinfo("S/W Contributors",'\n 1.sachin\n 2.ritwik \n ___Version 1.0___')
     
def clr():
     textin.set("")
     output.delete('1.0', END)
     
def restart_program():
     python = sys.executable
     os.execl(python, python, * sys.argv)
     
menu = Menu(root)
root.config(menu=menu)

#tp
subm = Menu(menu)
menu.add_cascade(label="File",menu=subm)
subm.add_command(label="Save")
subm.add_command(label="Save As")
subm.add_command(label="Print")
subm.add_command(label="Exit",command=exit)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Contributors",command=Contributors)

labelt = Label(root, text="Ḋi̇̇стi̇̇ỏɴẫяӯ",width=10,bg='#FBF6EB',font=("bold", 20))
labelt.place(x=295,y=10)

label_1 = Label(root, text="Enter word",width=10,bg='#FBF6EB',font=("bold", 20))
label_1.place(x=300,y=100,anchor=E)

but=Button(root,text='Submit',command=clk,width=10,bg='brown',fg='white',font=('bold'))
but.place(x=360,y=160,anchor=E)

but4=Button(root,text='Clear',command=clr,width=10,bg='brown',fg='white',font=('bold'))
but4.place(x=520,y=160,anchor=E)

labb=Label(root,text='Results',bg='#FBF6EB',font=('non 18 bold'))
labb.place(x=10,y=185)

but1=Button(root,text='Exit',command=exit,width=10,bg='brown',fg='white',font=('bold'))
but1.place(x=320,y=510)

root.mainloop()
