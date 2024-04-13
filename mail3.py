import smtplib
import urllib.request, urllib.error, urllib.parse
from tkinter import *
import tkinter.messagebox

def send():
    global entry1
    global entry2
    r_add = entry1.get()
    txt = entry2.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("sirji.beproject@gmail.com", "sirjibeproject")
    server.sendmail("sirji.beproject@gmail.com", r_add, txt)
    server.quit()

    window = Tk()

    tkinter.messagebox.showinfo('Email status', 'Email has been sent')

    window.mainloop()
    
def email():
    root = Tk()
    
      
    label1 = Label(root, text='Enter recipient address')
    label1.grid(row=0, column=0)
    entry1 = Entry(root)
    entry1.grid(row=0, column=1)
    entry1.focus_set()
    
    label2 = Label(root, text='Enter your message')
    label2.grid(row=1, column=0)
    entry2 = Entry(root)
    entry2.grid(row=1, column=1)
    entry2.focus_set()

    button = Button(root, text="Send", command = send)
    button.grid(row=2)


    root.mainloop()

        

