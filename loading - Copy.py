import tkinter as tk
import tkinter as tk
from tkinter import *
from tkinter import ttk

import time
from tkinter import Text, Tk
import tkinter.messagebox as tmsg
from PIL import ImageTk,Image
import tkinter as tk
global user3

# def add_links():
#     global links
#     input_links = link_entry.get()
#     new_links = input_links.split(',')
#     for link in new_links:
#         links.append(link.strip())
#     link_entry.delete(0, tk.END)
#     update_links_display()

# def update_links_display():
#     links_display.config(state=tk.NORMAL)
#     links_display.delete(1.0, tk.END)
#     for link in links:
#         links_display.insert(tk.END, link + "\n")
#     links_display.config(state=tk.DISABLED)

def main(p,links):
    # global link_entry, links_display, links

    # links = []

    root = tk.Tk()
    root.title("Link Manager")
    root.geometry("1366x768+0+0")  # Set window size

    root.configure(bg='green')  # Set background color

    root.title("KNOW YOUR ANSWER")
    root.configure(bg="#68D2E8")
    cmrit_label = Label(text="KNOW YOUR ANSWER", font="Times 20 italic bold", bg="#154360").pack(side=TOP, fill=X)
    # Set window size

    label = tk.Label(root, text="Enter URLs (separated by commas):", bg='green')
    label.pack()
    label = tk.Label(root, text="LOADING...", bg='green',font=("arial", 26))
    label.place(x=400,y=400)
    def choose_user():
        # label = tk.Label(root, text="LOADING...", bg='green',font=("arial", 26))
        # label.place(x=400,y=400)
        # print(link_entry1.get())
        # p=link_entry1.get()
        # # root.destroy()
        
        from test import main
        print(links)

        result=main(links,p)
        print(result)
        root.destroy()
        from window import main
        main(result)
        from samm import main
        main()
        
        # exit(0)
        

    link_entry = tk.Entry(root, width=60, font=('Arial', 14))  # Increase width and font size
    link_entry.pack(pady=10)  # Add padding at the top and bottom

    link_entry1 = tk.Entry(root, width=40, font=('Arial', 14), bg="grey")  # Increase width and font size
    link_entry1.place(x=600, y=550)
    # print(link_entry1.get())
    def add_links():
        pass

    add_button = tk.Button(root, text="Add Links", command=add_links)
    add_button.pack()

    links_display = tk.Text(root, height=15, width=60)
    links_display.pack()
    links_display.config(state=tk.DISABLED)

    clientb = Button(root, text="SUBMIT", bg="#C39BD3", height=2, font="Times 15 bold",
                     command=choose_user, padx=5)
    clientb.place(x=800, y=350)
    def backk():
        root.destroy()
        from first_page import first
        first()
    clientb = Button(root, text="<<BACK", bg="#C39BD3", height=2, font="Times 15 bold",
                     command=backk, padx=5)
    clientb.place(x=50, y=40)

    root.mainloop()

# if __name__ == "__main__":
#     main()
