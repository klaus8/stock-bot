from tkinter import *
from tkinter import ttk
# import sqlite3
import time
import tkinter as tk
from tkinter import Text, Tk
import tkinter.messagebox as tmsg
from PIL import ImageTk,Image


def first():
    root=tk.Tk()
    root.title("WELCOME TO FIRST PAGE")
    root.geometry("1600x1000+0+0")

    frame = tk.Frame(root, relief='ridge', borderwidth=1)  # Create a frame with relief and borderwidth
    frame.grid(row=0, column=0)

    c1 = tk.Canvas(frame, width=600, height=1600, bg="#5499C7")  # Create canvas inside the frame
    c1.pack()

    frame_1 = tk.Frame(root, relief='ridge', borderwidth=1)  # Create a frame with relief and borderwidth
    frame_1.grid(row=0, column=1)

    c2 = tk.Canvas(frame_1, width=800, height=1600, bg="red")  # Create canvas inside the frame
    c2.pack()
    t2='''TRAINED DOC:
       Access a treasure trove of knowledge with our Doc feature!
       Explore curated PDF documents containing valuable
       information on various stock market topics. 
       Select from a range of documents
       and ask StockBot questions to gain deeper insights 
       into the world of
       stock trading and investment strategies


    '''

    

    t1=''' LINK PASTE:
        Easily extract insights from any online article
        with the Link Paste feature! Simply paste the URL 
        of the article you want to explore, and 
        StockBot will provide a summary and answer
        any questions you have based on the content.
    '''
    e1 = Label(c2, text=t1, font=("arial", 15))
    e1.place(x=50, y=50)

    e2 = Label(c2, text=t2, font=("arial", 15))
    e2.place(x=50, y=300)

    my_img = Image.open("ssr.png")
    re3 = my_img.resize((100, 100), Image.ANTIALIAS)
    new_pic3 = ImageTk.PhotoImage(re3)
    my_img = c1.create_image(590, 600, image=new_pic3)
    # c1=Canvas(root,width=400,height=1600,bg="#5499C7",relief='ridge')
    # c1.grid(row=0,col=0)
    def admin_entry():
        root.destroy()
        from samm import main
        main()
    def doc_answers():
        root.destroy()
        from doc_page import main
        main()
    e2 = Label(c1, text="CHOOSE FROM BELOW", font=("arial", 26))
    e2.place(x=30, y=200)

    admin_button = Button(c1,
                            text="LINK PASTE",
                            bg="#117864", height=1, width=20, font="Times 20 bold", command=admin_entry)
    admin_button.place(x=30, y=300)

    admin_button = Button(c1,
                        text="DOC TRAIN",
                        bg="#117864", height=1, width=20, font="Times 20 bold", command=doc_answers)
    admin_button.place(x=30, y=390)

    while (t1):
        for x in range(0, 500):
            # c2.moveto(my_img,5,5)
            c1.move(my_img, 0, -1)
            root.update()
            time.sleep(0.01)
        

    root.mainloop()
# first()