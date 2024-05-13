from tkinter import *
from tkinter import ttk

import time
from tkinter import Text, Tk
import tkinter.messagebox as tmsg
from PIL import ImageTk,Image

global user3
def main(links):
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
    user.place(x=20, y=200)
    def answer():
    #    root1.destroy()
        # label = tk.Label(root, text="LOADING...", bg='green',font=("arial", 26))
    #     # label.place(x=400,y=400)
        print(user.get())
        p=user.get()
    #     # root.destroy()
        # from loading import main
        # main(p,links)
        
        
    #     # root.destroy()
        
        from test import main
        print(links)

        result=main(links,p)
        # lines = split_text_into_lines(result, 12)
        # for line in lines:
        #     mylist.insert(END, line)
        print(result)
        root1.destroy()
        from window import main
        main(result)
        # from samm import main
        # main()
        from ask_q import main
        main(links)
        
    frame = Frame(root1, bg='green', padx=20, pady=20)  # Set background color of the frame and add padding
    frame.place(x=100,y=700)

    # Determine the size of the scrollbar and listbox
    # scrollbar_width = int(window_width * 0.05)  # 5% of window width
    # listbox_width = int(window_width * 0.75)  # 75% of window width
    # listbox_height = int(window_height * 0.8)  # 80% of window height

    # Create the scrollbar and listbox
    scrollbar = Scrollbar(frame, width="5")
    scrollbar.pack(side=RIGHT, fill=Y)

    mylist = Listbox(frame, yscrollcommand=scrollbar.set, width="100", height="100", font=('Arial', 12), bg='#223344', bd=2, relief='ridge')
    
    # Split text into lines with 12 words per line
    def split_text_into_lines(text, words_per_line):
        words = text.split()
        lines = []
        current_line = ''
        for word in words:
            current_line += word + ' '
            if len(current_line.split()) >= words_per_line:
                lines.append(current_line.strip())
                current_line = ''
        if current_line:
            lines.append(current_line.strip())
        return lines

    

    # Insert each line into the Listbox
    

    mylist.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=mylist.yview)    
        
    
    admin_button = Button(c1,
                        text="Search",
                        bg="#117864", height=1, width=20, font="Times 20 bold", command=answer)
    admin_button.place(x=800, y=250)

    def backk():
        root1.destroy()
        from first_page import first
        first()

    clientb = Button(root1, text="<<BACK", bg="#C39BD3", height=2, font="Times 15 bold",
                     command=backk, padx=5)
    clientb.place(x=50, y=40)
   
    root1.mainloop()

main("")

