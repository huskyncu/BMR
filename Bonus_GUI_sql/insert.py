import tkinter as tk
from tkinter import ttk,messagebox
import pymysql
import db_dict
def add():
    db_settings =db_dict.dict()
    def submit():
        name = name_text.get()
        id = id_text.get()
        weight = weight_text.get()
        height = height_text.get()
        age = age_text.get()
        gender_str = onthchoosen.get()
        if gender_str == "男生":
              gender = '1'
        else:
              gender = '2'
        if name!="" and id!="" and weight!="" and height!="" and age !="" and gender !="":
            #new(name,id,gender,height,weight,age)
            conn = pymysql.connect(**db_settings)
            try:
                cursor = conn.cursor()
                cursor.execute(f"INSERT INTO bmr_chart(num,id,name,gender,weight,height,age) VALUES (NULL,'{id}','{name}','{gender}','{weight}','{height}','{age}');")
                conn.commit()
                conn.close()
                messagebox.showinfo('訊息',name+'的資料已新增完成')
            except Exception as e:
                conn.close()
                print(e)
        else:
            messagebox.showinfo('訊息','資料未填寫完！')
    def close():
        add_wnd.destroy()
    add_wnd = tk.Tk()
    add_wnd.geometry("400x400")
    add_wnd.title("add_data")
    name_label  = tk.Label(add_wnd,text="請輸入名字:")
    name_label.place(relx=0.25,rely=0.2,anchor="n")
    name_text = tk.Entry(add_wnd)
    name_text.place(relx=0.6,rely=0.2,anchor= 'n')
    id_label = tk.Label(add_wnd,text="請輸入身分證字號:")
    id_label.place(relx=0.25,rely=0.25,anchor="n")
    id_text = tk.Entry(add_wnd)
    id_text.place(relx=0.6,rely=0.25,anchor= 'n')
    gender_label  = tk.Label(add_wnd,text="請選擇性別:")
    gender_label.place(relx=0.25,rely=0.3,anchor="n")
    n = tk.StringVar()
    onthchoosen = ttk.Combobox(add_wnd, width = 17, textvariable = n)
    onthchoosen['values'] = ('男生', '女生')
    onthchoosen.place(relx=0.6,rely=0.3,anchor="n")
    height_label  = tk.Label(add_wnd,text="請輸入身高(單位：公分):")
    height_label.place(relx=0.25,rely=0.35,anchor="n")
    height_text = tk.Entry(add_wnd)
    height_text.place(relx=0.6,rely=0.35,anchor= 'n')
    weight_label = tk.Label(add_wnd,text="請輸入體重(單位：公斤):")
    weight_label.place(relx=0.25,rely=0.4,anchor="n")
    weight_text = tk.Entry(add_wnd)
    weight_text.place(relx=0.6,rely=0.4,anchor= 'n')
    age_label = tk.Label(add_wnd,text="請輸入年齡:")
    age_label.place(relx=0.25,rely=0.45,anchor="n")
    age_text = tk.Entry(add_wnd)
    age_text.place(relx=0.6,rely=0.45,anchor= 'n')
    submit_button= tk.Button(add_wnd,text='submit',command = submit,underline=-1)
    submit_button.place(relx= 0.4, rely= 0.6, anchor = 'n')
    close_button= tk.Button(add_wnd,text='close',command = close,underline=-1)
    close_button.place(relx= 0.6, rely= 0.6, anchor = 'n')
    add_wnd.mainloop()
# def new(name,id,gender,height,weight,age):
#     with open('data.txt', mode='a+',encoding='UTF-8') as patient_file:
#       patient_file.write(name+" "+id+" "+str(gender)+" "+str(height)+" "+str(weight)+" "+str(age)+"\n")
#     messagebox.showinfo('訊息',name+'的資料已新增完成')