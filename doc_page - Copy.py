from tkinter import *
from tkinter import ttk

import time
from tkinter import Text, Tk
import tkinter.messagebox as tmsg
from PIL import ImageTk,Image

global user3
def main():
    global root1
    root1 = Tk()
    global passw
    passw = StringVar()
    global passw2
    passw2 = StringVar()
    global userid
    userid = StringVar()
    global userid1
    userid1 = StringVar()
    global var
    var = IntVar()
    global sum
    sum = IntVar()
    # global root1
    # root1 = Tk()
    root1.geometry("1366x768+0+0")
    root1.title("KNOW YOUR ANSWER")

    def changeOnHover(button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))
    c1 = Canvas(root1, width=1600, height=1600, bg="#5499C7", relief='ridge')
    c1.pack(side=TOP, anchor="nw")

    t2=''' Ask Your Question here about stocks
    '''

    e2 = Label(c1, text=t2, font=("arial", 20),background="red")
    e2.place(x=400, y=100)

    user = Entry(width=60, bd=5, font=("arial", 25), textvar=userid1, bg="#7DCEA0")
    user.place(x=20, y=250)
    def answer():
    #    root1.destroy()
       question=userid1.get()
       print(question)
       from model import main
       result=main(question)
       root1.destroy()
       
       from window import main
       main(result)
       from doc_page import main
       main()
    admin_button = Button(c1,
                        text="Search",
                        bg="#117864", height=1, width=20, font="Times 20 bold", command=answer)
    admin_button.place(x=30, y=390)

    def backk():
        root1.destroy()
        from first_page import first
        first()

    clientb = Button(root1, text="<<BACK", bg="#C39BD3", height=2, font="Times 15 bold",
                     command=backk, padx=5)
    clientb.place(x=50, y=40)
   
    root1.mainloop()



