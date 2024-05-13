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

    root1.geometry("1366x768+0+0")
    root1.title("KNOW YOUR ANSWER")
    cmrit_label = Label(text="KNOW YOUR ANSWER", font="Times 20 italic bold", bg="#154360" ).pack(side=TOP,  fill=X)






    def changeOnHover(button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))

    c1 = Canvas(root1, width=400, height=1600, bg="#5499C7", relief='ridge')
    c1.pack(side=TOP, anchor="nw")
    c2 = Canvas(root1, width=1200, height=1600, bg="#A9CCE3", relief='ridge')
    c2.place(x=400, y=37)
    login_label = Label(c1, text="PASTE YOUR LINK HERE", font="Times 15 bold", bg="#117A65", pady=3, padx=30).place(x=80, y=100)
    t1 = True

    # l2 = Label(text="ENTER USER ID", bg="#48C9B0", padx=5, pady=5, font="arial 15 bold").place(x=630, y=100)
    user = Entry(width=20, show="*", bd=5, font=("arial", 25), textvar=userid1, bg="#7DCEA0")
    user.place(x=20, y=250)
    # l1 = Label(text="ENTER PASSWORD", bg="#48C9B0", padx=5, pady=5, font="arial 15 bold").place(x=630, y=200)
    user = Entry(width=20, show="*", bd=5, font=("arial", 25), textvar=passw2, bg="#7DCEA0")
    user.place(x=20, y=400)
    def choose_user():
        pass

    clientb = Button(root1, text="SUBMIT", bg="#C39BD3", height=2, font="Times 15 bold",
                     command=choose_user, padx=5)
    clientb.place(x=80, y=500)

    my_pic = Image.open("big33.png")
    re = my_pic.resize((220, 150), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(re)
    my_img = c2.create_image(740, 0, anchor=NW, image=new_pic)
    # b2 = Button(c2, text="<<BACK", bg="#C39BD3", height=2, font="Times 13 bold", padx=7, command=d0).place(
    #     x=200, y=250)

    # admin_button = Button(c1,
    #                       text="FOR ADMIN",
    #                       bg="#117864", height=1, width=20, font="Times 20 bold", command=admin_entry)
    # admin_button.place(x=30, y=400)

    text = Text(c1)
    text = Text(c1, height=2, width=30, bg="#5499C7", fg="#1F618D")
    text.insert(INSERT,
                '''THIS IS A SECTION OF PASTING NEWS''')

    text.insert(END, "!")
    text.place(x=40, y=550)

    # client_button = Button(c1,
    #                        text="FOR client",
    #                        bg="#117864", height=1, width=20, font="Times 20 bold", command=choose)
    # client_button.place(x=30, y=470)

    changeOnHover(clientb, "#3498DB", "#117864")
    # changeOnHover(admin_button, "#B03A2E", "#117864")

    my_pic = Image.open("bigg.png")
    re = my_pic.resize((410, 600), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(re)
    my_img = c1.create_image(0, 0, anchor=NW, image=new_pic)
    my_pic1 = Image.open("big33.png")
    re1 = my_pic1.resize((960, 900), Image.ANTIALIAS)
    new_pic1 = ImageTk.PhotoImage(re1)
    my_img1 = c2.create_image(0, 0, anchor=NW, image=new_pic1)
    l2 = Label(c2, text="EXPLORE ABOUT ARTICLE", font="Times 25 bold", bg="#16A085", padx=15).place(x=150, y=5)

    root1.mainloop()

# main()