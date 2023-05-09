import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
import insert
import query
import delete
import update
import download

wnd = tk.Tk()
wnd.geometry("400x400")
name = ""
id = ""
wnd.title("first bmi database")
add_button = tk.Button(wnd,text="Add Data",underline=-1,command=insert.add)
add_button.place(relx=0.15,rely=0.75,anchor="center")
delete_button = tk.Button(wnd,text="delete Data",underline=-1,command=delete.main)
delete_button.place(relx=0.37,rely=0.75,anchor="center")
query_button = tk.Button(wnd,text="query Data",underline=-1,command=query.main)
query_button.place(relx=0.6,rely=0.75,anchor="center")
update_button = tk.Button(wnd,text="update Data",underline=-1,command=update.update)
update_button.place(relx=0.85,rely=0.75,anchor="center")
update_button = tk.Button(wnd,text="download Data",underline=-1,command=download.download)
update_button.place(relx=0.3,rely=0.9,anchor="center")
close_button = tk.Button(wnd, text="close",underline=-1,command=wnd.destroy)
close_button.place(relx=0.7,rely=0.9,anchor="center")
wnd.mainloop()

