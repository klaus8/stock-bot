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

def add_links():
    global links
    input_links = link_entry.get()
    new_links = input_links.split(',')
    for link in new_links:
        links.append(link.strip())
    link_entry.delete(0, tk.END)
    update_links_display()

def update_links_display():
    links_display.config(state=tk.NORMAL)
    links_display.delete(1.0, tk.END)
    for link in links:
        links_display.insert(tk.END, link + "\n")
    links_display.config(state=tk.DISABLED)

def main():
    global link_entry, links_display, links

    links = []

    root = tk.Tk()
    root.title("Link Manager")
    root.geometry("1366x768+0+0")  # Set window size

    root.configure(bg='green')  # Set background color

    root.title("KNOW YOUR ANSWER")
    root.configure(bg="#68D2E8")
    cmrit_label = Label(text="KNOW YOUR ANSWER", font="Times 20 italic bold", bg="#154360").pack(side=TOP, fill=X)
    # Set window size

    label = tk.Label(root, text="Enter URLs (separated by commas):", bg='green', font="Times 20 italic bold")
    label.place(x=400,y=40)
    # label = tk.Label(root, text="LOADING...", bg='green',font=("arial", 26))
    # label.place(x=400,y=400)
    
    my_img = Image.open("notes.png")
    re3 = my_img.resize((500, 500), Image.ANTIALIAS)
    new_pic3 = ImageTk.PhotoImage(re3)
    # l1 = Label(root, image=new_pic3)
    # l1.place(x=600, y=500)
    # c2=Canvas(root,width=100,height=1600,bg='',relief='ridge')
    c2=Canvas(root,width=1000,height=700,background=root["bg"],bd=0, highlightthickness=0)
    c2.place(x=700,y=150)
    my_img = c2.create_image(300, 250, image=new_pic3)
    # def choose_user():
    #     # label = tk.Label(root, text="LOADING...", bg='green',font=("arial", 26))
    #     # label.place(x=400,y=400)
    #     print(link_entry1.get())
    #     p=link_entry1.get()
    #     # root.destroy()
    #     # from loading import main
    #     # main(p,links)
        
    #     # root.destroy()
        
    #     from test import main
    #     print(links)

    #     result=main(links,p)
    #     print(result)
    #     root.destroy()
    #     from window import main
    #     main(result)
    #     from samm import main
    #     main()
        
        # exit(0)
        
    def choose_user():
        root.destroy()
        print(links)
        from ask_q import main
        main(links)
        

    link_entry = tk.Entry(root, width=60, font=('Arial', 20))  # Increase width and font size
    link_entry.place(x=200,y=100) # Add padding at the top and bottom

    # link_entry1 = tk.Entry(root, width=40, font=('Arial', 20), bg="grey")  # Increase width and font size
    # link_entry1.place(x=600, y=550)
    # print(link_entry1.get())

    label = tk.Label(root, text="Link References", bg='green',font=("arial", 10))
    # label.place(x=400,y=400)
    label.place(x=250,y=400)

    add_button = tk.Button(root, text="Add Links", font=('Arial', 14),command=add_links,bg="orange")
    add_button.place(x=1050,y=100)

    links_display = tk.Text(root, height=15, width=60,bg="yellow")
    links_display.place(x=50,y=150)
    links_display.config(state=tk.DISABLED)
    
    
    links_display1 = tk.Text(root, height=12, width=60)
    links_display1.place(x=50,y=420)
    
    
    links_display1.insert(END,"https://www.livemint.com/market/live-blog/adani-wilmar-share-price-live-blog-for-01-mar-2024-11709260310231.html"+"\n")
    links_display1.insert(END,"https://www.business-standard.com/companies/news/tata-motors-plans-jaguar-land-rover-ev-imports-to-india-under-new-policy-124041801039_1.html"+"\n")
    links_display1.insert(END,"https://www.businesstoday.in/markets/company-stock/story/suzlon-energy-share-price-target-rs-54-jm-shares-targets-for-tata-power-sjvn-ntpc-bhel-adani-power-cesc-419436-2024-02-29"+"\n")
    links_display1.config(state=tk.DISABLED)

    clientb = Button(root, text="PROCEED", bg="#C39BD3", height=2, font="Times 15 bold",
                     command=choose_user, padx=5)
    clientb.place(x=550, y=200)
    def backk():
        root.destroy()
        from first_page import first
        first()
    clientb = Button(root, text="<<BACK", bg="#C39BD3", height=2, font="Times 15 bold",
                     command=backk, padx=5)
    clientb.place(x=50, y=40)

    root.mainloop()

if __name__ == "__main__":
    main()
