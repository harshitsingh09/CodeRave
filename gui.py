from tkinter import *
import tkinter.messagebox
import os
import index
import chatbot
import mail1
import song
import wikipedia


def mail():
    mail1.email()
       
def lyrics():
    s = song.details_input() 
    print("\r\n")
    F = open(s[0]+"_"+s[1]+".txt",'r')
    ly=F.read()
    print(ly)
    F.close()
    os.remove(s[0]+"_"+s[1]+".txt")

def wiki():
    a = input('What do you want to search: ')
    print(wikipedia.summary(a, sentences=2))

def run():
    index.run()

def chat():
    chatbot.chat()

def calc():
    os.system('calc.exe')

def notepad():
    os.system('notepad.exe')

def word():
    filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
    os.system('start winword.exe'.format(filepath))

def ppt():
    filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
    os.system('start powerpnt.exe'.format(filepath))

def pdf():
    filepath = "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
    os.system('start AcroRd32.exe'.format(filepath))

def onenote():
    filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
    os.system('start onenote.exe'.format(filepath))

def excel():
    filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
    os.system('start excel.exe'.format(filepath))
    
root = Tk()
root.title('Vani')

frame1 = Frame(root, height=300, width=5000)
frame1.pack()

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
openMenu = Menu(menu)

menu.add_cascade(label="Menu", menu = subMenu)
subMenu.add_command(label="Send email", command = mail)
subMenu.add_command(label="Get lyrics", command = lyrics)
subMenu.add_command(label="Search", command = wiki)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)
menu.add_cascade(label="Open", menu = openMenu)
openMenu.add_command(label="Calculator", command = calc)
openMenu.add_command(label="PDF", command = pdf)
openMenu.add_command(label="Notepad", command = notepad)
openMenu.add_separator()
openMenu.add_command(label="Word", command = word)
openMenu.add_command(label="PowerPoint", command = ppt)
openMenu.add_command(label="OneNote", command = onenote)
openMenu.add_command(label="Excel", command = excel)


b1 = Button(frame1, text="Begin", command=run, height=5, width=25)
b1.pack(side=LEFT,padx=150,pady=50)
b2 = Button(frame1, text="Chat", command=chat, height=5, width=25)
b2.pack(side=LEFT,padx=150,pady=50)

root.mainloop()
