import calculate
import tkinter as tk
import pymysql
from tkinter import ttk, messagebox
import db_dict
from gen import gen
def main():
    # db 
    db_setting = db_dict.dict()
    conn = pymysql.connect(**db_setting)
    def submit():
        name = name_text.get()
        id = id_text.get()
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM bmr_chart WHERE name = '{name}' AND id = '{id}'")
            line = cursor.fetchall()
            line = line[0]
            conn.commit()
            # text = tk.Text(query_wnd,width='50',height='10')
            # text.place(relx=0.5,rely=0.3,anchor='n')
            # text.insert("end",print_list.printout(line))
            # 我先把list的資料str型態轉型成int型態，這樣方便我後續幾行傳入函式的的操作。
            gender = int(line[3])
            height = int(line[5])
            weight = int(line[4])
            age = int(line[6])
            # text.insert("end",calculate.cal(gender,height,weight,age))
            contacts = []
            columns = ("name","id", "gender",'height','weight','age','bmi','bmitype','idealweight','bmr','bmr_type')
            headers =("name","id", "gender",'height','weight','age','bmi','bmitype','idealweight','bmr','bmr_type')
            widthes = (80,80,80,80,80,80,80,80,90,80,80)
            tv = ttk.Treeview(query_wnd, show="headings",height=2 ,columns=columns)
            for (column, header, width) in zip(columns, headers, widthes):
                tv.column(column, width=width, anchor="w")
                tv.heading(column, text=header, anchor="w")
            def inser_data():
                """插入数据"""
                contacts.append(tuple(name,id,gen(gender),height,weight,age)+calculate.cal(gender,height,weight,age))
                for i, v in enumerate(contacts):
                    print(i,v)
                    tv.insert('', i,values=v)
            tv.place(relx=0.5,rely=0.35,anchor= 'n')
            inser_data()
            print("已完成查詢！")
            messagebox.showinfo("訊息","已完成查詢！")
        except:
            messagebox.showinfo("訊息","查無此人！")
    def close():
        query_wnd.destroy()
    query_wnd = tk.Tk()
    query_wnd.geometry("400x400")
    query_wnd.title("query_data")
    name_label  = tk.Label(query_wnd,text="請輸入名字:")
    name_label.place(relx=0.25,rely=0.2,anchor="n")
    name_text = tk.Entry(query_wnd)
    name_text.place(relx=0.6,rely=0.2,anchor= 'n')
    id_label = tk.Label(query_wnd,text="請輸入身分證字號:")
    id_label.place(relx=0.25,rely=0.25,anchor="n")
    id_text = tk.Entry(query_wnd)
    id_text.place(relx=0.6,rely=0.25,anchor= 'n')
    submit_button= tk.Button(query_wnd,text='submit',command = submit,underline=-1)
    submit_button.place(relx= 0.4, rely= 0.8, anchor = 'n')
    close_button= tk.Button(query_wnd,text='close',command = close,underline=-1)
    close_button.place(relx= 0.6, rely= 0.8, anchor = 'n')
    query_wnd.mainloop()
    conn.close()

    