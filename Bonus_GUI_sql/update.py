import tkinter as tk
from tkinter import ttk,messagebox
import pymysql
import db_dict
def update():
    db_setting = db_dict.dict()
    conn = pymysql.connect(**db_setting)
    cursor = conn.cursor()
    def submit():
        def up():
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
                try:
                    db_setting = db_dict.dict()
                    conn = pymysql.connect(**db_setting)
                    cursor = conn.cursor()
                    cursor.execute(f"UPDATE bmr_chart SET gender='{gender}',weight = '{weight}',height='{height}',age='{age}' WHERE name='{name}' AND id='{id}'")
                    conn.commit()
                    print("已更新")
                    messagebox.showinfo("訊息","資料更新成功！")
                    update_wnd.destroy()
                except:
                    print("更新失敗")
        name = name_text.get()
        id = id_text.get()
        try:
            cursor.execute(f"SELECT * FROM bmr_chart WHERE name = '{name}' AND id = '{id}'")
            line = cursor.fetchall()
            line = line[0]
            conn.commit()
            conn.close()
            gender_label  = tk.Label(update_wnd,text="請選擇性別:")
            gender_label.place(relx=0.25,rely=0.3,anchor="n")
            n = tk.StringVar()
            onthchoosen = ttk.Combobox(update_wnd, width = 17, textvariable = n)
            onthchoosen['values'] = ('男生', '女生')
            onthchoosen.place(relx=0.65,rely=0.3,anchor="n")
            height_label  = tk.Label(update_wnd,text="請輸入身高(單位：公分):")
            height_label.place(relx=0.25,rely=0.35,anchor="n")
            height_text = tk.Entry(update_wnd)
            height_text.place(relx=0.65,rely=0.35,anchor= 'n')
            weight_label = tk.Label(update_wnd,text="請輸入體重(單位：公斤):")
            weight_label.place(relx=0.25,rely=0.4,anchor="n")
            weight_text = tk.Entry(update_wnd)
            weight_text.place(relx=0.65,rely=0.4,anchor= 'n')
            age_label = tk.Label(update_wnd,text="請輸入年齡:")
            age_label.place(relx=0.25,rely=0.45,anchor="n")
            age_text = tk.Entry(update_wnd)
            age_text.place(relx=0.65,rely=0.45,anchor= 'n')
            update_button= tk.Button(update_wnd,text='update',command = up,underline=-1)
            update_button.place(relx= 0.6, rely= 0.6, anchor = 'n')
        except:
            messagebox.showinfo("訊息","查無此人！")
    def close():
        update_wnd.destroy()
    update_wnd = tk.Tk()
    update_wnd.geometry("400x400")
    update_wnd.title("update_data")
    name_label  = tk.Label(update_wnd,text="請輸入欲更新的名字:")
    name_label.place(relx=0.25,rely=0.2,anchor="n")
    name_text = tk.Entry(update_wnd)
    name_text.place(relx=0.65,rely=0.2,anchor= 'n')
    id_label = tk.Label(update_wnd,text="請輸入欲更新的身分證字號:")
    id_label.place(relx=0.25,rely=0.25,anchor="n")
    id_text = tk.Entry(update_wnd)
    id_text.place(relx=0.65,rely=0.25,anchor= 'n')
    submit_button= tk.Button(update_wnd,text='submit',command = submit,underline=-1)
    submit_button.place(relx= 0.3, rely= 0.6, anchor = 'n')
    close_button= tk.Button(update_wnd,text='close',command = close,underline=-1)
    close_button.place(relx= 0.9, rely= 0.6, anchor = 'n')
    update_wnd.mainloop()