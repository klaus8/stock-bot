from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import time
def main():
    root=tk.Tk()
    root.title("Home page")
    root.geometry("1600x1000+0+0")
    c1=Canvas(root,width=900,height=1600,background="#1292EE",bd=0, highlightthickness=0)
    c1.place(x=0,y=20)
    # background=root["bg"]
    c2=Canvas(root,width=400,height=1600,background="#034077",bd=0, highlightthickness=0)
    c2.place(x=900,y=20)
    # def canavs_2():
    #     c4=Canvas(root,width=400,height=1600,background="blue",bd=0, highlightthickness=0)
    #     c4.place(x=900,y=20)
    # # canavs_2()

    home_label = Label(text="WELCOME TO HOME PAGE", font="Times 25 italic bold",foreground="#154360",bg="light green").pack(side=TOP, fill=X)

    stock_label=  Label(text="STOCK-BOT", font="Times 80 italic bold",foreground="#181000",bg="#0077CC").place(x=200,y=300)
    info_text=''' StockBot: Your Beginner's Guide
    to Stock Market Insights!
    Get comprehensive information 
    on stock basics,
    market trends, 
    and investment strategies. 
    Explore articles, ask questions,
    and stay informed with ease!
    '''
    # c3=Canvas(root,width=400,height=1600,background="blue",bd=0, highlightthickness=0)

        
    def information1():
        # c2.destroy()
        # # c3=Canvas(root,width=400,height=1600,background="blue",bd=0, highlightthickness=0)
        # c3.place(x=900,y=20)
        # stock_label=  Label(text=info_text, font="Times 10 italic bold",foreground="#181000",bg="red").place(x=10,y=10)
        new_canvas()
        info_label=  Label(c2,text=info_text, font="Times 16 italic bold",foreground="#181000",bg="#0077CC")
        info_label.place(x=20,y=100)
        info_back=Button(c2,text="<<BACK",fg="#181000",font=("arial",19),command=info_back1,bg="#0077CC")
        info_back.place(x=50,y=500)
        
    def info_back1():
        root.destroy()
        main()
        

    def proceed1():
        root.destroy()
        from first_page import first
        first()


    # info_back.destroy()

    information=Button(c2,text="ABOUT THE APPLICATION",fg="light green",font=("arial",19),command=information1,background="#0077CC")
    information.place(x=30,y=200)
    proceed=Button(c2,text="PROCEED",fg="light green",font=("arial",19),command=proceed1,background="#0077CC")
    proceed.place(x=100,y=300)
    def new_canvas():
        proceed.destroy()
        information.destroy()



    root.mainloop()
    
main()